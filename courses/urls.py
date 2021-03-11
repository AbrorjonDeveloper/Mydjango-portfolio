from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("list/", views.CourseListView.as_view(), name="courses"),
    path("detail/<slug:slug>/", views.CourseDetailView.as_view(), name="detail"),
    path("new-course/", views.CourseCreateView.as_view(), name="create"),
    path("detail/<slug:slug>/update/", views.CourseUpdateView.as_view(), name="update"),
    path("detail/<slug:slug>/delete/", views.CourseDeleteView.as_view(), name="delete"),
    # path('api/', views.apiCourse, name="API"),
    # path('api/list/', views.apiList, name="api-list"),
    # path('api/detail/<slug:slug>/', views.apiDetail, name="api-detail"),
    # path('api/create/', views.apiCreate, name="api-create"),
    # path('api/update/<str:pk>/', views.apiUpdate, name="api-update"),
    path('api/token/', obtain_auth_token, name="auth-token"),
]


