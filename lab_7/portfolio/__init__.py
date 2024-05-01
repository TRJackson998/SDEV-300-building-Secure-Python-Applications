"""
Portfolio Module Init
=====================
Initializes and configures the Flask app
Registers the auth and routes blueprints

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

from flask import Flask

from . import auth, routes

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY="dev",
)

app.register_blueprint(auth.bp)
app.register_blueprint(routes.bp)
