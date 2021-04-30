from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('main.urls')),
    path("register", include('main.urls')),
    path("contact", include('main.urls')),
    path("profile/<username>", include('main.urls')),
    path("academicProfile/<username>", include('main.urls')),
    path("login", include('main.urls')),
    path("job_details/<username>", include('main.urls')),
]

urlpatterns += staticfiles_urlpatterns()
