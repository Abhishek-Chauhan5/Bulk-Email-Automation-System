from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_excel, name='upload_excel'),
    path('users/', views.user_list, name='user_list'),
    path('download/', views.download_excel, name='download_excel'),
    path("history/", views.upload_history, name="upload_history"),
]