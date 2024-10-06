from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Taking, Student

# Create your views here.

@login_required(login_url='/users/')
def index(request):
    return render(request, "query/index.html", {
        "takings": Taking.objects.all(),
        "full": False,
    })

def query(request, taking_id):
    taking = Taking.objects.get(pk=taking_id)
    student = Student.objects.get(user=request.user)
    if student in taking.students.all():
        button_label = "Cancel"
    else:
        button_label = "Enroll"
    return render(request, "query/query.html", {
        "taking": taking,
        "students": taking.students.all(),
        "students_count": taking.students.all().count(),
        "closed": (taking.status=="Close"),
        "button_label": button_label,
    })

def take(request, taking_id):
    if request.method == "POST":
        taking = Taking.objects.get(pk=taking_id)
        student = Student.objects.get(user=request.user)

        if student in taking.students.all():
                student.takings.remove(taking)
                return HttpResponseRedirect(reverse("query", args=(taking_id,)))
        else:
            if taking.students.all().count() >= taking.seats:
                return render(request, "query/index.html", {
                    "takings": Taking.objects.all(),
                    "full": True,
                })
            else:
                student.takings.add(taking)
                return HttpResponseRedirect(reverse("query", args=(taking_id,)))