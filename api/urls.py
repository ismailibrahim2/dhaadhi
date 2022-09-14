from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.course_list, name='course_list'),
]
