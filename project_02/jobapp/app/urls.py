from django.urls import path


from app import views

urlpatterns = [
    path('',views.hello),
    path('job/1',views.jobdetail),
]
 