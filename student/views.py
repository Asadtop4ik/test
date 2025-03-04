from rest_framework import generics
from .models import Student, Test, TestResult
from .serializers import StudentSerializer, TestSerializer, TestResultSerializer
from django.db.models import Avg, Max
from rest_framework.response import Response
from rest_framework.views import APIView



class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TestListCreateView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestRetrieveView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestResultListCreateView(generics.ListCreateAPIView):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer


class TestResultsByStudentView(generics.ListAPIView):
    serializer_class = TestResultSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        return TestResult.objects.filter(student_id=student_id)


class TestResultsByTestView(generics.ListAPIView):
    serializer_class = TestResultSerializer

    def get_queryset(self):
        test_id = self.kwargs['test_id']
        return TestResult.objects.filter(test_id=test_id)


class TestAverageScoreView(APIView):
    def get(self, request, test_id):
        average_score = TestResult.objects.filter(test_id=test_id).aggregate(avg_score=Avg('score'))['avg_score']
        if average_score is None:
            return Response({"message": "No results found for this test"}, status=404)
        return Response({"test_id": test_id, "average_score": average_score})


class TestHighestScoreView(APIView):
    def get(self, request, test_id):
        highest_score = TestResult.objects.filter(test_id=test_id).aggregate(highest_score=Max('score'))['highest_score']
        if highest_score is None:
            return Response({"message": "No results found for this test"}, status=404)
        return Response({"test_id": test_id, "highest_score": highest_score})



