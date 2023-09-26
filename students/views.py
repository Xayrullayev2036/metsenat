from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from students.models import Student, Institute
from students.serializers import (StudentSerializer,
                                  StudentCreateSerializer,
                                  StudentUpdateSerializer,
                                  StudentListSerializer,
                                  StudentDetailSerializer, InstituteSerializer)


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return StudentCreateSerializer
        elif self.action in ("update", "partial_update"):
            return StudentUpdateSerializer
        elif self.action == "list":
            return StudentListSerializer
        elif self.action == "retrieve":
            return StudentDetailSerializer
        return StudentSerializer


class InstituteViewSet(ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer
    permission_classes = [IsAuthenticated]
