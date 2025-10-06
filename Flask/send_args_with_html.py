from flask import Flask, render_template
app = Flask(__name__) 


@app.route("/render_html_with_args")
def render_html():
    return render_template("home.html", username="David") 
# renders home.html + sends variable username to be used in said html file via {{username}}
# using python logic in html requires Jinja library (already installed in Flask)
# Jinja enables you to use python logic like for loops and variables in html templates to 
# work with args given via render_template() function  

@app.route("/dict")
def render_html_with_dict():
    items = [
        {"id": 1, "name": "Phone", "barcode": 8445124, "price": 500},
        {"id": 2, "name": "TV", "barcode": 158451, "price": 800},
        {"id": 3, "name": "Mouse", "barcode": 548229, "price": 90}
    ]

    return render_template("store.html", items_list=items) # sending list[dict] in variable items_list 

# using this code we can then iterate through the list and generate a table with all the arguments inside each dictionary
"""
    {% for item in items %}
        <tr>
            <td> {{item.id}} <td>
            <td> {{item.name}} <td>
            <td> {{item.barcode}} <td>
            <td> {{item.price}} <td>
        <tr>
    {% endfor %}
"""