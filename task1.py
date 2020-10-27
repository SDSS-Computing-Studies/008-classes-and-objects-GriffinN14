#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grade - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:

    # properties should be listed first
    name = ""
    studentNumber = ""
    grade = 0
    courses = []
    grades = []
    def __init__(self, name, studentNumber, grade): # You will need to create your own input parameters for all methods
        self.name = name
        self.studentNumber = studentNumber
        self.grade = grade
    def __del__(self):
        pass
    
    def getGrades(self,a,b,c,d,e,f,g):
        grades = [a,b,c,d,e,f,g]
        return grades
    
    def getCourses(self, courses):
        return courses
    def showCourses(self):
        print (self.getCourses)

    def showGrade(self, a):
        b = self.getGrades.index(a)
        c = self.getCourses.index(a)
        print(c + b)
        pass

    def average(self):
        av = 0
        grades = self.getGrades(self)
        av = grades[1] + grades[2] + grades[3] + grades[4] + grades[5] + grades[6] + grades[7]
        av = av / 7
        return av
    
    def getHonorRoll(self):
        list.sort(self.getGrades)
        av = grades[3] + grades[4] + grades[5] + grades[6] + grades[7]
        av = av / 5
        if av >= 86:
            h = True
        else:
            h = False
        return h
    
    
    def constuctor(self,a,b,c):
        pass
def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( 91, 94, 87, 99, 82, 100, 73)

    st2 = student("Joe Lunchbox","12346", 11)
    st1.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st1.getGrades( 71, 98, 93, 95, 68, 81, 71)


main()