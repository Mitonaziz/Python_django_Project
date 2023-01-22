from django.urls import path


from app import views

urlpatterns = [
    path('',views.hello),
    path('job/<id>',views.jobdetail),
    path('job2/<id>',views.jobnew),#deflt id is string
    path('job3/<int:id>',views.jobwork),# id is integer
]
  #dainamic  path('job/<id>',views.jobdetail),