from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from adminapp.models import Student,Course,Faculty

from facultyapp.models import CourseContent


# Create your views here.
def studenthome(request):
    sid = request.session["sid"]
    student=Student.objects.get(student_id=sid)
    print(student.student_id)
    return render(request,"studenthome.html",{"sid":sid,"student":student})


def checkstudentlogin(request):
    studentid=request.POST["sid"]
    studentpwd=request.POST["pwd"]
    flag=Student.objects.filter(Q(student_id=studentid)&Q(password=studentpwd))
    print(flag)

    if flag:
        print("login success")
        request.session["sid"] = studentid #creating new session variable sid
        student = Student.objects.get(student_id=studentid)
        print(student.student_id)
        return render(request,"studenthome.html",{"sid":studentid,"student":student})
    else:
        message = "Login Failed"
        return render(request,"studentlogin.html",{"msg":message})

def studentchangepwd(request):
    sid = request.session["sid"]
    return render(request,"studentchangepwd.html",{"sid":sid})


def studentupdatepwd(request):
    sid = request.session["sid"]
    opwd = request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(sid , opwd , npwd)
    flag = Student.objects.filter(Q(student_id = sid) & Q(password=opwd))
    if flag:
        msg1 = "Password Updated Successfully"
        Student.objects.filter(student_id = sid).update(password=npwd)
        return render(request,"studentchangepwd.html",{"sid":sid , "msg1":msg1})
    else:
        msg2 = "Old Password is Incorrect"
        return render(request,"studentchangepwd.html",{"sid":sid , "msg2":msg2})


def studentcourses(request):
    sid = request.session["sid"]
    return render(request,"studentcourses.html",{"sid":sid})

def displaystudentcourses(request):
    sid = request.session["sid"]
    ay=request.POST["academic_year"]
    sem=request.POST["semester"]
    courses=Course.objects.filter(Q(academic_year=ay)&Q(semester=sem))
    return render(request,"displaystudentcourses.html",{"courses":courses,"sid":sid})

def studentcoursecontent(request):
    sid=request.session["sid"]
    content=CourseContent.objects.all()
    return render(request,"studentcoursecontent.html",{"sid":sid,"coursecontent":content})

