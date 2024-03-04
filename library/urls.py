from . import views
from django.urls import path

urlpatterns = [
    path("", views.landing, name="landing"),
    path('createuser/', views.create_user, name='createuser'),
    path("success/", views.success, name="success"),
    path("login/", views.login, name="login"),
]