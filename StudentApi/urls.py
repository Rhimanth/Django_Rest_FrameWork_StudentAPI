"""
URL configuration for StudentApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from StudentApiApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # urls for function based views 
    path('student/v1/all',views.get_students,name="get_all_student_records"),
    path('student/v1/add',views.post_students,name="create_student_record"),
    path('student/v1/update/<int:pk>',views.put_students,name="update_student_record"),
    path('student/v1/get/<int:pk>',views.get_one_students,name="get_one_student_record"),
    path('student/v1/delete/<int:pk>',views.delete_student,name="delete_student_record"),

    # urls for class based views  using APIView

    path('student/v2',views.Student_ApiView.as_view(),name="class_based_view_1_for_SApi_using_APIView"),
    path('student/v2/<int:pk>',views.Student_ApiView.as_view(),name="class_based_view_2_for_SApi_using_APIView"),

    # urls for class based views using generics

    
]
