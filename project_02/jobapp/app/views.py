from django.shortcuts import render
from django.http import HttpResponse
job_title= [
    "First Job",
    "Second Job"
    
]
job_description=[
    "First job description ",
    "Second job description"

]


# Create your views here.
def hello(requsest):
    return HttpResponse("<h1>hello word</h1>")
def jobdetail(requsest, id):
  
 # return HttpResponse(f"<h1>Job details page {id}</h1>")
    #make a site urls click
    site="https://google.com"
    return HttpResponse(f"visit <a href={site}>google here</a>")



def jobnew(requsest,id):
    print (type (id)) #this id is string so we convert this id string to int
    return_html = f"<h1>{job_title [int (id)]}</h1> <h3>{job_description[int (id)]} "
    return HttpResponse(return_html)

#"<domain>/job/1" -->job detail page