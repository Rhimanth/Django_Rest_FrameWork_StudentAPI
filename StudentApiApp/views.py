from django.shortcuts import render
from .models import School,Standard,Student
from .serializers import StandarcSerializer,StudentSerializers,SchoolSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.


@api_view(["GET"])
def get_students(request):
    query=Student.objects.all()
    serializer=StudentSerializers(query,many=True)
    return Response(serializer.data)
@api_view(["GET"])
def get_one_students(request,pk):
    try:
        query=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return "Student Record Does Not Exist In The Give Id"
    serializer=StudentSerializers(query)
    return Response(serializer.data)
@api_view(["POST"])
def post_students(request):
    serializer=StudentSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return serializer.errors
@api_view(["PUT"])
def put_students(request,pk):
    query=Student.objects.get(pk=pk)
    serializer=StudentSerializers(query,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(["DELETE"])
def delete_student(request,pk):
    try:
        query=Student.objects.get(pk=pk)
    except  Student.DoesNotExist:
        return Response({"Details":"No Student Found By Given ID"})
    query.delete()
    return Response({"Details":"Student Record Deleted Successfully !!!..."})

