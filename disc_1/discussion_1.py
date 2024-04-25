"""
Discussion 1: Programming Style Guides
UMGC SDEV 300
3.10.24
Terrence Jackson

Programming style guides exist for practically every programming language including Python.

After you have successfully installed pylint on your desktop
(see the Install Python guide in week 1 content), 
create a simple Python application and save the file in an appropriately named file. 
The application should be unique (something you create) and be less than 10 lines of code.
For example, you could write a simple math calculation 
or a query asking the user for their favorite color/food or other item.

The goal is to write a few lines of code and then analyze the code using using pylint 
and then discuss the results and steps to fixing each recommendation from pylint.

Work to remove all issues making the code a "10.00 out of 10". 
Include your code as well as each output report showing how you 
resolved each error code in the pylint output.
"""

ide = input("What is your favorite IDE: ")

print(f"You chose: {ide}")

ones_i_know = ["pycharm", "spyder", "visual studio code", "vscode", "eclipse", "vim"]

if ide.lower() in ones_i_know:
    print("Hey, I know that IDE!")
else:
    print("I don't recognize that one...")
