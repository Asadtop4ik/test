from rest_framework import generics
from .models import Student, Test
from .serializers import StudentSerializer, TestSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TestListCreateView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestRetrieveView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


