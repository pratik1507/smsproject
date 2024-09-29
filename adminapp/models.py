from django.db import models

# Create your models here.
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password=models.CharField(max_length=100,blank=False,default="klu@123")

    class Meta:
        db_table = "admin_table"
    def __str__(self):
        return self.username


class Course(models.Model):
    id=models.AutoField(primary_key=True)
    department_choices=(("CSE(Regular)","CSE(R)"),("CSE(HONORS)","CSE(H)"),("CS&IT","CSIT"))
    department = models.CharField(max_length=100, blank=False,choices=department_choices)
    program_choices = (("B.TECH", "B.TECH"), ("M.TECH", "M.TECH")) #tuple
    Program = models.CharField(max_length=100, blank=False, choices=program_choices)  # B.Tech or M.Tech
    academic_choices=(("2022-23","2022-23"),("2023-24","2023-24"))
    academic_year = models.CharField(max_length=100, blank=False,choices=academic_choices)  # 2023-24
    semester_choices=(("ODD","ODD"),("EVEN","EVEN"))
    semester = models.CharField(max_length=10, blank=False,choices=semester_choices)
    year = models.IntegerField(blank=False)  # 1 or 2 or 3
    Coursecode=models.CharField(max_length=20,blank=False) #21TS3001
    CourseTitle=models.CharField(max_length=100,blank=False)#python fullstack web development
    ltps=models.CharField(max_length=10 ,blank=False)#2-0-2-0
    credits = models.FloatField(blank=False)

    class Meta:
        db_table="course_table"
    def __str__(self):
        return self.Coursecode

class Student(models.Model):
    id = models.AutoField(primary_key=True) #this is for records not student_id
    student_id = models.BigIntegerField(blank=False) # 2100032530
    fullname = models.CharField(max_length=100,blank=False) #Rama Krishna
    gender_choices=(("Female","Female"),("Male","Male"),("Others","Others"))
    gender=models.CharField(max_length=20,blank=False,choices=gender_choices) #male or female or others
    department_choices = (("CSE(Regular)", "CSE(R)"), ("CSE(HONORS)", "CSE(H)"), ("CS&IT", "CSIT"))
    department=models.CharField(max_length=100,blank=False,choices=department_choices) # CSE ,ECE
    program_choices=(("B.TECH","B.TECH"),("M.TECH","M.TECH"))
    Program = models.CharField(max_length=100, blank=False,choices=program_choices) #B.Tech or M.Tech
    semester_choices=(("ODD","ODD"),("EVEN","EVEN"))
    semester = models.CharField(max_length=10, blank=False,choices=semester_choices) #odd or even
    year = models.IntegerField(blank=False)  # 1 or 2 or 3
    password=models.CharField(max_length=100,blank=False,default="klu@123")
    email=models.CharField(max_length=50,blank=False,unique=True)
    contact=models.CharField(max_length=20,blank=False,unique=True)

    class Meta:
        db_table="student_table"
    def __str__(self):
        return str(self.student_id)

class Faculty(models.Model):
    id = models.AutoField(primary_key=True) #this is for records not student_id
    faculty_id = models.BigIntegerField(blank=False,unique=True) # 4654
    fullname = models.CharField(max_length=100,blank=False) #Jonnalagadda SuryaKiran
    gender_choices = (("Female", "Female"), ("Male", "Male"), ("Others", "Others"))
    gender=models.CharField(max_length=20,blank=False,choices=gender_choices) #male or female or others
    department_choices = (("CSE(Regular)", "CSE(R)"), ("CSE(HONORS)", "CSE(H)"), ("CS&IT", "CSIT"))
    department=models.CharField(max_length=100,blank=False,choices=department_choices) # CSE ,ECE
    qualification_choices=(("B.TECH","B.TECH"),("M.TECH","M.TECH"),("Ph.D","Ph.D"))
    qualification = models.CharField(max_length=100, blank=False,choices=qualification_choices) # B.Tech or M.Tech or p.hd
    designation_choices=(("Professor","Professor"),("AssistantProfessor","AssistantProfessor"))
    designation = models.CharField(max_length=100, blank=False,choices=designation_choices) #Professor or AssistantProfessor or
    password=models.CharField(max_length=100,blank=False,default="klu@123")
    email=models.CharField(max_length=50,blank=False,unique=True)
    contact=models.CharField(max_length=20,blank=False,unique=True)

    class Meta:
        db_table="faculty_table"

    def __str__(self):
        return str(self.faculty_id)

class FacultyCourseMapping(models.Model):
    mappingid = models.AutoField(primary_key =True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE) #course is an object of type Course
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE) # faculty is an object of type Faculty

    component_choices = (("L","Lecture") ,("T","Tutorial"),("P","Practical"),("S","Skilling") )
    component = models.CharField(max_length=10 , blank=False , choices = component_choices)

    faculty_choices = (("Main" ,"MainFaculty") , ("Assist" , "Assistance"))
    faculty_type = models.CharField(max_length=20 , blank=False , choices = faculty_choices)

    section  = models.IntegerField(blank = False)


    class Meta:
        db_table  ="facultycourse_table"

    def __str__(self):
        return f"{self.course.CourseTitle }-{ self.faculty.faculty_id}"



