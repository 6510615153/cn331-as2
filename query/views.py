from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Taking, Student

# Create your views here.

@login_required(login_url='/users/')
def index(request):
    return render(request, "query/index.html", {
        "takings": Taking.objects.all()
    })

def query(request, current_course):
    taking = Taking.objects.get()
    return render(request, "query/query.html", {
        "taking": taking,
        "students": taking.students.all(),
        "non_taker": Student.objects.exclude(takings=taking).all(),
    })

def take(request, current_course):
    if request.method == "POST":
        taking = Taking.objects.get()
        student = Student.objects.get(pk=int(request.POST["student"]))
        student.takings.add(taking)

        return HttpResponseRedirect(reverse("query", args=(current_course)))