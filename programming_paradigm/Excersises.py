import unittest

class Divide():
    """  program that takes two numbers as input from the user and divides the first number by the second number. """
    def __init__(self):
        self.num1 = float(input("Enter First Number: "))
        self.num2 = float(input("Enter Second Number: "))
        
    def divsion(self):
        try:
            self.result = self.num1 / self.num2
        except ZeroDivisionError as e:
            print(e)
        else:
            print(f"{self.num1} / {self.num2} = {self.result}")
        finally:
            print("Thanks for using the program.")
        
# use = Divide()
# result = use.divsion()

############################################

class ReadFile():
    """  program that attempts to open and read data from a file specified by the user. """
    def __init__(self):
        self.file_name = str(input("Enter file name: "))
               
    def read(self):
        try:
            file = open(self.file_name)
        except FileNotFoundError as e:
            print(e)
        else:
            text = file.read()
            print(f"{text}")
            file.close()
            
        finally:
            print("Thanks for using the program.")
        
# use = ReadFile()
# result = use.read()

############################################

class ValueTooHighError(Exception):
    """  a custom exception class called ValueTooHighError that handle error results from entering values greater than 100. """
    def __init__(self, number):
        self.check_number = number
        
    def __str__(self):
        return f"Sorry the value {self.check_number} is greater than 100."

class SmallerThan100():
    
    def __init__(self):
        self.number = int(input("Enter number: "))
        
    def check_value(self):
        try:
            if self.number > 100:
                raise ValueTooHighError(self.number)
            else:
                print(f"{self.number} is smaller than 100.")
        except ValueTooHighError as e:
            print(e)  # Catch the custom exception and print its message.
        finally:
            print("Thanks for using the program.")
            
        
# use = SmallerThan100()
# result = use.check_value()

############################################

def calculate_square_number(number):
    result = number ** 2
    return result

class TestCalculateSquareNumber(unittest.TestCase):
    def test_valid_input(self):
        test_result = calculate_square_number(3)
        self.assertEqual(test_result, 9)
    
        
unittest.main()


