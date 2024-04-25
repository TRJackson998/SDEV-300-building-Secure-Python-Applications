"""
Matrix App
==========
allows a user to enter and validate their phone number and zipcode+4. Then the user
will enter values of two, 3x3 matrices and then select from options including, addition, 
subtraction, matrix multiplication, and element by element multiplication. 
You should use numpy.matmul() for matrix multiplication (e.g. np.matmul(a, b) ). 
The program should compute the appropriate results and return the results, 
the transpose of the results, the mean of the rows for the results, and the
mean of the columns for the results.
When entering data, the application should use regular expressions and/or Pandas functionality to
check the format of the phone number and zipcode. 
You should check that each value is numeric for the matrices.
The user interface should continue to run until the user indicates they are ready to exit.

Author
------
Terrence Jackson

Last Modified
-------------
4.9.24

Class
-----
UMGC SDEV 300
"""

import re
from typing import Union

import numpy


def get_input(prompt: str, validate=None) -> Union[str, int, float, bool]:
    """
    Display prompt and read in input
    If validator function was passed in, validate input
    Continue prompting until valid input
    """
    # get initial input
    user_input = input(prompt)

    # keep going until valid input returned
    while True:
        # no validator function
        if not validate:
            return user_input

        # passes validation?
        validated_input = validate(user_input)
        if validated_input is not None:
            return validated_input

        # invalid, prompt again
        user_input = input(prompt)


def get_matrix_input(prompt: str) -> numpy.ndarray:
    """
    Display prompt and read in input
    Validate that it is a 3x3 matrix
    """
    print(prompt)
    row_map = {}

    try:
        for i in range(3):
            element_1, element_2, element_3 = input().strip().split(" ")
            row_map[i] = [float(element_1), float(element_2), float(element_3)]

    except ValueError:
        print(
            "Invalid input. "
            "Please input a matrix using only integers and floats in the following format:"
        )
        print("  X X X")
        print("  X X X")
        print("  X X X")
        return get_matrix_input(prompt)

    matrix = numpy.array([row_map[0], row_map[1], row_map[2]])
    return matrix


def validate_yn(input_str: str) -> bool | None:
    """Returns T/F whether user input an understandable yes or no"""
    # confirm input
    if input_str.lower() in ["yes", "y"]:
        return True

    if input_str.lower() in ["no", "n"]:
        return False

    # not valid, not able to parse as yes/no
    print("Invalid, please input 'yes' or 'no'.")
    return None


def validate_phone_number(input_str: str) -> str | None:
    """Validate phone number using regex and return it if valid"""
    regex = re.compile(r"(\d{3}-){2}\d{4}")
    if re.fullmatch(regex, input_str):
        return input_str

    # not valid, not able to parse as phone number
    print("Invalid, please input a phone number in the format XXX-XXX-XXXX")
    return None


def validate_zip_code(input_str: str) -> str | None:
    """Validate zip using regex and return it if valid"""
    regex = re.compile(r"\d{5}-\d{4}")
    if re.fullmatch(regex, input_str):
        return input_str

    # not valid, not able to parse as zip code
    print("Invalid, please input a phone number in the format XXX-XXX-XXXX")
    return None


def print_matrix(matrix: numpy.ndarray) -> None:
    """Prints out each value in the matrix with two decimal places in an 8 space width field"""
    for row in matrix:
        values = [f"{col:8.2f}" for col in row]
        print("".join(values))


def main():
    """Driver function"""
    # welcome message
    print("***************** Welcome to the Python Matrix Application***********")

    # init prompt
    play_the_game = get_input(
        "Do you want to play the Matrix Game?\nEnter Y for Yes or N for No: ",
        validate_yn,
    )

    # continue processing as long as user doesn't select N to quit
    while play_the_game:
        phone_number = get_input(
            "Enter your phone number (XXX-XXX-XXXX): ", validate_phone_number
        )
        print(f"Your phone number: {phone_number}")

        zip_code = get_input("Enter your zip code+4 (XXXXX-XXXX): ", validate_zip_code)
        print(f"Your zip code: {zip_code}")

        matrix_1 = get_matrix_input("Enter your first 3x3 matrix:")
        print("Your first 3x3 matrix is:")
        print_matrix(matrix_1)
        matrix_2 = get_matrix_input("Enter your second 3x3 matrix:")
        print("Your second 3x3 matrix is:")
        print_matrix(matrix_2)

        choice_map = {
            "a": ["Addition", numpy.add],
            "b": ["Subtraction", numpy.subtract],
            "c": ["Matrix Multiplication", numpy.matmul],
            "d": ["Element by element multiplication", numpy.multiply],
        }
        print("Select a Matrix Operation from the list below:")
        for key, value in choice_map.items():
            print(f"{key}. {value[0]}")

        user_choice = get_input("Choice: ").lower()
        while user_choice not in list(choice_map):
            print("Invalid choice. Please enter a valid option.")
            user_choice = get_input("Choice: ").lower()

        chosen_function = choice_map[user_choice][1]
        result_matrix = chosen_function(matrix_1, matrix_2)

        print(f"You selected {choice_map[user_choice][0]}. The results are:")
        print_matrix(result_matrix)
        print("The Transpose is:")
        print_matrix(numpy.transpose(result_matrix))
        print("The row and column mean values of the results are:")
        row_mean = numpy.mean(result_matrix, axis=1)
        col_mean = numpy.mean(result_matrix, axis=0)
        print(f"Row:    {"".join([f"{col:8.2f}" for col in row_mean])}")
        print(f"Column: {"".join([f"{col:8.2f}" for col in col_mean])}")

        # prompt for choice again
        play_the_game = get_input(
            "Do you want to play the Matrix Game?\nEnter Y for Yes or N for No: ",
            validate_yn,
        )

    # close out with a thank you
    print("*********** Thanks for playing the Python Matrix Game ***************")


if __name__ == "__main__":
    main()
