from rest_framework import serializers

from students.models import Student, Institute


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "fullname", "student_type", "institute", "contract_amount", "created_at"]


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "fullname", "student_type", "institute", "contract_amount", "created_at"]


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ["created_at", "updated_at"]


class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ["created_at", "updated_at"]

