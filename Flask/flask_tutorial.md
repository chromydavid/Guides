# FLASK Basics

## Creating virtual eviroment (venv)
- Create venv directory: `python -m venv venv`

- Move to venv (Shell will show (venv) at the start if succesful):
    - Linux: `source env/bin/activate`
    - Windows (CMD): `venv\Scripts\activate.bat`
    - Windows (Powershell): 
        - Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`    
        - Then: `venv\Scripts\Activate.ps1`

- Exit venv: `deactivate`

- Install packages (modules/libraries): `pip install Flask Flask-SQLAlchemy`
    - Flask: (main Framework)
    - SQLAlchemy: Simplifies comunication to DBs (App to DB middleman)

- Create requirements.txt: `pip freeze > requirements.txt`
    - Writes all pip libs inside requirements.txt file for future lib install
      
- If requirements.txt exists, pull libs from it: `pip install -r requirements.txt`

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
        from flask import Flask, render_template, redirect, request
        from flask_sqlalchemy import SQLAlchemy 
        
        app = Flask(__name__) #Creates flask app object

        @app.route("/") #Runs function if said route is visited
        def index():
            return render_template("index.html") #Renders index.html

        if __name__ == "__main__":  #Runs when this file is started directly
            app.run(host="0.0.0.0", port=8080, debug=True) #debug=True automatically reloads web when code is changed (remove for prod)
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
            <input type="submit" value="Add Task" id="btn_add">
        </form>
    </div>
    {% endblock %}
    ```

## Configure SQLAlchemy database
- content of `app.py`:
    ``` python
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy 
    from datetime import datetime

    app = Flask(__name__) 

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    db = SQLAlchemy(app)

    class MyTask(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        content = db.Column(db.String(100), nullable=False)
        cmplete = db.Column(db.Integer)
        created = db.Column(db.DateTime, default=datetime.utcnow)

        def __repr__(self) -> str:
            return f"Task {self.id}"
    

    @app.route("/") 
    def index():
        return render_template("index.html") 

    if __name__ == "__main__": 
        with app.app_context():
            db.create_all()
        app.run(debug=True) 
    ``` 

## HTTP requests
- We are extending the paths in our python file:
    ``` python
    @app.route("/", methods=["POST", "GET"])
    def index():
        # add a task
        if request == "POST":
            current_task = request.form["content"]
            new_task = MyTask(content=current_task)
            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect("/")
            except Exception as e:
                print(f"ERROR:{e}")
                return f"ERROR:{e}"
        # see all tasks
        else:
            tasks = MyTask.query.order_by(MyTask.created).all()
            return render_template("index.html", tasks=tasks)
    
    #delete item
    @app.route("/delete/<int:id>")
    def delete(id:int):
        delete_task = MyTask.query.get_or_404(id)
        try:
            db.session.delete(delete_task)
            de.session.commit()
            return redirect("/")
         except Exception as e:
                print(f"ERROR:{e}")
                return f"ERROR:{e}"


- Now we also need to edit index.html to be able to show the received data:
    ```html
    {% extends "base.html" %}
    {% block head %}
    <title>Task Manager</title>
    {% endblock %}

    {% block body %}
    <div class="content">
        <h1>Task manager</h1>

        {% if tasks | length < 1%}    
        <h3>No tasks to show</h3>
        {% else %}    
        <table>
            <tr>
                <th>Task</th>
                <th>Added</th>
                <th>Actions</th>
            </tr>
            {% for task in tasks %}
            <tr>
                <td>{{task.content}}</td>
                <td>{{task.created.strftime("%Y-%m-%d")}}</td>
                <td>
                    <a href="/delete/{{task.id}}">Delete</a>
                </td>
            </tr>
            {% endfor %}
        </table>
        {% endif %}
        <form action="/" method="POST">
            <input type="text" name="content" id="content">
            <input type="submit" value="Add Task" id="btn_add">
        </form>
    </div>
    {% endblock %}
    ```
