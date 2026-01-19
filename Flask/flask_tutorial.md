# FLASK Basics

## Creating virtual eviroment (venv)
- Create venv directory: `python -m venv env`

- Move to venv: `source env/bin/activate`

- Exit venv: `deactivate`

- Install packages (modules/libraries): `pip install Flask Flask-SQLAlchemy`
    - Flask: (main Framework)
    - SQLAlchemy: Simplifies comunication to DBs (App to DB middleman)

- Create requirements.txt (inside venv): `pip freeze > requirements.txt`
    - Writes all pip libs inside venv into the requirements.txt file

## Simple project structure
    ``` yaml
    flask_app/
    │
    ├── venv/                 # Virtual environment 
    │
    ├── static/               # Static files (CSS, JS, images)
    │   └── style.css
    │
    ├── templates/            # HTML templates 
    │       └── index.html
    │
    ├── app.py                # Entry point to run the app
    └── requirements.txt      # Python dependencies
    ```

## Initial setup
- Create `app.py`
    - `app.py` will be our main run-app file
    - Possible content of `app.py`:
        ``` python
        from flask import Flask
        from flask_sqlalchemy import SQLAlchemy 
        
        app = Flask(__name__) #Creates flask app object

        @app.route("/") #Runs function if said route is visited
        def index():
            return render_template("index.html") #Renders index.html

        if __name__ == "__main__":  #Runs when this file is started directly
            app.run(debug=True) #debug=True automatically reloads web when code is changed (remove for prod !!unsafe)
        ``` 

## Template inheritance
- We create a base.html template:
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{{url_for("static", filename="styles.css")}}">
        {% block head %}{% endblock %}
    </head>
    <body>
        {% block body %}{% endblock %}
    </body>
    </html>
    ```
    - The {block} are used as a marker of space into which we can later inser code

- Now we can create the index.html and we can just inherit the boilerplate from base.html:
    ```html
    {% extends "base.html" %}
    {% block head %}
    <title>Task Manager</title>
    {% endblock %}

    {% block body %}
    <div class="content">
        <h1>Task manager</h1>
        <table>
            <tr>
                <th>Task</th>
                <th>Added</th>
                <th>Actions</th>
            </tr>
            <tr>
                <td>Content</td>
                <td>Date</td>
                <td>More</td>
            </tr>
        </table>
        <form action="">
            <input type="text" name="content" id="content">
            <input type="sub" >
        </form>
    </div>
    {% endblock %}
    ```