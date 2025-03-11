from django.urls import path
from . import views

urlpatterns = [
    path('course/',views.course,name='course'),
    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/enroll/', views.enroll_in_course, name="enroll_in_course"),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name="lesson_detail"),
]
