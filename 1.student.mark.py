from datetime import date

#input function
def numofstudentGET():
    while True:
        try:
            numofstudent = int (input('Input number of students in Your Class: '))
            if numofstudent >= 0:
                break
        except ValueError:
            continue
    return numofstudent


def studentinfoGET(numofstudent):
    student = [[0 for i in range (3)]  for i in range (numofstudent)]
    for i in range (0, numofstudent):
        student[i][0] = input("Student ID: ")
        student[i][1] = input("Student Name: ")
        sDoB, sMoB, sYoB = input("DoB (DD/MM/YYYY): ").split("/")
        student[i][2] = date(int(sYoB), int(sMoB), int (sDoB))
        i = i+1
    return student

def numofcourseGET():
    while True:
        try:
            numofcourse = int (input('Input number of Course: '))
            if numofcourse >= 0:
                break
        except ValueError:
            continue
    return numofcourse


def courseinfoGET(numofcourse):
    course = [[0 for i in range (2)]  for i in range (numofcourse)]
    for i in range (0, numofcourse):
        course[i][0] = str (input("Course ID: "))
        course[i][1] = input("Course Name: ")
        i = i+1
    return course

def transformerStudent(student):
    ID = input("Type the studentID you want to input mark: ")
    for i in range(len(student)):
        if ID == student[i][0]:
            return i

def transformerCourse(course):
    ID = input("Type the courseID you want to input/see mark: ")
    for i in range(len(course)):
        if ID == course[i][0]:
            return i

def markGET(student, course):
    mark = [[0 for i in range (numofcourse)]  for i in range (numofstudent)]
    j = transformerCourse(course)
    for i in range (len(student)):
        mark[i][j] = input("{}'s mark for {} course ( -1 if he/she doesn't take this course ):  ".format(student[i][1], course[j][1]))
    return mark

def studentLISTING(student):
    for i in range (len(student)):
       print("{}. ID: {} , Name: {} , DoB: {} ".format(i+1, student[i][0],student[i][1],student[i][2]))

def courseLISTING(course):
    for i in range (len(course)):
       print("{}. Course ID: {} , Course Name: {} ".format(i+1, course[i][0],course[i][1]))

def markLISTING(student, course, mark):
    j = transformerCourse(course)
    print("MARKSHEET FOR {} COURSE".format(course[j][1]))
    for i in range (len(student)):
         print("{}. ID: {} , Name: {} , Mark: {} \n".format(i+1, student[i][0],student[i][1],mark[i][j]))

numofstudent = numofstudentGET()
student = studentinfoGET(numofstudent)
numofcourse = numofcourseGET()
course = courseinfoGET(numofcourse)
mark = markGET(student, course)
studentLISTING(student)
courseLISTING(course)
markLISTING(student, course, mark)
       
