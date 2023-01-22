from django.urls import path


from app import views

urlpatterns = [
    path('',views.hello),
    path('job/<id>',views.jobdetail),
    path('job2/<id>',views.jobnew),
]
  #dainamic  path('job/<id>',views.jobdetail),