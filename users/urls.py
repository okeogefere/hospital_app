from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('signup/', views.signup, name='signup'),
]