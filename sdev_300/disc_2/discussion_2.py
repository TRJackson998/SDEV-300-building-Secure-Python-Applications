"""
Discussion 2: SDEV-300-building-Secure-Python-Applications/sdev_300/disc_1
UMGC SDEV 300
3.27.24
Terrence Jackson

To date, we haven't talked too much about handling possible input errors 
resulting from a user either accidentally or purposely entering incorrect 
data that is used by the program. 
This discussion will allow you to take some of your previous code 
from week 1 or week 2 and make adjustments such that input errors are handled gracefully.

Using code you developed in week 1 or week 2 and the guidance found in this document:

http://easypythondocs.com/validation.html

use one of the two methods suggested along one or more of the validation techniques 
provided and fix your code to gracefully and securely handle user input errors.  

Just pick a smaller section of the code to fix. 
Provide the code before and after the fix. 
Be sure to demonstrate the new fix works as expected by providing screen captures.

Interact with one student and try their code fix. 
Comment on which method and techniques were used. 
Make adjustments and experiment to further demonstrate your understanding of their implementation.
"""


def main():
    """Adding input validation to my discussion 1 example"""

    valid = False

    while not valid:
        ide = input("What is your favorite IDE: ")
        if len(ide) < 1:
            print("IDE entered is too short!")
        elif len(ide) > 20:
            print("IDE entered is too long!")
        else:
            valid = True

    print(f"You chose: {ide}")

    ones_i_know = [
        "pycharm",
        "spyder",
        "visual studio code",
        "vscode",
        "eclipse",
        "vim",
    ]

    if ide.lower() in ones_i_know:
        print("Hey, I know that IDE!")
    else:
        print("I don't recognize that one...")


def tara_smith():
    """Responding to a classmate's example"""
    while True:
        try:
            first_name = str(input("What is your first name? ")).strip().upper()
            if len(first_name) < 1:
                raise ValueError("Please input at least one character.")
            if not first_name.isalpha():
                raise ValueError("Please do not use symbols or numbers")
            return first_name
        except ValueError as err:
            print(err)


if __name__ == "__main__":
    main()
