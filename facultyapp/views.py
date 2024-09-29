from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from adminapp.models import Faculty,FacultyCourseMapping,Course


# Create your views here.

def checkfacultylogin(request):
    facultyid=request.POST["fid"]
    facultypwd=request.POST["pwd"]
    flag=Faculty.objects.filter(Q(faculty_id=facultyid)&Q(password=facultypwd))
    print(flag)

    if flag:
        print("login success")
        request.session["fid"] = facultyid #creating new session variable fid
        faculty = Faculty.objects.get(faculty_id=facultyid)
        return render(request,"facultyhome.html",{"fid":facultyid,"faculty":faculty})
    else:
        message = "Login Failed"
        return render(request,"facultylogin.html",{"msg":message})


def facultyhome(request):
    fid = request.session["fid"]
    faculty = Faculty.objects.get(faculty_id=fid)
    return render(request,"facultyhome.html",{"fid":fid,"faculty":faculty})

def facultycourses(request):
    fid = request.session["fid"]

    #print(fid)
    courses = Course.objects.all()
    count = Course.objects.count()
    mappingcourses = FacultyCourseMapping.objects.all()
    fmcourses=[]
    for course in mappingcourses:
        if(course.faculty.faculty_id==int(fid)):
            fmcourses.append(course)
        #print(course.faculty.faculty_id)
    print(fmcourses)
    count = len(fmcourses)

    #print(mappingcourses)
    return render(request,"facultycourses.html",{"fid":fid , "fmcourses":fmcourses, "count":count})

def facultychangepwd(request):
    fid = request.session["fid"]
    return render(request,"facultychangepwd.html",{"fid":fid})

def facultyupdatepwd(request):
    fid = request.session["fid"]
    opwd = request.POST['opwd']
    npwd = request.POST['npwd']
    print(fid, opwd, npwd)
    flag = Faculty.objects.filter(Q(faculty_id=fid) & Q(password=opwd))
    if flag:
        Faculty.objects.filter(faculty_id = fid).update(password=npwd)
        msg1 = "Password Updated Successfully"
        return render(request,"facultychangepwd.html",{"fid":fid , "msg1":msg1})
    else:
        msg2="Old Password is Incorrect"
        return render(request,"facultychangepwd.html",{"fid":fid , "msg2":msg2})





