"""
Portfolio App
=============
In this exercise you will update your web site to include a password update form and 
provide additional validation on the password check.
Specifically you should create: 
    a. Password update Form – 
        This Python form allows a previously registered user to reset their password
        after they have successfully logged in. 
    b. Authentication functions – 
        These Python functions will check the following NIST SP 800-63B criteria
        are met upon password update: 
        - Use the previous criteria for password length and complexity.
          (This work should already be done.) 
        - Compare the prospective secrets against a list that contains values known to be commonly-
            used, expected, or compromised (Provided as CommonPasswords.txt). 
        - If the chosen secret is found in the list, 
          the application SHALL advise the subscriber that they need to select a different secret. 
    c. Logger – 
        Create a log to log all failed login attempts. 
        The Log should include date, time and IP address.  
 
Hints: 
1. Start early. This will take you longer than you think.
2. Leverage the File I/O, Flask and Data structures work previously performed in the class.
3. Use functions to enhance code reuse and modularity.
4. Use Python Lists or other data structures to store the Common Passwords 
    and then appropriate search functions to expedite comparisons.
5. Use comments to document your code 
6. Test with many combinations.  
7. Use pylint to verify the code style – the goal is a 10!

Author
------
Terrence Jackson

Last Modified
-------------
5.1.24

Class
-----
UMGC SDEV 300

Notes
-----
A lot of this project is based on the Flask tutorial:
Based on https://flask.palletsprojects.com/en/3.0.x/tutorial/
"""

from lab_8.portfolio import app

app.run(debug=True)
