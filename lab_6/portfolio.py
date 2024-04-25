r"""
Flask App
=========
Generate a simple Web site using Python flask. 
The site should be unique, include at least 3 routes (e.g. 3 pages one can navigate),
each route should render the HTML pages by using the render_template() functionality.
A style sheet should be included that is used by all Web pages.
Proper organization should take place of the web site
including the location of templates and static pages.
Keep in the basic HTML form for a function web page includes the following components:
    <!DOCTYPE html>
    <html>
    <head>
    <title>Page Title</title>
    </head>
    <body>
    ...your page content...
    </body>
    </html>
In addition to the requirements list above the following functionality
should be found within your web site on one or more web pages.
    - Use at least 3 different heading styles (e.g. <h1>, <h2>, <h3>)
    - Paragraph (<p>)
    - Comments <!-- -->)
    - Ordered list
    - Unordered list
    - At least 3 Links to other External Web Sites
    - Display the Date and Time on a Web page 
        (Hint: Just use the Python datetime functions)

The content and topic of the Web site is up to you.
Consider an information web site about a topic you are interested.
It should be unique and something you want to create.

Hints:
1. Be sure to end tags that are started (e.g. <h1> </h1>)
2. Start early. This will take you longer than you think.
3. Use comments to document your code
4. Test with many combinations.
5. Use pylint to verify the code style – the goal is a 10!

Author
------
Terrence Jackson

Last Modified
-------------
4.21.24

Class
-----
UMGC SDEV 300

Additional Details
------------------
Command to run in my poetry environment:
`poetry run flask --app .\sdev_300\lab_6\portfolio.py run`

"""
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def landing():
    """Renders landing page with today's date"""
    today_ = datetime.today()
    date_string = f"{today_.strftime(r"%B, %d %Y")} at {today_.strftime(r"%I:%M%p")}"
    return render_template(
        "welcome.html",
        current_datetime=date_string,
    )


@app.route("/about")
def about():
    """Renders about page"""
    return render_template("about.html")


@app.route("/resume")
def resume():
    """Renders resume page"""
    return render_template("resume.html")

@app.route("/contact")
def contact():
    """Renders contact page"""
    return render_template("contact.html")
