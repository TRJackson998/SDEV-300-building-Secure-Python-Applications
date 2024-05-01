"""
Portfolio App
=============
This exercise uses your programming environment to enhance the Web site you
created last week with additional functionality to include images, tables and a Form using
Python flask. Specifically, you will add two (2) additional routes allowing a user to register and
login to a web site. Additional security considerations include other routes (beyond the register
route) will not be accessible until a successful login has occurred.

In addition to the requirements list above,
the following functionality should be found within your web site on one or more web pages.
    - Add at least 4 different images. The images should be local in your environment.
        For example, they should be saved in your environment
        and referenced similar to this syntax: <img src="image.gif">
    - A Table with at least 4 rows and 3 columns.
    - A user registration form
    - A user login form
    - A password complexity should be enforced to include at least 12 characters in length, and
        include at least 1 uppercase character, 1 lowercase character,
        1 number and 1 special character.

The content and topic of the new images, and tables are up to you.
How much is required for the user registration is up to you as well.
However, the registration and associated login should contain at least a login name and password.

Hints:
1. Start early. This will take you longer than you think.
2. Test all aspects of the forms from input to output on your environment.
3. Use comments to document your code
4. Test with many combinations.
5. Use pylint to verify the code style – the goal is a 10!

Author
------
Terrence Jackson

Last Modified
-------------
4.25.24

Class
-----
UMGC SDEV 300

Notes
-----
A lot of this project is based on the Flask tutorial:
Based on https://flask.palletsprojects.com/en/3.0.x/tutorial/
"""

from lab_7.portfolio import app

app.run(debug=True)
