from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect #that means one when i use a id and located anoter page 

job_title= [
    "First Job",
    "Second Job",
    "Third job" 
    
]
job_description=[
    "First job description ",
    "Second job description",
    "Third job description"

]
def joblist(requsest):
    #<ul><li>job 1</li> <li>job 2</li> <li>job 3</li>
   
    list_of_jobs = "<ul>"
    for i in job_title :
        job_id =job_title.index(i)
        list_of_jobs += f"<li><a href='job/{job_id}'>{i}</a></li>"
    list_of_jobs += "</ul>"
    return HttpResponse(list_of_jobs)
 
 # Create your views here.
 #def hello(requsest):
 #   return HttpResponse("<h1>hello word</h1>")
#def jobdetail(requsest, id):
    
  # return HttpResponse(f"<h1>Job details page {id}</h1>")
    #make a site urls click
    site="https://google.com"
    return HttpResponse(f"visit <a href={site}>google here</a>")



def jobnew(requsest,id):
    print (type (id)) #this id is string so we convert this id string to int
   
     
    
    return_html = f"<h1>{job_title [int (id)]}</h1> <h3>{job_description[int (id)]} "
    return HttpResponse(return_html)

def jobwork(requsest,id):
    print (type (id)) #this id is string so we convert this id string to int
      
    if id == 0:
     return redirect("/")#/ meance home page 
    
    
    return_html = f"<h1>{job_title [id]}</h1> <h3>{job_description[ id]} "
    return HttpResponse(return_html)



#"<domain>/job/1" -->job detail page