class CustomException(Exception):
    def __init__(self, message="This is a custom exception."):
        self.message = message
        super().__init__(self.message)

def check_condition(value):
    if value < 0:
        raise CustomException("Value should be a non-negative integer.")

# Example usage:
try:
    user_input = int(input("Enter a non-negative integer: "))
    check_condition(user_input)
    print(f"The entered value is: {user_input}")
except CustomException as ce:
    print(f"Custom Exception: {ce}")
except ValueError:
    print("Error: Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
