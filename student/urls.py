from .views import StudentRetrieveView, StudentListCreateView
from django.urls import path


urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='students-list-create'),
    path('students/<int:pk>/', StudentRetrieveView.as_view(), name='student-detail'),
]
