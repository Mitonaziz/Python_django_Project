from django.urls import path

from app.views import hello


urlpatterns = [
    path('',hello)
]
 