""" Home Work #9 """
from prettytable import PrettyTable
import os

def file_reading_gen(path, fields, sep, header):
    """ Generator function to read file line by line by seperator """
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError("file cannot be opened")
    else:
        with fp:
            if(header == True):
                next(fp)
            for n, line in enumerate(fp):
                line = line.strip()
                data = line.split(sep)
                if(len(data) != fields):
                    raise ValueError(f"'{path}' has {len(data)} fields on line {n + 1} but expected {fields} ")
                else:
                    yield tuple(data)
    fp.close()

class Repository:
    """ class Repository to hold the students, instructors and grades for a single University """

    def __init__(self, directory, pt):
        """ constructor method to initialze """
        self.directory = directory
        self.studentData = Student(directory)
        self.instructorData = Instructor(directory)
        if(pt):
            print("inside the if, ", pt)
            self.printStudentSummary()
            self.printInstructorSummary()

    def printStudentSummary(self):
        self.studentData.printTable()

    def printInstructorSummary(self):
        self.instructorData.printTable()
    
class Student:
    """ class Student to hold all of the details of a student """

    def __init__(self, directory):
        self.directory = directory
        self.studentSummary = dict()
        self.generateStudentSummary()
    
    def generateStudentSummary(self):
        """ Function to generate student data """
        try:
            grades_list = file_reading_gen(os.path.join(self.directory, 'grades.txt'), 4, '\t', False)
            student_summary = file_reading_gen(os.path.join(self.directory, 'students.txt'), 3, '\t', False)
            for cwid, name, major in student_summary:
                if(cwid not in self.studentSummary):
                    self.studentSummary[cwid] = dict()
                    self.studentSummary[cwid]['name'] = name
                    self.studentSummary[cwid]['completed_course'] = list()

            for studentId, course, grade, instructor_id in grades_list:
                self.studentSummary[studentId]['completed_course'].append(course)
        except FileNotFoundError as fe:
            print(fe)
        except ValueError as ve:
            print(ve)

    def printTable(self):
        """ function to print pretty table """
        pt = PrettyTable(field_names=['CWID', 'Name', 'Completed Courses'])
        for cwid, data in self.studentSummary.items():
            row = [cwid, data['name'], data['completed_course']]
            pt.add_row(row)
        print(pt)

class Instructor:
    """ class Instructor to hold all of the details of an instructor """

    def __init__(self, directory):
        self.directory = directory
        self.instructorSummary = dict()
        self.instructorSummaryResult = list()
        self.generateInstructorSummary()
    
    def generateInstructorSummary(self):
        """ function to generate instructor summary data """

        grades_list = file_reading_gen(os.path.join(self.directory, 'grades.txt'), 4, '\t', False)
        instructor_summary = file_reading_gen(os.path.join(self.directory, 'instructors.txt'), 3, '\t', False)
        gradeDict = dict()
        courseMap = dict()

        for i_cwid, i_name, dept in instructor_summary:
            if(i_cwid not in self.instructorSummary):
                self.instructorSummary[i_cwid] = dict()
                self.instructorSummary[i_cwid]['name'] = i_name
                self.instructorSummary[i_cwid]['dept'] = dept
                self.instructorSummary[i_cwid]['course'] = set()
                self.instructorSummary[i_cwid]['students'] = 0

        for studentId, course, grade, instructor_id in grades_list:
            if(course in courseMap):
                courseMap[course] += 1
            else:
                courseMap[course] = 1
            
            self.instructorSummary[instructor_id]['course'].add(course)
        
        for id, data in self.instructorSummary.items():
            for c in data['course']:
                self.instructorSummaryResult.append((id, data['name'], data['dept'], c, courseMap[c]))
    
    def printTable(self):
        """ Function to print pretty table """
        pt = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Course', 'Students'])
        for data in self.instructorSummaryResult:
            pt.add_row(list(data))
        print(pt)
        


def main():
    stevens = Repository("/Users/athibanp/athiban/ms-cs/SSW-810/Assignments/HW09_Athiban_Parthiban/data", True)