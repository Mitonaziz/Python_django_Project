from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(requsest):
    return HttpResponse("hello word")
def jobdetail(requsest):
    return HttpResponse("Job details page")



#"<domain>/job/1" -->job detail page