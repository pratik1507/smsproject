from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Admin, Course, Student, Faculty, FacultyCourseMapping
from .forms import AddFacultyForm, AddStudentForm, AddCourseForm, StudentForm, FacultyForm


# Create your views here.
def adminhome(request):
    auname = request.session["auname"]
    return render(request,"adminhome.html",{"adminuname":auname})
def adminlogout(request):
    return render(request,"login.html")

def checkadminlogin(request):
    adminuname=request.POST["uname"]
    adminpwd=request.POST["pwd"]
    flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
    print(flag)

    if flag:
        print("login success")
        request.session["auname"] = adminuname #creating session variable auname
        return render(request,"adminhome.html",{"adminuname":adminuname})
    else:
        message = "Login Failed"
        return render(request,"login.html",{"msg":message})
        #return HttpResponse("Login Failed")



def viewstudents(request):
    students=Student.objects.all()
    count=Student.objects.count()
    auname = request.session["auname"]
    return render(request,"viewstudents.html",{"studentdata":students , "count":count , "adminuname":auname})

def viewfaculty(request):
    faculty=Faculty.objects.all()
    count=Faculty.objects.count()
    auname = request.session["auname"]
    return render(request,"viewfaculty.html",{"facultydata":faculty , "count":count , "adminuname":auname})

def viewcourses(request):
    courses=Course.objects.all()
    count=Course.objects.count()
    auname = request.session["auname"]
    return render(request,"viewcourses.html",{"coursesdata":courses , "count":count , "adminuname":auname})

def admincourse(request):
    auname = request.session["auname"]
    return render(request,"AdminCourse.html",{"adminuname":auname})

def adminfaculty(request):
    auname = request.session["auname"]
    return render(request,"AdminFaculty.html",{"adminuname":auname})

def adminstudent(request):
    auname=request.session["auname"]
    return render(request,"AdminStudent.html",{"adminuname":auname})



def updatecourse(request):
    auname = request.session["auname"]
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request, "updatecourse.html", {"adminuname": auname,"courses":courses,"count":count})
def updatefaculty(request):
    auname = request.session["auname"]
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request, "updatefaculty.html", {"adminuname": auname, "faculty": faculty, "count": count})


def courseupdation(request,cid):
    auname = request.session["auname"]
    return render(request,"courseupdation.html",{"cid":cid,"adminuname":auname});
def studentupdation(request,sid):
    auname = request.session["auname"]
    student=get_object_or_404(Student,pk=sid)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            msg = "Student Updated Successfully"
            return render(request,"studentupdated.html",{"form":form,"msg":msg,"adminuname":auname})
        else:
            msgf = "Updation Failed"
            return render(request,"studentupdated.html",{"form":form,"msg":msgf,"adminuname":auname})
    else:
        form=StudentForm(instance=student)
    return render(request,"studentupdated.html",{"form":form,"adminuname":auname});

def facultyupdation(request,fid):
    auname = request.session["auname"]
    faculty=get_object_or_404(Faculty,pk=fid)
    if request.method=="POST":
        form=FacultyForm(request.POST,instance=faculty)
        if form.is_valid():
            form.save()
            msg = "Faculty Updated Successfully"
            return render(request,"facultyupdated.html",{"form":form,"msg":msg,"adminuname":auname})
        else:
            msgf = "Updation Failed"
            return render(request,"facultyupdated.html",{"form":form,"msg":msgf,"adminuname":auname})
    else:
        form=FacultyForm(instance=faculty)
    return render(request,"facultyupdated.html",{"form":form,"adminuname":auname});


def courseupdated(request):
    auname = request.session["auname"]
    cid=request.POST["cid"]
    ctitle = request.POST["coursetitle"]
    ltps = request.POST["ltps"]
    credits = request.POST["credits"]
    Course.objects.filter(id=cid).update(CourseTitle=ctitle,ltps=ltps,credits=credits)
    msg="Course Updated Successfully"
    return render(request,"courseupdation.html",{"msg":msg,"adminuname":auname})




def addfaculty(request):
    auname = request.session["auname"]
    return render(request,"addfaculty.html",{"adminuname":auname})

def addstudent(request):
    auname = request.session["auname"]
    return render(request,"addstudent.html",{"adminuname":auname})

def insertcourse(request):
    auname = request.session["auname"]
    dept=request.POST['dept']
    program=request.POST['program']
    academicyear=request.POST['academicyear']
    semester=request.POST['semester']
    year=request.POST['year']
    coursecode=request.POST['coursecode']
    coursetitle=request.POST['coursetitle']
    ltps = request.POST['ltps']
    credits = request.POST['credits']


    course =Course(department=dept,Program=program,academic_year=academicyear,semester=semester,year=year,Coursecode=coursecode,CourseTitle=coursetitle , ltps=ltps , credits=credits)

    Course.save(course)
    message="Course Added Successfully"
    return render(request,"addcourse.html",{"msg":message})



def deletecourse(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]
    return render(request, "deletecourse.html", {"coursesdata": courses, "count": count , "adminuname":auname})

def coursedeletion(request,cid):
    Course.objects.filter(id=cid).delete()
    return redirect("deletecourse")

def addfaculty(request):
    auname = request.session["auname"]
    form = AddFacultyForm() # non-parameterised constructor
    if request.method == "POST":
        form1 = AddFacultyForm(request.POST) # request.POST means form data
        if form1.is_valid():
            form1.save()
            message = "Faculty Added Successfully"
            return render(request,"addfaculty.html",{"msg" : message , "form":form , "adminuname":auname})
        else:
            message="Failed to Add Faculty Data"
            return render(request, "addfaculty.html", {"msgf": message, "form": form, "adminuname": auname})

    return render(request,"addfaculty.html",{"form":form , "adminuname":auname})

def addcourse(request):
    auname = request.session["auname"]
    form = AddCourseForm()
    if request.method == "POST":
        form1 = AddCourseForm(request.POST)
        if form1.is_valid():
            form1.save()
            message = "Course Added Successfully"
            return render(request, "addcourse.html", {"msg": message, "form": form, "adminuname": auname})
        else:
            message = "Failed to Add Course Data"
            return render(request, "addcourse.html", {"msgf": message, "form": form, "adminuname": auname})

    return render(request, "addcourse.html", {"form": form, "adminuname": auname})






def deletefaculty(request):
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    return render(request, "deletefaculty.html", {"facultydata": faculty, "count": count , "adminuname":auname})

def facultydeletion(request,fid):
    Faculty.objects.filter(id=fid).delete()
    return redirect("deletefaculty")

def addstudent(request):
    auname = request.session["auname"]
    form = AddStudentForm() # non-parameterised constructor
    if request.method == "POST":
        form1 = AddStudentForm(request.POST) # request.POST means form data
        if form1.is_valid():
            form1.save()
            message = "Student Added Successfully"
            return render(request,"addstudent.html",{"msg" : message , "form":form , "adminuname":auname})
        else:
            message="Failed to Add Student Data"
            return render(request, "addstudent.html", {"msgf": message, "form": form, "adminuname": auname})

    return render(request,"addstudent.html",{"form":form , "adminuname":auname})

def deletestudent(request):
    students = Student.objects.all()
    count = Student.objects.count()
    auname = request.session["auname"]
    return render(request, "deletestudent.html", {"studentdata": students, "count": count , "adminuname":auname})

def updatestudent(request):
    students = Student.objects.all()
    count = Student.objects.count()
    auname = request.session["auname"]
    return render(request, "updatestudent.html", {"studentdata": students, "count": count, "adminuname": auname})

def studentdeletion(request,sid):
    Student.objects.filter(id=sid).delete()
    return redirect("deletestudent")

def facultycoursemapping(request):
    fmcourses  = FacultyCourseMapping.objects.all()
    auname = request.session["auname"]
    return render(request,"facultycoursemapping.html",{"adminuname":auname , "fmcourses":fmcourses})


def adminchangepwd(request):
    auname = request.session["auname"]
    return render(request,"adminchangepwd.html",{"adminuname":auname})

def adminupdatepwd(request):
    auname = request.session["auname"]
    opwd = request.POST['opwd']
    npwd = request.POST['npwd']
    print(auname,opwd,npwd)
    flag = Admin.objects.filter(Q(username=auname) & Q(password = opwd))
    if flag:
        print("Old password is correct")
        Admin.objects.filter(username=auname).update(password=npwd)
        print("updated..")
        msg1= "Password Updated Successfully"
        return render(request, "adminchangepwd.html", {"adminuname": auname, "msg1": msg1})
    else:
        print("Old password is not correct")
        msg2="Old Password is Incorrect"
        return render(request,"adminchangepwd.html",{"adminuname":auname , "msg2":msg2})
