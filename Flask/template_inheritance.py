"""
Allows us to have a base html and just inherit from it.

Into the home.html we add (at the start):
{% extends 'base.html' %}

We can also change some parts of the base html (for exaple title):
base.html:
    <title>
        {% block title %}

        {% endblock %}
    </title>  

home.html:
    {% extends 'base.html' %}
    {% block title %}
        Home Page
    {% endblock %} 

This way we inherit base.html into home.html but we change the Title.
"""

from flask import Flask, render_template

app = Flask(__name__)   


@app.route("/")     
def hi_everyone():
    return("<h>hi everyone<h>") 

@app.route("/render_html")
def render_html():
    return render_template("home.html") 

app.run(host="0.0.0.0", port=80)   