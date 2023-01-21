from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(requsest):
    return HttpResponse("hello word")