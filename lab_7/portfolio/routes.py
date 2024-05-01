"""
Routes
==============
Flask Blueprint for rendering non-auth routes

Author
------
Terrence Jackson

Last Modified
-------------
4.28.24

Class
-----
UMGC SDEV 300
"""

from datetime import datetime

from flask import Blueprint, g, redirect, render_template, url_for

bp = Blueprint("routes", __name__)

@bp.before_request
def before_request():
    """Check if logged in first"""
    if not g.user:
        # if not logged in, redirect to login page
        return redirect(url_for("auth.login"))

@bp.route("/")
def landing():
    """Renders landing page with today's date"""
    today_ = datetime.today()
    date_string = f"{today_.strftime(r"%B, %d %Y")} at {today_.strftime(r"%I:%M%p")}"
    return render_template(
        "routes/landing.html",
        current_datetime=date_string,
    )


@bp.route("/about")
def about():
    """Renders about page"""
    return render_template("routes/about.html")


@bp.route("/resume")
def resume():
    """Renders resume page"""
    return render_template("routes/resume.html")


@bp.route("/contact")
def contact():
    """Renders contact page"""
    return render_template("routes/contact.html")
