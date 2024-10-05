from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Taking, Student

# Create your views here.

@login_required(login_url='/users/')
def index(request):
    return render(request, "query/index.html", {
        "takings": Taking.objects.all()
    })

def query(request, taking_id):
    taking = Taking.objects.get(pk=taking_id)
    return render(request, "query/query.html", {
        "taking": taking,
        "students": taking.students.all(),
    })

def take(request, taking_id):
    if request.method == "POST":
        taking = Taking.objects.get(pk=taking_id)
        student = Student.objects.get()

        student.takings.add(taking)

        return HttpResponseRedirect(reverse("query", args=(taking_id,)))