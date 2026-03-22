# ------------------------------------------------- #
# Title: Presentation Classes Module
# Description: A collection of classes for presenting data and handling I/O (IO).
# ChangeLog: (Who, When, What)
# mofarhat, 3/8/2026, Created module
# ------------------------------------------------- #

try:
    if __name__ == "__main__":
        raise Exception("Please use the main.py file to start this application.")
    else:
        import json
        import data_classes as data
except Exception as e:
    print(e.__str__())


MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

class IO:
    """
    A collection of presentation layer methods that manage user input and output

    ChangeLog: (Who, When, What)
    mofarhat, 3/8/2026, Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This method displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        mofarhat, 3/8/2026, Created method

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu(menu: str):
        """ This method displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        mofarhat, 3/8/2026, Created method

        :return: None
        """
        print()
        print(menu)
        print()


    @staticmethod
    def input_menu_choice():
        """ This method gets a menu choice from the user

        ChangeLog: (Who, When, What)
        mofarhat, 3/8/2026, Created method

        :return: string with the users choice
        """
        choice = "0"
        while True:
            try:
                choice = input("Enter your menu choice number: ")
                if choice not in ("1", "2", "3", "4"):  # Note these are strings
                    raise Exception("Please, choose only 1, 2, 3, or 4")
                return choice
            except Exception as e:
                IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message



    @staticmethod
    def output_employee_data(employee_data: list):
        """ This method displays employee data to the user

        ChangeLog: (Who, When, What)
        mofarhat, 3/8/2026, Created method

        :param employee_data: list of employee object data to be displayed

        :return: None
        """

        # Map ratings to descriptions
        ratings = {
            5: "Leading",
            4: "Strong",
            3: "Solid",
            2: "Building",
            1: "Not Meeting Expectations"
        }

        print()
        print("-" * 50)
        for employee in employee_data:
            description = ratings.get(employee.review_rating, "Unknown")
            print(f"{employee.first_name} {employee.last_name} "
                f"rated on {employee.review_date} "
                f"as {employee.review_rating} ({description})")
        print("-" * 50)
        print()

    @staticmethod
    def input_employee_data(employee_data: list, employee_type: object):
        """ This method gets the first name, last name, review date and review rating from the user

        ChangeLog: (Who, When, What)
        mofarhat, 3/8/2026, Created method

        :param employee_data: objects to be filled with input data

        :return: list
        """

        try:
            # Input the data
            employee_object = employee_type()
            employee_object.first_name = input("What is the employee's first name? ")
            employee_object.last_name = input("What is the employee's last name? ")
            employee_object.review_date = input("What is their review date as YYYY-MM-DD? ")
            employee_object.review_rating = int(input("What is their review rating? "))
            employee_data.append(employee_object)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data