from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("list/", views.CourseListView.as_view(), name="courses"),
    path("detail/<slug:slug>/", views.CourseDetailView.as_view(), name="detail"),
    path("new-course/", views.CourseCreateView.as_view(), name="create"),
    path("detail/<slug:slug>/update/", views.CourseUpdateView.as_view(), name="update"),
    path("detail/<slug:slug>/delete/", views.CourseDeleteView.as_view(), name="delete"),
]


