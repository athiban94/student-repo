""" Testing file for testing HW08_Athiban_Parthiban """
import unittest
import HW10_Athiban_Parthiban as hw10

class TestModuleRepository(unittest.TestCase):
    """ test class to test all the function in the HW09_Athiban_Parthiban """

    def setUp(self):
        """ setup method """
        self.stevens = hw10.Repository("data", False)
        self.student_data = {'10103': {'name': 'Baldwin, C', 'completed_course': ['SSW 567', 'SSW 564', 'SSW 687', 'CS 501'], 'dept': 'SFEN', 'remaining_req': {'SSW 555', 'SSW 540'}, 'remaining_elec': 'None'}, '10115': {'name': 'Wyatt, X', 'completed_course': ['SSW 567', 'SSW 564', 'SSW 687', 'CS 545'], 'dept': 'SFEN', 'remaining_req': {'SSW 555', 'SSW 540'}, 'remaining_elec': 'None'}, '10172': {'name': 'Forbes, I', 'completed_course': ['SSW 555', 'SSW 567'], 'dept': 'SFEN', 'remaining_req': {'SSW 540', 'SSW 564'}, 'remaining_elec': {'CS 513', 'CS 501', 'CS 545'}}, '10175': {'name': 'Erickson, D', 'completed_course': ['SSW 567', 'SSW 564', 'SSW 687'], 'dept': 'SFEN', 'remaining_req': {'SSW 555', 'SSW 540'}, 'remaining_elec': {'CS 513', 'CS 501', 'CS 545'}}, '10183': {'name': 'Chapman, O', 'completed_course': ['SSW 689'], 'dept': 'SFEN', 'remaining_req': {'SSW 540', 'SSW 555', 'SSW 567', 'SSW 564'}, 'remaining_elec': {'CS 513', 'CS 501', 'CS 545'}}, '11399': {'name': 'Cordova, I', 'completed_course': ['SSW 540'], 'dept': 'SYEN', 'remaining_req': {'SYS 612', 'SYS 671', 'SYS 800'}, 'remaining_elec': 'None'}, '11461': {'name': 'Wright, U', 'completed_course': ['SYS 800', 'SYS 750', 'SYS 611'], 'dept': 'SYEN', 'remaining_req': {'SYS 612', 'SYS 671'}, 'remaining_elec': {'SSW 810', 'SSW 540', 'SSW 565'}}, '11658': {'name': 'Kelly, P', 'completed_course': ['SSW 540'], 'dept': 'SYEN', 'remaining_req': {'SYS 612', 'SYS 671', 'SYS 800'}, 'remaining_elec': 'None'}, '11714': {'name': 'Morton, A', 'completed_course': ['SYS 611', 'SYS 645'], 'dept': 'SYEN', 'remaining_req': {'SYS 612', 'SYS 671', 'SYS 800'}, 'remaining_elec': {'SSW 810', 'SSW 540', 'SSW 565'}}, '11788': {'name': 'Fuller, E', 'completed_course': ['SSW 540'], 'dept': 'SYEN', 'remaining_req': {'SYS 612', 'SYS 671', 'SYS 800'}, 'remaining_elec': 'None'}}
        self.instructor_data = [('98765', 'Einstein, A', 'SFEN', 'SSW 540', 3), ('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4), ('98764', 'Feynman, R', 'SFEN', 'SSW 564', 3), ('98764', 'Feynman, R', 'SFEN', 'CS 501', 1), ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1), ('98764', 'Feynman, R', 'SFEN', 'SSW 687', 3), ('98763', 'Newton, I', 'SFEN', 'SSW 555', 1), ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1), ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1), ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2), ('98760', 'Darwin, C', 'SYEN', 'SYS 645', 1), ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1)]
        self.major_data = {'SFEN': {'required': ['SSW 540', 'SSW 564', 'SSW 555', 'SSW 567'], 'electives': ['CS 501', 'CS 513', 'CS 545']}, 'SYEN': {'required': ['SYS 671', 'SYS 612', 'SYS 800'], 'electives': ['SSW 810', 'SSW 565', 'SSW 540']}}

    def test_Student(self):
        """ test method to test student summary """
        self.assertDictEqual(self.stevens.studentData.studentSummary, self.student_data)

    def test_Major(self):
        """ Test method for Majors """
        self.assertDictEqual(self.stevens.majorData.majorSummary, self.major_data)

    def test_Instructor(self):
        """ test method to test instructor summary """

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)