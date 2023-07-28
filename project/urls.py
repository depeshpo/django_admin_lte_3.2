from django.urls import path, include

urlpatterns = [
    path('', include('project.pages.urls')),
    path('dashboard/', include('project.dashboard.urls')),
    path('accounts/', include('project.user.urls')),
]
