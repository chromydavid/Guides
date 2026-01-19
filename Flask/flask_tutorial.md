# FLASK Basics

## Creating virtual eviroment (venv)
- Create venv directory: `python -m venv env`

- Move to venv: `source env/bin/activate`

- Exit venv: `deactivate`

- Install packages (modules/libraries): `pip install Flask Flask-Scss Flask-SQLAlchemy`
    - Flask: (main Framework)
    - Flask-Scss: (Sassy CSS)
    - SQLAlchemy: Simplifies comunication to DBs (App to DB middleman)

- Create requirements.txt (inside venv): `pip freeze > requirements.txt`
    - Writes all pip libs inside venv into the requirements.txt file

## Initial setup
- Create `app.py`
    - `app.py` will be our main run-app file
    - Possible content of `app.py`:
        ``` python
        from flask import Flask
        from flask_scss import Scss
        from flask_sqlalchemy import SQLAlchemy #Recommend using Sass VSCode extension
        
        app = Flask(__name__)

        @app.route("/")
        def index():
            return "Testing 123"

        if __name__ == "__main__":
            app.run(debug=True)
        ``` 