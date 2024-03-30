"""
State Data
==========
Python command line menu-driven application
that allows a user to display, sort and update, as needed 
a List of U.S states containing the state capital, 
overall state population, and state flower.
The Internet provides multiple references with these lists. For example:
    https://www.crestcapital.com/tax/us_states_and_capitals
    https://statesymbolsusa.org/categories/flower
    https://worldpopulationreview.com/states/state-capitals/
You will need to embed the State data into your Python code 
in a data structure of your choice, from the readings this week.

The user interface will allow the user to perform the following functions:
    1. Display all U.S. States in Alphabetical order along with the
    Capital, State Population, and Flower
    2. Search for a specific state and display the appropriate Capital
    name, State Population, and an image of the associated State Flower.
    3. Provide a Bar graph of the top 5 populated States showing their
    overall population.
    4. Update the overall state population for a specific state.
    5. Exit the program

As before, generate an appropriate Welcome, prompt, 
and exit messages to help the user navigate the program.
The program should continue to allow selections until the program is exited.
If a state is not found an appropriate message should be displayed.

Hints:
    1. Use the List data structure and associated sort() and searching capabilities
    2. Create and use functions as often as possible.
    3. Validate input data to ensure each entry from the user is correct before proceeding.
    4. Prompt the user to reenter information as needed.
    5. The following Python sites are excellent resources 
    for learning more about the Python libraries mentioned in the readings 
    that you should use as part of this exercise.
        a. https://matplotlib.org/tutorials/introductory/pyplot.html
        b. https://matplotlib.org/tutorials/introductory/
            images.html#sphx-glr-tutorials-introductory-images-py
    6. Use comments to document your code
    7. Test with many combinations.
    8. Use pylint to verify the code style – the goal is a 10!
    9. Before you import a third part library (e.g. matplotlib) )you must install it.
        To install a Third Party library, you use this command at the command prompt:
        python -m pip install -U matplotlib

Author
------
Terrence Jackson

Last Modified
-------------
3.30.24

Class
-----
UMGC SDEV 300
"""

from pathlib import Path
from typing import Union

import matplotlib.pyplot as plt
from matplotlib.image import imread

# A list of global variables to be used in processing State data
FULL_NAME = "Full Name"
CAPITAL = "Capital"
FLOWER = "Flower"
POPULATION = "Population"
STATES = {
    "AK": {
        FULL_NAME: "Alaska",
        CAPITAL: "Juneau",
        FLOWER: "Forget-me-not",
        POPULATION: 31168,
    },
    "AZ": {
        FULL_NAME: "Arizona",
        CAPITAL: "Phoenix",
        FLOWER: "Saguaro Cactus Blossom",
        POPULATION: 1676481,
    },
    "AR": {
        FULL_NAME: "Arkansas",
        CAPITAL: "Little Rock",
        FLOWER: "Apple Blossom",
        POPULATION: 203106,
    },
    "CA": {
        FULL_NAME: "California",
        CAPITAL: "Sacramento",
        FLOWER: "California Poppy",
        POPULATION: 530334,
    },
    "CO": {
        FULL_NAME: "Colorado",
        CAPITAL: "Denver",
        FLOWER: "Rocky Mountain Columbine",
        POPULATION: 708948,
    },
    "CT": {
        FULL_NAME: "Connecticut",
        CAPITAL: "Hartford",
        FLOWER: "Mountain Laurel",
        POPULATION: 120734,
    },
    "DE": {
        FULL_NAME: "Delaware",
        CAPITAL: "Dover",
        FLOWER: "Peach Blossom",
        POPULATION: 37811,
    },
    "FL": {
        FULL_NAME: "Florida",
        CAPITAL: "Tallahassee",
        FLOWER: "Orange Blossom",
        POPULATION: 205536,
    },
    "GA": {
        FULL_NAME: "Georgia",
        CAPITAL: "Atlanta",
        FLOWER: "Cherokee Rose",
        POPULATION: 498386,
    },
    "HI": {
        FULL_NAME: "Hawaii",
        CAPITAL: "Honolulu",
        FLOWER: "Hibiscus",
        POPULATION: 349913,
    },
    "ID": {
        FULL_NAME: "Idaho",
        CAPITAL: "Boise",
        FLOWER: "Syringa",
        POPULATION: 237250,
    },
    "IL": {
        FULL_NAME: "Illinois",
        CAPITAL: "Springfield",
        FLOWER: "Violet",
        POPULATION: 112282,
    },
    "IN": {
        FULL_NAME: "Indiana",
        CAPITAL: "Indianapolis",
        FLOWER: "Peony",
        POPULATION: 874089,
    },
    "IA": {
        FULL_NAME: "Iowa",
        CAPITAL: "Des Moines",
        FLOWER: "Wild Rose",
        POPULATION: 208254,
    },
    "KS": {
        FULL_NAME: "Kansas",
        CAPITAL: "Topeka",
        FLOWER: "Sunflower",
        POPULATION: 124479,
    },
    "KY": {
        FULL_NAME: "Kentucky",
        CAPITAL: "Frankfort",
        FLOWER: "Goldenrod",
        POPULATION: 28172,
    },
    "LA": {
        FULL_NAME: "Louisiana",
        CAPITAL: "Baton Rouge",
        FLOWER: "Louisiana Iris",
        POPULATION: 216641,
    },
    "ME": {
        FULL_NAME: "Maine",
        CAPITAL: "Augusta",
        FLOWER: "White Pine",
        POPULATION: 19220,
    },
    "MD": {
        FULL_NAME: "Maryland",
        CAPITAL: "Annapolis",
        FLOWER: "Black-eyed Susan",
        POPULATION: 40425,
    },
    "MA": {
        FULL_NAME: "Massachusetts",
        CAPITAL: "Boston",
        FLOWER: "Mayflower",
        POPULATION: 629842,
    },
    "MI": {
        FULL_NAME: "Michigan",
        CAPITAL: "Lansing",
        FLOWER: "Dwarf Lake Iris",
        POPULATION: 112520,
    },
    "MN": {
        FULL_NAME: "Minnesota",
        CAPITAL: "St. Paul",
        FLOWER: "Pink and White Lady's Slipper",
        POPULATION: 295222,
    },
    "MS": {
        FULL_NAME: "Mississippi",
        CAPITAL: "Jackson",
        FLOWER: "Magnolia",
        POPULATION: 138998,
    },
    "MO": {
        FULL_NAME: "Missouri",
        CAPITAL: "Jefferson City",
        FLOWER: "Hawthorn",
        POPULATION: 42541,
    },
    "MT": {
        FULL_NAME: "Montana",
        CAPITAL: "Helena",
        FLOWER: "Bitterroot",
        POPULATION: 35540,
    },
    "NE": {
        FULL_NAME: "Nebraska",
        CAPITAL: "Lincoln",
        FLOWER: "Goldenrod",
        POPULATION: 293678,
    },
    "NV": {
        FULL_NAME: "Nevada",
        CAPITAL: "Carson City",
        FLOWER: "Sagebrush",
        POPULATION: 57577,
    },
    "NH": {
        FULL_NAME: "New Hampshire",
        CAPITAL: "Concord",
        FLOWER: "Purple Lilac",
        POPULATION: 44964,
    },
    "NJ": {
        FULL_NAME: "New Jersey",
        CAPITAL: "Trenton",
        FLOWER: "Purple Violet",
        POPULATION: 88744,
    },
    "NM": {
        FULL_NAME: "New Mexico",
        CAPITAL: "Santa Fe",
        FLOWER: "Yucca",
        POPULATION: 90292,
    },
    "NY": {
        FULL_NAME: "New York",
        CAPITAL: "Albany",
        FLOWER: "Rose",
        POPULATION: 102988,
    },
    "NC": {
        FULL_NAME: "North Carolina",
        CAPITAL: "Raleigh",
        FLOWER: "Dogwood",
        POPULATION: 488854,
    },
    "ND": {
        FULL_NAME: "North Dakota",
        CAPITAL: "Bismarck",
        FLOWER: "Wild Prairie Rose",
        POPULATION: 75153,
    },
    "OH": {
        FULL_NAME: "Ohio",
        CAPITAL: "Columbus",
        FLOWER: "Scarlet Carnation",
        POPULATION: 909676,
    },
    "OK": {
        FULL_NAME: "Oklahoma",
        CAPITAL: "Oklahoma City",
        FLOWER: "Oklahoma Rose",
        POPULATION: 706576,
    },
    "OR": {
        FULL_NAME: "Oregon",
        CAPITAL: "Salem",
        FLOWER: "Oregon Grape",
        POPULATION: 179043,
    },
    "PA": {
        FULL_NAME: "Pennsylvania",
        CAPITAL: "Harrisburg",
        FLOWER: "Penngift Crownvetch",
        POPULATION: 50274,
    },
    "RI": {
        FULL_NAME: "Rhode Island",
        CAPITAL: "Providence",
        FLOWER: "Violet",
        POPULATION: 188398,
    },
    "SC": {
        FULL_NAME: "South Carolina",
        CAPITAL: "Columbia",
        FLOWER: "Yellow Jessamine",
        POPULATION: 143210,
    },
    "SD": {
        FULL_NAME: "South Dakota",
        CAPITAL: "Pierre",
        FLOWER: "Pasque Flower",
        POPULATION: 13878,
    },
    "TN": {
        FULL_NAME: "Tennessee",
        CAPITAL: "Nashville",
        FLOWER: "Iris",
        POPULATION: 677519,
    },
    "TX": {
        FULL_NAME: "Texas",
        CAPITAL: "Austin",
        FLOWER: "Bluebonnet",
        POPULATION: 983126,
    },
    "UT": {
        FULL_NAME: "Utah",
        CAPITAL: "Salt Lake City",
        FLOWER: "Sego Lily",
        POPULATION: 208656,
    },
    "VT": {
        FULL_NAME: "Vermont",
        CAPITAL: "Montpelier",
        FLOWER: "Red Clover",
        POPULATION: 7979,
    },
    "VA": {
        FULL_NAME: "Virginia",
        CAPITAL: "Richmond",
        FLOWER: "American Dogwood",
        POPULATION: 231782,
    },
    "WA": {
        FULL_NAME: "Washington",
        CAPITAL: "Olympia",
        FLOWER: "Western Rhododendron",
        POPULATION: 55731,
    },
    "WV": {
        FULL_NAME: "West Virginia",
        CAPITAL: "Charleston",
        FLOWER: "Rhododendron",
        POPULATION: 45616,
    },
    "WI": {
        FULL_NAME: "Wisconsin",
        CAPITAL: "Madison",
        FLOWER: "Wood Violet",
        POPULATION: 275493,
    },
    "WY": {
        FULL_NAME: "Wyoming",
        CAPITAL: "Cheyenne",
        FLOWER: "Indian Paintbrush",
        POPULATION: 64000,
    },
    "AL": {
        FULL_NAME: "Alabama",
        CAPITAL: "Montgomery",
        FLOWER: "Camellia",
        POPULATION: 193948,
    },
}


def print_menu() -> None:
    """Prints out the menu of options for the user"""
    print("\nMenu:")
    print("a. Display all states.")
    print("b. Search for state.")
    print("c. Graph 5 most populous states.")
    print("d. Update state population.")
    print("e. Exit program")


def print_state(state: dict[str]):
    """Prints out state data in a nice string"""
    for key, value in state.items():
        if key == FULL_NAME:
            print(f"===={value}====")
        else:
            print(f"{key}: {value}")
    print()


def display_state_flower(state: dict[str]):
    """Uses matplotlib to display a picture of the state flower"""
    project_folder = Path(__file__).parent
    image_path = project_folder / "Flowers" / f"{state[FLOWER]}.jpg"

    img = imread(image_path)
    plt.imshow(img)
    plt.axis("off")
    plt.title(f"{state[FULL_NAME]} Flower: {state[FLOWER]}")
    plt.show()


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
    Returns valid integer input or None when not valid
    """
    try:
        integer = integer.replace(",", "")  # remove any commas
        integer = int(integer)
        if integer < 1:
            # not valid to have a 0 or negative population
            raise ValueError
        return integer
    except ValueError:
        # not an int value
        print("Invalid, please input an integer number greater than 0.")
        return None


def validate_state(input_str: str) -> str | None:
    """Returns state abbreviation string when valid, None when invalid"""
    input_str = input_str.upper()  # match uppercase abbreviation data
    for state_abbreviation, state_data in STATES.items():
        # manipulate full name data to match input
        full_name: str = state_data[FULL_NAME]
        # remove spaces to help with uniformity
        full_name = full_name.upper().replace(" ", "")

        # if input matches abbreviation or full name
        if input_str == state_abbreviation or input_str.replace(" ", "") == full_name:
            return state_abbreviation

    # not valid
    print("Invalid, please input a valid state.")
    return None


def get_state_data(state_abbreviation: str) -> dict[str]:
    """Returns state data dictionary"""
    return STATES[state_abbreviation]


def set_state(new_data: dict[str]) -> dict[str]:
    """Updates dictionary with new state data"""
    for state_abbreviation, state_data in STATES.items():
        # find the state where the full name field matches
        if state_data[FULL_NAME] == new_data[FULL_NAME]:
            # update the dictionary entry
            STATES[state_abbreviation] = new_data
            # get the new state data
            state = get_state_data(state_abbreviation)
            break
    return state


def display_all_states():
    """Loops through all states and prints out their data"""
    # get a sorted list of states
    alphabetized_states = sorted(STATES.values(), key=lambda x: x[FULL_NAME])

    # for each state in sorted order, get and print data
    for state_data in alphabetized_states:
        print_state(state_data)


def graph_populous_states():
    """Display a graph of the top 5 most populous states"""
    sorted_states = sorted(STATES.values(), key=lambda x: x[POPULATION], reverse=True)
    top_5_states = sorted_states[:5]
    names = [state[FULL_NAME] for state in top_5_states]
    pop = [state[POPULATION] for state in top_5_states]

    # generate graph
    plt.bar(names, pop)
    plt.xlabel("State")
    plt.ylabel("Population")
    plt.title("Top 5 Most Populous States")
    plt.show()


def update_state_population(state: dict[str], population: int):
    """Finds the state in the data dictionary and updates its population entry"""
    state[POPULATION] = population
    state = set_state(state)
    print_state(state)


def main():
    """Driver function"""
    # init prompt
    print("Welcome to the state data program!")
    print_menu()
    user_choice = input("Enter your choice: ").strip().lower()

    # continue processing as long as user doesn't select e to quit
    while user_choice != "e":
        if user_choice == "a":
            display_all_states()
        elif user_choice == "b":
            state = get_input("Enter state: ", validate=validate_state)
            state = get_state_data(state)
            print_state(state)
            display_state_flower(state)
        elif user_choice == "c":
            graph_populous_states()
        elif user_choice == "d":
            state = get_input("Enter state: ", validate=validate_state)
            state = get_state_data(state)
            population = get_input("Enter new population: ", validate=validate_int)
            update_state_population(state, population)
        else:
            print("Invalid choice. Please enter a valid option.")

        # prompt for choice again
        print_menu()
        user_choice = input("Enter your choice: ").strip().lower()

    # close out with a thank you
    print("Thank you for using the program. Goodbye!")


if __name__ == "__main__":
    main()
