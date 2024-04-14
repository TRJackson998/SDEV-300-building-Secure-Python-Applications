"""
Data Analysis
=============
This program allows a user to load one of two CSV files and then perform histogram analysis
and plots for select variables on the datasets. 
The first dataset represents the population change for specific dates for U.S. regions. 
The second dataset represents Housing data over an extended period of
time describing home age, number of bedrooms and other variables. The first row provides a column
name for each dataset. The following columns should be used to perform analysis:
PopChange.csv:
    Pop Apr 1
    Pop Jul 1
    Change Pop
Housing.csv:
    AGE
    BEDRMS
    BUILT
    ROOMS
    UTILITY

Notice for the Housing CSV file, 
there are more columns in the file than are required to be analyzed.
You can and should still load each column.
Specific statistics should include:
    Count
    Mean
    Standard Deviation
    Min
    Max
    Histogram

If an inappropriate entry is detected, 
the program should prompt for a correct value and continue to do
so until a correct value is entered.
Hints:
1. Use the Pandas, Numpy, MatplotLib and other Python modules when appropriate.
2. Be sure to install the required Python modules in your environment 
before you import or try to use them in your code.
For example, pip install each of the required modules that are external Python
libraries that you need.
3. If an inappropriate entry is detected, 
the program should prompt for a correct value and continue to
do so until a correct value is entered.
4. Use comments to document your code
5. Test with many combinations.
6. Use pylint to verify the code style – the goal is a 10!
7. The user Interface should continue to run until the user indicates they are ready to exit.
8. Be sure to review the previous readings and modules as you may need to use statistics and other
modules to complete this lab.


Author
------
Terrence Jackson

Last Modified
-------------
4.14.24

Class
-----
UMGC SDEV 300
"""

from pathlib import Path

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def print_file_menu() -> None:
    """Prints out the menu of file options for the user"""
    print("\nSelect the file you want to analyze:")
    print("1. Population Data")
    print("2. Housing Data")
    print("3. Exit the Program")


def print_col_menu(options: list[str]) -> None:
    """Prints out the menu of column options for the user"""
    print("\nSelect the Column you want to analyze:")
    i = 0
    for i, option in enumerate(options):
        print(f"{i}: {option}")
    print(f"{i+1}: Exit Column")


def get_input(int_range: list[int]) -> int:
    """
    Display prompt, read in input, validate input
    Continue prompting until valid input
    """
    # get initial input
    user_input = input("Enter your choice: ")

    # keep going until valid input returned
    while True:
        # passes validation?
        validated_input = validate_int(user_input, int_range)
        if validated_input is not None:
            return validated_input

        # invalid, prompt again
        user_input = input("Enter your choice: ")


def validate_int(integer: str, int_range: list[int]) -> int | None:
    """
    Returns T/F whether input is an integer
    """
    try:
        integer = int(integer)
        if integer not in int_range:
            # potential options passed in, must be one of them to be valid
            raise ValueError
        return integer
    except ValueError:
        # not an int value
        print("Invalid, please input a number in the presented options.")
        return None


def main():
    """Driver function"""
    # welcome message
    print("***************** Welcome to the Python Matrix Application***********")

    # init file prompt
    print_file_menu()
    file_choice = get_input(list(range(1, 4)))

    # continue processing as long as user doesn't select 3 to quit
    while file_choice != 3:
        # read file into df, get column options
        file = Path(__file__).parent
        if file_choice == 1:
            options = ["Pop Apr 1", "Pop Jul 1", "Change Pop"]
            df = pd.read_csv(file / "PopChange.csv")
        else:
            options = ["AGE", "BEDRMS", "BUILT", "ROOMS", "UTILITY"]
            df = pd.read_csv(file / "Housing.csv")

        # init column prompt
        print_col_menu(options)
        option_choice = get_input(list(range(0, len(options) + 1)))

        while option_choice != len(options):
            # print results to user
            print(f"You selected {options[option_choice]}")
            col_list = list(df[options[option_choice]])
            print(f"Count = {len(col_list)}")
            print(f"Mean = {(sum(col_list) / len(col_list)):.2f}")
            print(f"Standard Deviation = {np.std(col_list):.2f}")
            print(f"Min = {min(col_list)}")
            print(f"Max = {max(col_list)}")

            # show histogram
            plt.hist(col_list)
            plt.show()

            # prompt for column choice again
            print_col_menu(options)
            option_choice = get_input(list(range(0, len(options) + 1)))

        # prompt for file choice again
        print_file_menu()
        file_choice = get_input(list(range(1, 4)))

    # close out with a thank you
    print("*********** Thanks for using the Data Analysis App ***************")


if __name__ == "__main__":
    main()
