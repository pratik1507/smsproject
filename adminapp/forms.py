from django import forms
from .models import Faculty , Student , Course

#add faculty form will be created automatically based on Faculty model
class AddFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty # we need model for Faculty , model name
        fields = "__all__" #all fields in the model form, autofield will be hided
        exclude={"password"} #this will exclude fields
        labels = {"faculty_id":"Enter Faculty ID","fullname":"Enter FullName","gender":"Select Gender"} #you can change label names

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = {"password"}
        labels = {"student_id": "Enter Student ID", "fullname": "Enter FullName", "gender": "Select Gender"}

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        labels={"department":"Select Department","Program":"Select Program","academic_year":"Select Academic_Year"}

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        exclude={"student_id"}

class FacultyForm(forms.ModelForm):
    class Meta:
        model=Faculty
        fields="__all__"
        exclude={"faculty_id"}




