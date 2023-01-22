from django.urls import path


from app import views

urlpatterns = [
    path('',views.joblist),
    #path('job/<int:id>',views.jobdetail),
    path('job/<id>',views.jobnew),#deflt id is string
    path('job/<int:id>',views.jobwork),# id is integer
    
    
   # path('job3/<str:id>',views.jobwork),#id is string but not working
]
  #dainamic  path('job/<id>',views.jobdetail),