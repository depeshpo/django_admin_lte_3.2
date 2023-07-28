from django.urls import path

from project.pages.views import home

urlpatterns = [
    path('', home, name='home')
]
