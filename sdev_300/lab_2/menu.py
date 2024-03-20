"""
Lab 2: Math and Secret Generation
===================
A command line menu-driven python application providing users with the
ability to perform several math and security related functions.

Author: Terrence Jackson
Date: 3.15.24
Class:  UMGC SDEV 300

Requirements
------------
Create a menu-driven python application with following menu options for users to
run at the command line:
    a. Generate Secure Password
    b. Calculate and Format a Percentage
    c. How many days from today until July 4, 2025?
    d. Use the Law of Cosines to calculate the leg of a triangle.
    e. Calculate the volume of a Right Circular Cylinder
    f. Exit program

1. Create functions to be called sending in the parameters the user enters.
2. Validate input data to ensure each entry from the user is correct before proceeding.
3. Prompt the user to reenter information as needed.
4. The following Python sites are excellent resources for learning more about the string,
datetime, secrets, math, and random number libraries mentioned in the readings that
you should use as part of this exercise.
    i. https://docs.python.org/3/library/random.html
    ii. https://docs.python.org/3/library/secrets.html
    iii. https://docs.python.org/3/library/string.html
    iv. https://docs.python.org/3/library/datetime.html
    v. https://docs.python.org/3/library/math.html
5. Use comments to document your code
6. Test with many combinations.
7. Use pylint to verify the code style – the goal is a 10!

Additional Guidance
-------------------
1. For the secure Password, you should prompt the user for the length of the password to be
created, as well as the complexity (i.e. Use of Upper Case, Use of Lower Case, Use of Numbers,
Use of special characters). Check out options from commercial password generators such as
Norton. (https://my.norton.com/extspa/passwordmanager?path=pwd-gen). Note in a command
line interface, the input and prompts are just text, so you won’t be creating a GUI, just the
functionality that allows the user to enter the information needed.

2. For the percentage, consider a simple example, where the user has to enter the numerator and
denominator and the number of decimal points for formatting. For example, 22, 57, 3 would
yield 38.596 percent.

3. For days until July 4, 2025 the output should just be the number of days. There would be no
input other than the selection from the menu

4. The formula for the law of cosines can be found at sites such as
https://www.mathsisfun.com/algebra/trig-cosine-law.html. You want to solve for c (lower case
c) in the following diagram.

5. The formula for a right cylinder can be found here:
https://www.mathsisfun.com/geometry/prism-vs-cylinder.html. Be sure to select right circular
cylinder.

6. When exiting the program be sure to thank the user for visiting your application.
"""

import secrets
import string
from datetime import date
from math import cos, pi, sqrt
from typing import Union


def print_menu() -> None:
    """Prints out the menu of options for the user"""
    print("\nMenu:")
    print("a. Generate Secure Password")
    print("b. Calculate and Format a Percentage")
    print("c. How many days from today until July 4, 2025?")
    print("d. Use the Law of Cosines to calculate the leg of a triangle.")
    print("e. Calculate the volume of a Right Circular Cylinder")
    print("f. Exit program")


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


def validate_int(integer: str) -> int | None:
    """
    Returns T/F whether input is an integer
    """
    try:
        integer = int(integer)
        if integer < 1:
            # all our calculations are on real lengths and angles,
            # no dividing by 0, can't have a 0 len password
            raise ValueError
        return integer
    except ValueError:
        # not an int value
        print("Invalid, please input a number greater than 0.")
        return None


def validate_float(floating_point: float) -> float | None:
    """
    Returns T/F whether input is a float
    """
    try:
        floating_point = float(floating_point)
        if floating_point <= 0:
            # all our calculations are on real lengths and angles,
            # no dividing by 0, can't have a 0 len password
            raise ValueError
        return floating_point
    except ValueError:
        # not a float value
        print("Invalid, please input a number greater than 0.")
        return None


def validate_yn(input_str: str) -> bool | None:
    """Returns T/F whether user input an understandable yes or no"""
    # confirm input
    if input_str.lower() in ["yes", "y"]:
        return True

    if input_str.lower() in ["no", "n"]:
        return False

    # not valid, not able to parse as yes/no
    print("Invalid, please input 'yes' or 'no.")
    return None


def generate_secure_password(
    length: int, letters: bool, upper_case: bool, punctuation: bool, numbers: bool
) -> str:
    """
    Uses the secrets library to generate a password
    args: letters, upper_case, punctuation, numbers are all yes/no strings
    returns generated password as a string
    """
    alphabet = ""
    if letters:
        # user chose to include letters
        if upper_case:
            # user chose to include all letters
            alphabet += string.ascii_letters
        else:
            # user chose not to include uppercase letters
            alphabet += string.ascii_lowercase
    if punctuation:
        # user chose to include punctuation
        alphabet += string.punctuation
    if numbers:
        # user chose to include digits
        alphabet += string.digits

    # generate password from alphabet
    password = "".join(secrets.choice(alphabet) for i in range(length))
    return password


def calculate_percentage(numerator: int, denominator: int, decimal_points: int) -> float:
    """
    Calculates a percentage given a numerator and denominator.
    Returns the percentage rounded to the given decimal place
    """
    percent = (numerator / denominator) * 100  # calculate percent
    return round(percent, decimal_points)  # round and return


def days_until_july_4_2025() -> int:
    """Returns the number of days between today and July 4th, 2025 as an integer"""
    july_4 = date(year=2025, month=7, day=4)
    today = date.today()

    return (july_4 - today).days


def law_of_cosines(a: float, b: float, angle_c: float) -> float:
    """
    Calculates side c given side a, side b, and angle c of a triangle
    c2 = a2 + b2 − 2ab cos(C)
    returns length of side c as a float
    """
    # generate all parts of the equation
    a2 = pow(a, 2)
    b2 = pow(b, 2)
    ab = a * b
    cos_c = cos(angle_c)

    # plug everything into equation
    c2 = a2 + b2 - (2 * ab * cos_c)

    # solve for c
    c = sqrt(c2)

    # return rounded result
    return round(c, 5)


def volume_of_cylinder(r: float, h: float) -> float:
    """
    Calculates volume given the radius and height of a cylinder
    (πr2) × h
    returns volume as a float
    """
    # generate r2
    r2 = pow(r, 2)

    # plug everything into equation
    volume = (pi * r2) * h

    # return rounded result
    return round(volume, 5)


def get_input_parameters(option: str) -> list[Union[str, int, float]]:
    """
    Prompts the user for input parameters based on the selected option
    Returns a list of validated input parameters
    """
    parameters = []

    if option == "a":
        # for generating secure password
        length = get_input("How long should it be? ", validate=validate_int)

        letters = get_input("Should it include letters? (yes/no): ", validate=validate_yn)
        if letters:
            upper_case = get_input("Should it include uppercase? (yes/no): ", validate=validate_yn)
        else:
            upper_case = False
        punctuation = get_input("Should it include punctuation? (yes/no): ", validate=validate_yn)
        numbers = get_input("Should it include numbers? (yes/no): ", validate=validate_yn)

        # validate at least one charset chosen
        if not letters and not punctuation and not numbers:
            print("No character set chosen, please choose at least one.")
            parameters = get_input_parameters("a")
        else:
            parameters.extend([length, letters, upper_case, punctuation, numbers])

    elif option == "b":
        # for calculating percentage
        numerator = get_input("Enter numerator: ", validate=validate_int)
        denominator = get_input("Enter denominator: ", validate=validate_int)
        decimal_points = get_input(
            "Enter number of decimal places to display: ", validate=validate_int
        )
        parameters.extend([numerator, denominator, decimal_points])

    elif option == "d":
        # for calculating the leg of a triangle using Law of Cosines
        side_a = get_input("Enter side_a: ", validate=validate_float)
        side_b = get_input("Enter side_b: ", validate=validate_float)
        angle = get_input("Enter the angle between the sides: ", validate=validate_float)
        parameters.extend([side_a, side_b, angle])

    elif option == "e":
        # for calculating the volume of a Right Circular Cylinder
        radius = get_input("Enter radius: ", validate=validate_float)
        height = get_input("Enter height: ", validate=validate_float)
        parameters.extend([radius, height])

    return parameters


def main() -> None:
    """Driver"""
    # init prompt
    print_menu()
    user_choice = input("Enter your choice: ").strip().lower()

    # dictionary to map user choice to corresponding function
    option_functions = {
        "a": generate_secure_password,
        "b": calculate_percentage,
        "c": days_until_july_4_2025,
        "d": law_of_cosines,
        "e": volume_of_cylinder,
    }

    # continue processing as long as user doesn't select f to quit
    while user_choice != "f":
        # get the function corresponding to the user's choice
        selected_function = option_functions.get(user_choice)

        if selected_function:
            # get input parameters for the selected function
            params = get_input_parameters(user_choice)
            # call the selected function with the input parameters
            result = selected_function(*params)
            print(result)
        else:
            print("Invalid choice. Please enter a valid option.")

        # prompt for choice again
        print_menu()
        user_choice = input("Enter your choice: ").strip().lower()

    # close out with a thank you
    print("Thank you for using the program. Goodbye!")


if __name__ == "__main__":
    main()
