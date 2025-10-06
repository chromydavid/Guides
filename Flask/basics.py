"""
pip install flask   # flask lib 
pip install requests    #interact with APIs
"""
"""
basic flask structure:
flask_app/
│
├── app/                      # Main application package
│   ├── __init__.py           # Initializes Flask app and extensions
│   ├── routes.py             # Routes / endpoints
│   ├── models.py             # Database models (if using SQLAlchemy)
│   ├── forms.py              # Forms (if using Flask-WTF)
│   ├── static/               # Static files (CSS, JS, images)
│   │   └── style.css
│   └── templates/            # HTML templates (Jinja2)
│       └── index.html
│
├── venv/                     # Virtual environment (optional, ignored by Git)
│
├── config.py                 # Configuration file (e.g., database URI, secret key)
├── run.py                    # Entry point to run the app
└── requirements.txt          # Python dependencies
"""

from flask import Flask, render_template

app = Flask(__name__)   # creates flask instance with args = to my current file so that flask knows where to find everything


# These decorators call their functions when the route criteria is met. 
# In this example hi_everyone() is called when the base url is loaded
@app.route("/")     
def hi_everyone():
    return("<h>hi everyone<h>") # fills empty space with whatever you put as return value

@app.route("/render_html")
def render_html():
    return render_template("home.html") # renders/returns html file for client to load

app.run(host="0.0.0.0", port=80)    # runs app on said ip/port this allows for local hosting