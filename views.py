from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route('/')
def homepage():
    return render_template("Dashboard.html")

@views.route('/whatigot')
def whatigot():
    return render_template("What_I_Got.html")

@views.route('/floods')
def floods():
    return render_template("Floods.html")