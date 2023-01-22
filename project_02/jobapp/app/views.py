from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(requsest):
    return HttpResponse("<h1>hello word</h1>")
def jobdetail(requsest, id):
    return HttpResponse(f"<h1>Job details page {id}</h1>")



#"<domain>/job/1" -->job detail page