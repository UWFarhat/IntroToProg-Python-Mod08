# ------------------------------------------------- #
# Title: Presentation Classes Unit Tests
# Description: Contains unit tests for the classes in presentation_classes.py.
# ChangeLog: (Who, When, What)
# mofarhat, 3/8/2026, Created Script
# ------------------------------------------------- #

import unittest
from unittest.mock import patch, MagicMock, ANY
from presentation_classes import IO
import data_classes as data

class TestIO(unittest.TestCase):
    @patch('builtins.print')
    def test_output_error_messages(self, mock_print: MagicMock):
       # tests the display of a custom error messages to the user
       IO.output_error_messages("That value is not the correct type of data!", ValueError())
       mock_print.assert_any_call("That value is not the correct type of data!", end="\n\n")

    @patch('builtins.print')
    def test_output_menu(self, mock_print: MagicMock):
        #tests the display of the main menu
        menu: str = '''
        ---- Employee Ratings ------------------------------
          Select from the following menu:
            1. Show current employee rating data.
            2. Enter new employee rating data.
            3. Save data to a file.
            4. Exit the program.
        --------------------------------------------------
        '''
        IO.output_menu(menu)
        mock_print.assert_any_call(menu)

    @patch('builtins.input', side_effect=["6", "2"])
    @patch('presentation_classes.IO.output_error_messages')
    def test_input_menu_choice(self, mock_error, mock_input: MagicMock):
       # Act
        choice = IO.input_menu_choice()

       # Assert if a wrong input was captured
        mock_error.assert_called_with("Please, choose only 1, 2, 3, or 4")

        # Assert that the correct choice was returned
        self.assertEqual(choice, "2")

        # Assert the test ran twice
        self.assertEqual(mock_input.call_count, 2)

    @patch('builtins.print')
    def test_output_employee_data(self, mock_print: MagicMock):
        #tests the display of employee data as expected
        mock_employee = MagicMock()
        mock_employee.first_name = "John"
        mock_employee.last_name = "Johnson"
        mock_employee.review_date = "2026-03-08"
        mock_employee.review_rating = 5

        IO.output_employee_data([mock_employee])
        mock_print.assert_any_call("John Johnson rated on 2026-03-08 as 5 (Leading)")

    @patch('presentation_classes.IO.output_error_messages')
    @patch('builtins.input', side_effect=["John", "Johnson", "2026-03-08", 5])
    def test_input_employee_data_valid(self, mock_input, mock_error):
        # Arrange
        mock_employee_data = []

        # Act
        IO.input_employee_data(mock_employee_data, data.Employee)

        # Assert that input() was called 4 times (4 items per call x 1 calls)
        self.assertEqual(mock_input.call_count, 4)

        # Assert
        self.assertEqual(len(mock_employee_data), 1)
        self.assertEqual(mock_employee_data[0].first_name, "John")
        self.assertEqual(mock_employee_data[0].last_name, "Johnson")
        self.assertEqual(mock_employee_data[0].review_date, "2026-03-08")
        self.assertEqual(mock_employee_data[0].review_rating, 5)
        self.assertEqual(mock_error.call_count, 0)  # 0 for success

    @patch('presentation_classes.IO.output_error_messages')
    @patch('builtins.input', side_effect=["John", "Johnson", "20-03-2008",
                                          "John", "Johnson", "2026-03-08", "Excellent",
                                          "J0hn",
                                          "John", "J0hnson", "2026-03-08", "Leading"])
    def test_input_employee_data_invalid(self, mock_input: MagicMock, mock_error):
        #Test that employee date input is handled correct and captures errors.

        #Arrange
        mock_employee_data = []

        #Act
        IO.input_employee_data(mock_employee_data, data.Employee) #Error on date
        IO.input_employee_data(mock_employee_data, data.Employee) #Error on rating
        IO.input_employee_data(mock_employee_data, data.Employee) #Error on name
        IO.input_employee_data(mock_employee_data, data.Employee) #Error on name

        #Assert if ValueError was captured
        mock_error.assert_any_call("That value is not the correct type of data!", ANY)

        # Assert that input() was called 10 times (3 + 4 + 1 + 2)
        self.assertEqual(mock_input.call_count, 10)

        #Assert that no data was captured
        self.assertEqual(len(mock_employee_data), 0)

if __name__ == '__main__':
    unittest.main()