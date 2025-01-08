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
from django.urls import path,include
from StudentApiApp import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'student/v5',views.Api_viewSets,basename="class_based_views_using_viewsets")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/v1/all',views.get_students,name="get_all_student_records"),
    path('student/v1/add',views.post_students,name="create_student_record"),
    path('student/v1/update/<int:pk>',views.put_students,name="update_student_record"),
    path('student/v1/get/<int:pk>',views.get_one_students,name="get_one_student_record"),
    path('student/v1/delete/<int:pk>',views.delete_student,name="delete_student_record"),

    # class based views using APIView

    path('student/v2',views.Student_ApiView.as_view(),name="class_based_views_01_using_APIView"),
    path('student/v2/<int:pk>',views.Student_ApiView.as_view(),name="class_based_views_02_using_APIView"),

    # class based views using Generics

    path('student/v3',views.Api_Generics_01.as_view(),name="class_based_views_01_using_generics"),
    path('student/v3/<int:pk>',views.Api_Generics_02.as_view(),name="class_based_views_02_using_generics"),

    # class based views using Mixins

    path('student/v4',views.Api_mixins_01.as_view(),name="class_based_views_01_using_Mixinx"),
    path('student/v4/<int:pk>',views.Api_Mixins_02.as_view(),name="class_based_views_02_using_Mixinx"),

    # class based views using modelviewsets
    path('',include(router.urls)),

]
