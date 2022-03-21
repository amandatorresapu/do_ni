from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja

@app.route('/new_ninja')
def display_ninja():
    return render_template('new_ninja.html')




# action
@app.route('/ninja/create', methods = ["POST"])
def create_ninja():
    Ninja.create(request.form)
    return render_template('view.html')


