from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

# display
@app.route('/')
def index():
    dojo = Dojo.get_all()
    return render_template('index.html', all_dojos = dojo)


@app.route('/ninjas/view')
def view_all_ninjas(id):
    data = {"id": id}
    dojo = Dojo.get_all_ninjas(data)
    return render_template ("view.html", dojo=dojo)
#action

@app.route ('/dojo/create', methods=["POST"])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/')


# button for new add ninjas????