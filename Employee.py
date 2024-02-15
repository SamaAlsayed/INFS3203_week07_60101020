class Employee:
    def __init__(self, name, age, emp_id, department):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.department = department

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def create_employee(self, name, age, emp_id, department):
        employee = Employee(name, age, emp_id, department)
        self.employees.append(employee)

    def get_employee_by_id(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                return employee
        return None

    def delete_employee_by_id(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                return True
        return False
import unittest

class TestEmployeeManagementSystem(unittest.TestCase):
    def setUp(self):
        self.system = EmployeeManagementSystem()

    def test_create_employee(self):
        self.system.create_employee("Alice", 30, 1, "HR")
        self.assertEqual(len(self.system.employees), 1)

    def test_get_employee_by_id(self):
        self.system.create_employee("Bob", 35, 2, "Engineering")
        employee = self.system.get_employee_by_id(2)
        self.assertEqual(employee.name, "Bob")

    def test_delete_employee_by_id(self):
        self.system.create_employee("Charlie", 25, 3, "Marketing")
        self.system.delete_employee_by_id(3)
        self.assertEqual(len(self.system.employees), 0)

if __name__ == "__main__":
    unittest.main()
