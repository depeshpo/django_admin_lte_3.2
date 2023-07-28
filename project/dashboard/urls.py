from django.urls import path

from project.dashboard.views import home

urlpatterns = [
    path('', home, name='dashboard')
]
