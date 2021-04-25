from django.shortcuts import render
from .models import Job, Category
from django.http import HttpResponse
# Create your views here.

def job_list(request):
    return HttpResponse("LIST OF JOBS HERE")

def job_details(request, id):
    pass