from django.db import models

# Create your models here.
class Student(models.Model):
    student_id=models.IntegerField(primary_key=True)
    student_name=models.CharField(max_length=200)
    student_gender=models.CharField(max_length=10)
    student_age=models.IntegerField()
    def __str__(self):
        return self.student_name
class Standard(models.Model):
    class_id=models.IntegerField(primary_key=True)
    class_name=models.CharField(max_length=100)
    class_Mentor=models.CharField(max_length=100)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    def __str__(self):
        return self.class_name
class School(models.Model):
    school_id=models.IntegerField(primary_key=True)
    school_name=models.CharField(max_length=200)
    school_address=models.CharField(max_length=200)
    Standard=models.ForeignKey(Standard,on_delete=models.CASCADE)
    def __str__(self):
        return self.school_name