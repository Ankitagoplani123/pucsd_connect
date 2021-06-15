from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("my_profile/<username>", views.profile, name="profile"),
    path("profiles/<username>", views.profiles, name="profiles"),
    path("allot_role", views.allot_role, name="allot_role"),
    path("academicProfile/<username>", views.academicProfile, name="academicProfile"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("job_details/<username>", views.job_details, name="job_details"),
]
