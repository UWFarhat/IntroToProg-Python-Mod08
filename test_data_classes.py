# ------------------------------------------------- #
# Title: Data Classes Unit Tests
# Description: Contains unit tests for the classes in data_classes.py.
# ChangeLog: (Who, When, What)
# mofarhat, 3/8/2026, Created Script
# ------------------------------------------------- #

import unittest
from data_classes import Person
from data_classes import Employee

if __name__ == "__main__":
    unittest.main()

# Define a function to test the Person and Student classes
class TestPerson(unittest.TestCase):
   def test_person_init_valid(self):
       # Test Person class stores the correct value
       person = Person("John", "Doe")

       self.assertEqual(person.first_name, "John")  # Checks for correct value and .title() formatting
       self.assertEqual(person.last_name, "Doe")  # Checks for correct value and .title() formatting

   def test_person_invalid_names(self):
       # Test Person class does not store incorrect values
       person = Person("John", "Doe")

       # Test invalid first name
       with self.assertRaises(ValueError) as context:
           person.first_name = "J0hn"
       self.assertTrue("should not contain numbers" in str(context.exception))

       # Test invalid last name
       with self.assertRaises(ValueError) as context:
           person.last_name = "D0e"
       self.assertTrue("should not contain numbers" in str(context.exception))

class TestEmployee(unittest.TestCase):
   """Tests the Employee class for inheritance and validation."""

   def test_employee_init_valid(self):
       employee = Employee("alice", "smith", "2025-01-01", 5)

       # Check inherited properties
       self.assertEqual(employee.first_name, "Alice")
       self.assertEqual(employee.last_name, "Smith")

       # Check new properties
       self.assertEqual(employee.review_date, "2025-01-01")
       self.assertEqual(employee.review_rating, 5)

   def test_employee_invalid_review_date(self):
       """Test that setting an improperly formatted date raises a ValueError."""
       employee = Employee()

       with self.assertRaises(ValueError) as context:
           employee.review_date = "01/01/2025"  # Incorrect format
       self.assertTrue("Incorrect data format" in str(context.exception))

   def test_employee_invalid_review_rating(self):
       """Test that setting an out-of-range rating raises a ValueError."""
       employee = Employee()

       with self.assertRaises(ValueError) as context:
           employee.review_rating = 10  # Out of range (1-5)
       self.assertTrue("choose only values 1 through 5" in str(context.exception))