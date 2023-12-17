from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('courses', views.CourseViewSet)

app_name = 'courses'

urlpatterns = [
    path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/<int:pk>/', views.SubjectDetailView.as_view(),
         name='subject_detail'),
    path('', include(router.urls))
]
