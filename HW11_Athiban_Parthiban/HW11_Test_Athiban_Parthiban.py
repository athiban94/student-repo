""" Testing file for testing HW08_Athiban_Parthiban """
import unittest
import HW11_Athiban_Parthiban as hw11

class TestModuleRepository(unittest.TestCase):
    """ test class to test all the function in the HW09_Athiban_Parthiban """

    def setUp(self):
        """ setup method """
        self.stevens = hw11.Repository("../HW10_Athiban_Parthiban/data", False)
        self.instructor_data = [('98762', 'Hawking, S', 'CS', 'CS 501', 1), ('98762', 'Hawking, S', 'CS', 'CS 546', 1), ('98764', 'Cohen, R', 'SFEN', 'CS 546', 1), ('98762', 'Hawking, S', 'CS', 'CS 570', 1), ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1), ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4)]


    def test_Instructor(self):
        """ test method to test instructor summary """
        self.assertEquals(self.stevens.ins_data_db, self.instructor_data)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)