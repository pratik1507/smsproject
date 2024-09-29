from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from adminapp.models import Student,Course



def demofunction(request):
    return HttpResponse("<h2 align=center> PFSD SDP PROJECT</h2>")
def demofunction1(request):
    return HttpResponse("<h1>K L University</h1>")
def demofunction2(request):
    return HttpResponse("<font color='green'>Student Management System</font>")
def homefunction(request):
    return render(request,"index.html")
def aboutfunction(request):
    return render(request,"about.html")
def loginfunction(request):
    return render(request,"login.html")
def contactfunction(request):
    return render(request,"contact.html")

def facultylogin(request):
    return render(request , "facultylogin.html")

def studentlogin(request):
    return render(request , "studentlogin.html")







