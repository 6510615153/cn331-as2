from django.test import TestCase
from django.contrib.auth.models import User
from django.db.models import Max
from django.urls import reverse
from .models import Status, Course, Taking, Student

# Create your tests here.

class CourseTakingTestCase(TestCase):
    def setUp(self):
        # Creating available course to take

        self.user = User.objects.create_user(username='testuser', password='test4269')
        # self.user2 = User.objects.create_user(username='testuser2', password='test42692')

        course1 = Course.objects.create(course_code="CN001", course_name="Basic Computer", course_semester="1", course_year="2024")

        status1 = Status.objects.create(status_code="Open")
        status2 = Status.objects.create(status_code="Close")

        taking1 = Taking.objects.create(status=status1, current_course=course1, seats=2)

        student1 = Student.objects.create(user=self.user, fname="Big", lname="Daddy")
        # student2 = Student.objects.create(user=self.user2, fname="Small", lname="Mommy")

        taking1.students.add(student1)

    def test_index_view_status_code(self):
        """ index view's status code is ok """

        self.client.force_login(self.user)

        response = self.client.get(reverse('query:index_return'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_context(self):
        """ context is correctly set """

        self.client.force_login(self.user)

        response = self.client.get(reverse('query:index_return'))
        self.assertEqual(response.context['takings'].count(), 1)

    def test_valid_taking_page(self):
        """ valid taking page should return status code 200 """

        self.client.force_login(self.user)

        taking = Taking.objects.first()
        response = self.client.get(reverse('query:query_id', args=(taking.id,)))
        self.assertEqual(response.status_code, 200)

    def test_valid_checking_page(self):
        """valid course checking page should return status code 200"""
        self.client.force_login(self.user)

        response = self.client.get(reverse('query:check'))
        self.assertEqual(response.status_code, 200)

    def test_can_stop_taking_course(self):
        """canceling taking the course is available"""
        self.client.force_login(self.user)

        taking = Taking.objects.first()

        response = self.client.post(reverse('query:take', args=(taking.id,)))

        self.assertEqual(response.status_code, 302)

    def test_cannot_take_full_course(self):
        """ course is full, cannot take"""

        self.user2 = User.objects.create_user(username='testuser2', password='test42692')
        student2 = Student.objects.create(user=self.user2, fname="Small", lname="Mommy")

        self.client.force_login(self.user2)

        taking = Taking.objects.first()
        taking.seats = 1
        taking.save()

        self.client.post(reverse('query:take', args=(taking.id,)), {'students': student2.id})
        self.assertEqual(taking.students.count(), 1)

    def test_can_take_course(self):
        """ course is available to take"""

        self.user2 = User.objects.create_user(username='testuser2', password='test42692')
        student2 = Student.objects.create(user=self.user2, fname="Small", lname="Mommy")

        self.client.force_login(self.user2)

        taking = Taking.objects.first()

        self.client.post(reverse('query:take', args=(taking.id,)), {'students': student2.id})
        self.assertEqual(taking.students.count(), 2)

    def test_whether_enroll_show(self):
        """Cancel show up for non-taker"""
        self.user2 = User.objects.create_user(username='testuser2', password='test42692')
        student2 = Student.objects.create(user=self.user2, fname="Small", lname="Mommy")
        self.client.force_login(self.user2)

        taking = Taking.objects.first()
        response = self.client.get(reverse('query:query_id', args=(taking.id,)))
        
        self.assertContains(response, "Enroll")

    def test_whether_cancel_show(self):
        """Cancel show up for non-taker"""

        self.client.force_login(self.user)

        taking = Taking.objects.first()
        response = self.client.get(reverse('query:query_id', args=(taking.id,)))
        
        self.assertContains(response, "Cancel")