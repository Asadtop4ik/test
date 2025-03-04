from .views import StudentRetrieveView, StudentListCreateView, TestRetrieveView, TestListCreateView
from django.urls import path


urlpatterns = [
    path('', StudentListCreateView.as_view(), name='students-list-create'),
    path('students/<int:pk>/', StudentRetrieveView.as_view(), name='student-detail'),
    path('tests/', TestListCreateView.as_view(), name='test-list-create'),
    path('tests/<int:pk>/', TestRetrieveView.as_view(), name='test-detail')
]

