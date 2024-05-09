from django.urls import path
from . import views

urlpatterns = [
    path('webhook_receiver/', views.webhook_receiver, name='webhook_receiver'),
    path('api/projects/', views.project_list, name='project_list'),
    path('api/projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('api/projects/<int:project_id>/builds/', views.build_history, name='build_history'),
]