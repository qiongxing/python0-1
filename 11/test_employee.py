import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('Qiong','Xing',120000)
    
    def test_normal_add_money(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annualSalary,125000)

    def test_give_custom_raise(self):
        self.employee.give_raise(1000)
        self.assertEqual(self.employee.annualSalary,121000)

unittest.main()