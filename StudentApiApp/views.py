from django.shortcuts import render
from .models import School,Standard,Student
from .serializers import StandarcSerializer,StudentSerializers,SchoolSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

# Function based Views

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

# Class Based Views Using APIView 

class Student_ApiView(APIView):

    # for get all student records or individual record
    def get(self,request,pk=None):
        if pk:
            try:
                query=Student.objects.get(pk=pk)
            except Student.DoesNotExist:
                return Response({"Details":"No Student Found by the given id"})
            serializer=StudentSerializers(query)
            return Response(serializer.data)
        else:
            query=Student.objects.all()
            serializer=StudentSerializers(query,many=True)
            return Response(serializer.data)
    # for to create a student record
    def post(self,request):
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return serializer.errors
    # for to update the existing student record
    def put(self,request,pk):
        query=Student.objects.get(pk=pk)
        serializer=StudentSerializers(query,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    # for to delete the student record
    def delete(self,request,pk):
        try:
            query=Student.objects.get(pk=pk)
        except  Student.DoesNotExist:
            return Response({"Details":"No Student Found By Given ID"})
        query.delete()
        return Response({"Details":"Student Record Deleted Successfully !!!..."})
        
# Class  based Views Using Generics

class Api_Generics_01(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
class Api_Generics_02(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

# Class based views using GenericAPIView and Mixins

class Api_mixins_01(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class Api_Mixins_02(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    def get(self,request,pk):
        return self.retrieve(request,pk=pk)
    def put(self,request,pk):
        return self.update(request,pk=pk)
    def delete(self,request,pk):
        return self.destroy(request,pk=pk)
    

# class based views using ModelViewsets

class Api_viewSets(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    