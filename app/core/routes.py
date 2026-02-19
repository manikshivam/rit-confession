from flask import render_template
from . import core


@core.route("/contact")
def contact():
    return render_template("contact.html")

@core.route("/about")
def about():
    return render_template("about.html")