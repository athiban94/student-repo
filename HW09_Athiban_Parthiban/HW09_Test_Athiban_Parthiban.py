""" Testing file for testing HW08_Athiban_Parthiban """
import unittest
import HW09_Athiban_Parthiban as hw09

class TestModuleRepository(unittest.TestCase):
    """ test class to test all the function in the HW09_Athiban_Parthiban """

    def setUp(self):
        """ setup method """
        self.stevens = hw09.Repository("/Users/athibanp/athiban/ms-cs/SSW-810/Assignments/HW09_Athiban_Parthiban/data", False)
        self.student_data = {'10103': {'name': 'Baldwin, C', 'completed_course': ['SSW 567', 'SSW 564', 'SSW 687', 'CS 501']}, 
                            '10115': {'name': 'Wyatt, X', 'completed_course': ['SSW 567', 'SSW 564', 'SSW 687', 'CS 545']}, 
                            '10172': {'name': 'Forbes, I', 'completed_course': ['SSW 555', 'SSW 567']}, 
                            '10175': {'name': 'Erickson, D', 'completed_course': ['SSW 567', 'SSW 564', 'SSW 687']}, 
                            '10183': {'name': 'Chapman, O', 'completed_course': ['SSW 689']}, 
                            '11399': {'name': 'Cordova, I', 'completed_course': ['SSW 540']}, 
                            '11461': {'name': 'Wright, U', 'completed_course': ['SYS 800', 'SYS 750', 'SYS 611']}, 
                            '11658': {'name': 'Kelly, P', 'completed_course': ['SSW 540']}, 
                            '11714': {'name': 'Morton, A', 'completed_course': ['SYS 611', 'SYS 645']}, 
                            '11788': {'name': 'Fuller, E', 'completed_course': ['SSW 540']}}
        self.instructor_data = [('98765', 'Einstein, A', 'SFEN', 'SSW 540', 3), ('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4), ('98764', 'Feynman, R', 'SFEN', 'SSW 564', 3), ('98764', 'Feynman, R', 'SFEN', 'CS 501', 1), ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1), ('98764', 'Feynman, R', 'SFEN', 'SSW 687', 3), ('98763', 'Newton, I', 'SFEN', 'SSW 555', 1), ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1), ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1), ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2), ('98760', 'Darwin, C', 'SYEN', 'SYS 645', 1), ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1)]

    def test_Student(self):
        """ test method to test student summary """
        self.assertTrue(self.stevens.studentData.studentSummary == self.student_data)
    
    def test_Instructor(self):
        """ test method to test instructor summary """

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)