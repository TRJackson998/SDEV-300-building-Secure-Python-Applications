"""
Lab 1: Python Start
===================
Using your Python programming environment,
write a Python application that supports voter registration.

Author: Terrence Jackson
Date: 3.13.24
Class:  UMGC SDEV 300

Requirements
------------
The application will launch and run from the command line prompt.

The application will prompt the user for their first name, last name, age, 
country of citizenship, state of residence and zipcode.

To be a valid registration all fields must be entered.

If they are at least 18 years old and a U.S citizen, 
they can move forward and be prompted for the remaining questions and register to vote.

If not, they should not be presented with the additional questions.

There should be some error checking logic on the input statements 
to make sure the age numbers entered seem reasonable (e.g. a person is probably not > 120 years) 
and states should be 2 letters representing only valid U.S. States.

The application should prompt the user for the needed questions to complete the registration 
and re-prompt when data is invalid giving the user the opportunity to retry.

The output should summarize the input data and congratulate the user if they are eligible 
to vote and entered all of the data.

The user should be given options to exit the program at any time to cancel the registration process.
"""

import sys


def close_down(reason: str):
    """Close program after printing out reason"""
    print(reason)
    print("Goodbye!")
    sys.exit()


def get_input(prompt: str, validate=None) -> str:
    """
    Display prompt and read in input
    If user inputs 'q', close down program
    If validator function was passed in, validate input
    Continue prompting until valid input or quit
    """
    # get initial input
    user_input = input(prompt)

    # keep going as long as not quit
    while user_input.lower() != "q":
        # either no validator function or passed validation
        if not validate or validate(user_input):
            return user_input

        # invalid, prompt again
        user_input = input(prompt)

    # user input quit, shut down
    close_down("User chose to quit.")

    # return empty str, shouldn't ever get here
    return ""


def validate_name(name: str) -> bool:
    """Returns T/F whether name is at least one alphabet"""
    # confirm name is all alphabetic characters, at least one character
    if name.isalpha():
        return True

    # invalid
    print("Invalid, please only input alphabetic characters")
    return False


def validate_age(age: str) -> bool:
    """
    Returns T/F whether age is an integer between 1 and 120
    0 is invalid, 120 is valid
    """
    try:
        age = int(age)

        # validate age range
        if 0 < age <= 120:
            return True

        # not a valid age
        print("Invalid, please input a number between 1 and 120.")
        return False

    except ValueError:
        # not an int value
        print("Invalid, please input a number.")
        return False


def validate_state(state: str) -> bool:
    """Returns T/F whether state is in the list of real states"""
    valid_states = [
        "AL",
        "AK",
        "AZ",
        "AR",
        "CA",
        "CO",
        "CT",
        "DE",
        "FL",
        "GA",
        "HI",
        "ID",
        "IL",
        "IN",
        "IA",
        "KS",
        "KY",
        "LA",
        "ME",
        "MD",
        "MA",
        "MI",
        "MN",
        "MS",
        "MO",
        "MT",
        "NE",
        "NV",
        "NH",
        "NJ",
        "NM",
        "NY",
        "NC",
        "ND",
        "OH",
        "OK",
        "OR",
        "PA",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VT",
        "VA",
        "WA",
        "WV",
        "WI",
        "WY",
    ]

    # confirm state is in the list
    if state.upper() in valid_states:
        return True

    # not a valid state
    print("Invalid, please input a two letter state code.")
    return False


def validate_yn(input_str: str) -> bool:
    """Returns T/F whether user input an understandable yes or no"""
    # confirm input
    if input_str.lower() in ["yes", "no", "y", "n"]:
        return True

    # not valid, not able to parse as yes/no
    print("Invalid, please input 'yes' or 'no.")
    return False


def validate_zipcode(zipcode: str):
    """Returns T/F whether zipcode is 5 digits"""
    # check it's 5 characters long and all digits
    if len(zipcode) == 5 and zipcode.isdigit():
        return True

    # not a valid zipcode
    print("Invalid, please enter a 5-digit numeric zipcode.")
    return False


def print_usa_flag():
    """Print a USA flag design using * and -"""
    for i in range(7):  # rows
        for j in range(12):  # cols
            if i < 4 and j < 5:
                print("*  ", end=" ")
            else:
                print("-  ", end=" ")
        print()


def main():
    """Driver function"""
    print_usa_flag()
    print("Welcome to the Voter Registration Application!\n")
    print("Enter 'q' at any time to quit.\n")

    # prompt for names
    fname = get_input("First name: ", validate_name)
    lname = get_input("Last name: ", validate_name)

    # prompt for age
    age = get_input("Age: ", validate_age)
    if int(age) < 18:  # validator ensures age is an int
        close_down("Sorry, you must be at least 18 years old to register to vote.")

    # prompt for US citizenship
    country = get_input("Are you a U.S. citizen? (yes/no): ", validate_yn)
    if "y" not in country.lower():
        close_down("Sorry, only U.S. citizens are eligible to register to vote.")

    # prompt for other address info
    state = get_input("State: ", validate_state)
    zipcode = get_input("Zip code: ", validate_zipcode)

    # print out result
    print("\nCongratulations! You are eligible to vote.")
    print_usa_flag()
    print("Voter Registration Summary:")
    print(f"Name: {fname} {lname}")
    print(f"Age: {age}")
    print("Country of Citizenship: U.S.")
    print(f"State of Residence: {state}")
    print(f"Zipcode: {zipcode}")


if __name__ == "__main__":
    main()
