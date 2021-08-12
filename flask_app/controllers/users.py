# burgers.py
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.users import Users

@app.route('/')
def index():

    users_info = Users.get_all()
    print(users_info)
    
    return render_template('read.html', all_users = users_info)

@app.route('/users')
def users():

    return render_template('create.html')

@app.route('/add_user', methods = ['POST'])
def add_user():

    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    Users.save(data)

    return redirect('/')

@app.route('/show_user/<int:id>')
def show_user(id):
    print("User Id: ", id)
    users_info = Users.single_user(id)

    return render_template('show_user.html', all_users = users_info)

@app.route('/edit_user/<int:id>')
def edit_user(id):
    print("edit user pressed ", id)
    session['results'] = Users.user_result

    print("session results: " , session['results'])
    return render_template('/edit.html', id = id)

@app.route('/edit/<int:id>', methods = ['POST'])
def edit(id):

    data = {
        "id": id,
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }

    print("data: ", data)
    Users.edit(data, id)

    return redirect('/')

@app.route('/delete_user/<int:id>')
def delete_user(id):
    print("pressed delete, delete_user/ ", id)

    data = {
        "id": id
    }

    Users.delete(data, id)
    
    return redirect('/')