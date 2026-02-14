from flask import render_template
from . import game


@game.route("/tictoe")
def index():
    return render_template("game/tictoe.html")