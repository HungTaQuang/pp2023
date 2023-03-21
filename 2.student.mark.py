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


class Student:
    def __init__(self, id, name, DoB):
        self.__id = id
        self.__name = name
        self.__DoB = DoB

    def getID(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDoB(self):
        return self.__DoB

    def printStu(self):
        print("ID: {}, Name: {}, DoB: {}.".format(self.__id, self.__name, self.__DoB))

    
def studentinfoGET(numofstudent):
    student=[]
    for i in range (0, numofstudent):
        id = input("Student ID: ")
        name = input("Student Name: ")
        sDoB, sMoB, sYoB = input("DoB (DD/MM/YYYY): ").split("/")
        DoB = date(int(sYoB), int(sMoB), int (sDoB))
        student.append(Student(id, name, DoB))
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


class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__mark = []

    def getID(self):
        return self.__id

    def getName(self):
        return self.__name

    def markGET(self, student):
        sID = Student.getID()
        mark = -1
        while mark < 0  or mark > 20:
            try:
                mark = float(input("Input the student {}'s mark: ".format(student.getName())))
            except ValueError:
                continue
        if len(self.__mark) > 0:
            for i in self.__mark:
                if i['ID'] == sID:
                    i['mark'] == mark
                    return
        self.__mark.append({'ID': sID, 'mark': mark})

   
    def printCou(self):
        print("ID: {}, Name: {}.".format(id, self.name))
    
def courseinfoGET(numofcourse):
    course=[]
    for i in range (0, numofcourse):
        id = str (input("Course ID: "))
        name = input("Course Name: ")
        course.append(Course(id, name))
        print("=================================")
    print("*****************************************************************************************")
    return course


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
studentlist = studentinfoGET(numofstudent)
numofcourse = numofcourseGET()
courselist = courseinfoGET(numofcourse)


while True:
    menu = menuGET()
    match menu:
        case 1:
            for i in studentlist:
                i.printStu()
            input("Press Enter to continue...")
            print("=========================================================================================")

        case 2:
            for i in courselist:
                i.printCou()
            input("Press Enter to continue...")
            print("=========================================================================================")

        case 4:
            print("Choose the Course you want to update Marks \n")
            for i in courselist:
                i.printCou()
            choose = int (input("You choose: "))
             

## GOT LOST !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                


        
