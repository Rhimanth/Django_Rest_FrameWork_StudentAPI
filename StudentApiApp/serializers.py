from rest_framework import serializers
from .models import Standard,Student,School

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"
class StandarcSerializer(serializers.ModelSerializer):
    class meta:
        model=Standard
        fields="__all__"
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields="__all__"