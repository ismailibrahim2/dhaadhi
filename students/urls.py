from django.urls import path
from . import views
app_name = 'students'

urlpatterns = [
    path('join/login/', views.login_request, name='login'),
    path('join/signup/', views.register_page, name='register'),
    path('', views.home, name='homepage'),
]
