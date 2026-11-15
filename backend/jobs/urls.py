# backend/jobs/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .views import index_view

urlpatterns = [
    # Job endpoints
    path("jobs/", views.job_list, name="job-list"),
    path("jobs/<int:pk>/", views.job_detail, name="job-detail"),
    path("jobs/create/", views.create_job, name="create-job"),
    path("jobs/<int:pk>/edit/", views.update_delete_job, name="update-delete-job"),
    path("jobs/search/", views.search_jobs, name="search-jobs"),
    path("jobs/<int:pk>/apply/", views.apply_to_job, name="apply-to-job"),
    
    # Auth endpoints
    path("register/", views.register, name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", index_view, name="index"),
    path("jobs/<int:pk>/applications/", views.view_job_applications, name="job-applications"),
]