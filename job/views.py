from django.core import paginator
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Job, Category
from django.http import HttpResponse
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 1)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj, 'jobs2': job_list}
    return render(request, "job/job_list.html", context)

def job_details(request, id):
    job_detail = Job.objects.get(id=id)
    context = {'job': job_detail}
    return render(request, "job/job_detail.html", context)
