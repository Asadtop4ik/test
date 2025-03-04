from .views import StudentRetrieveDestroyView, StudentListCreateView, TestRetrieveView, TestListCreateView, \
TestResultListCreateView, TestResultsByTestView, TestResultsByStudentView, TestAverageScoreView, \
TestHighestScoreView

from django.urls import path


urlpatterns = [
    path('', StudentListCreateView.as_view(), name='students-list-create'),
    path('students/<int:pk>/', StudentRetrieveDestroyView.as_view(), name='student-detail'),
    path('tests/', TestListCreateView.as_view(), name='test-list-create'),
    path('tests/<int:pk>/', TestRetrieveView.as_view(), name='test-detail'),
    path('results/', TestResultListCreateView.as_view(), name='test-results-list-create'),
    path('results/student/<int:student_id>/', TestResultsByStudentView.as_view(), name='test-results-by-student'),
    path('results/test/<int:test_id>/', TestResultsByTestView.as_view(), name='test-results-by-test'),
    path('results/test/<int:test_id>/average/', TestAverageScoreView.as_view(), name='test-average-score'),
    path('results/test/<int:test_id>/highest/', TestHighestScoreView.as_view(), name='test-highest-score'),
]

