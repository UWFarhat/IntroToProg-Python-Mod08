# ------------------------------------------------- #
# Title: Processing Classes Unit Tests
# Description: Contains unit tests for the classes in processing_classes.py.
# ChangeLog: (Who, When, What)
# mofarhat, 3/8/2026, Created Script
# ------------------------------------------------- #

import unittest
import tempfile
import json
import os
from processing_classes import FileProcessor

class ExampleEmployee:
    def __init__(self, first_name="", last_name="", review_date="", review_rating=3):
        self.first_name = first_name
        self.last_name = last_name
        self.review_date = review_date
        self.review_rating = review_rating

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []

    def tearDown(self):
        # Close up and delete the temporary file
        self.temp_file.close()
        if os.path.exists(self.temp_file_name): #Needed to work around Windows requirement for delete=False
            os.remove(self.temp_file_name)

    def test_read_employee_data_from_file(self):
        # Create some sample data and write it to the temporary file
        sample_data = [
            {"FirstName": "John", "LastName": "Doe", "ReviewDate": "2025-01-01", "ReviewRating": 3},
            {"FirstName": "Alice", "LastName": "Smith", "ReviewDate": "2025-01-01", "ReviewRating": 5},
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_data_from_file method and check if it returns the expected data
        FileProcessor.read_employee_data_from_file(self.temp_file_name, self.employee_data, ExampleEmployee)

        # Assert that the employee_data list contains the expected employee objects
        self.assertEqual(len(self.employee_data), len(sample_data))
        self.assertEqual(self.employee_data[0].first_name, "John")
        self.assertEqual(self.employee_data[1].review_rating, 5)

    def test_write_employee_data_to_file(self):
        sample_employees = [
            ExampleEmployee("John", "Doe", "2025-01-01", 3),
            ExampleEmployee("Alice", "Smith", "2025-01-01", 5),
        ]
        FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_employees)

        with open(self.temp_file_name, "r") as file:
            data = json.load(file)
        self.assertEqual(data[1]["FirstName"], "Alice")

    def test_read_data_file_not_found(self):
        with self.assertRaises(FileNotFoundError) as context:
            FileProcessor.read_employee_data_from_file("missing.json", [], ExampleEmployee)
        self.assertEqual(str(context.exception), "Text file must exist before running this script!")

    def test_write_data_type_error(self):
        # We pass an integer instead of a list so 'for employee in employee_data' fails with a TypeError
        invalid_data = 12345

        with self.assertRaises(TypeError) as context:
            FileProcessor.write_employee_data_to_file(self.temp_file_name, invalid_data)

        self.assertEqual(str(context.exception), "Please check that the data is a valid JSON format")

if __name__ == "__main__":
    unittest.main()


