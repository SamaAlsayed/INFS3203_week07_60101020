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
