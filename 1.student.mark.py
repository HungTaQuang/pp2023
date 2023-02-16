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
    print("=========================================================================================")
    return numofstudent


def studentinfoGET(numofstudent):
    student = [[0 for i in range (3)]  for i in range (numofstudent)]
    for i in range (0, numofstudent):
        student[i][0] = input("Student ID: ")
        student[i][1] = input("Student Name: ")
        sDoB, sMoB, sYoB = input("DoB (DD/MM/YYYY): ").split("/")
        student[i][2] = date(int(sYoB), int(sMoB), int (sDoB))
        print("=================================")
    print("*****************************************************************************************")
    return student

def numofcourseGET():
    while True:
        try:
            numofcourse = int (input('Input number of Course: '))
            if numofcourse >= 0:
                break
        except ValueError:
            continue
    print("=========================================================================================")
    return numofcourse


def courseinfoGET(numofcourse):
    course = [[0 for i in range (2)]  for i in range (numofcourse)]
    for i in range (0, numofcourse):
        course[i][0] = str (input("Course ID: "))
        course[i][1] = input("Course Name: ")
        print("=================================")
    print("*****************************************************************************************")
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

def menuGET():
    a = """Choose what you want to do:
    1. See the list of Students.                        2. See the list of Courses
    3. See the MARKSHEET of any course.                 4. Input mark for any course    
                                        5. EXIT"""
    print(a)
    print("=========================================================================================")
    menu = int (input("You choose: "))
    return menu

numofstudent = numofstudentGET()
student = studentinfoGET(numofstudent)
numofcourse = numofcourseGET()
course = courseinfoGET(numofcourse)
mark = [[0 for i in range (numofcourse)]  for i in range (numofstudent)]
while True:
    menu = menuGET()
    match menu:
        case 1:
            studentLISTING(student)
            input("Press Enter to continue...")
            print("=========================================================================================")

        case 2:
            courseLISTING(course)
            input("Press Enter to continue...")
            print("=========================================================================================")

        case 3:
            print("Choose the Course you want to see the Marksheet \n")
            for i in range(len(course)):
                print("{}. {} \n".format(i+1, course[i][1]))
            j = int (input("You choose: "))
            print("MARKSHEET FOR {} COURSE".format(course[j-1][1]))
            for i in range (len(student)):
                print("{}. ID: {} , Name: {} , Mark: {} \n".format(i+1, student[i][0],student[i][1],mark[i][j-1]))
            input("Press Enter to continue...")
            print("=========================================================================================")
        
        case 4:
            print("Choose the Course you want to update Marks \n")
            for i in range(len(course)):
                print("{}. {} \n".format(i+1, course[i][1]))
            j = int (input("You choose: "))
            for i in range (len(student)):
                mark[i][j-1] = input("{}'s mark for {} course ( -1 if he/she doesn't take this course ):  ".format(student[i][1], course[j-1][1]))
            input("Press Enter to continue...")
            print("=========================================================================================")
        case 5:
            break
        
