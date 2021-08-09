from flask import Blueprint, render_template, request, flash, redirect, url_for
from scriptspy.models import User, Admin, Personal, Contact
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from scriptspy import db

auth = Blueprint('auth', __name__)


@auth.route('/login.html')
def login():
    return render_template('login.html')


@auth.route('/profileSubmit', methods=['POST', 'GET'])
def profilesub():

    first_name = request.form.get('first_name')
    DOB = request.form.get('DOB')
    Gender = request.form.get('Gender')


    user = User.query.filter_by(first_name=first_name).first()

    new_personal = Personal(DOB=DOB, Gender=Gender, user_id=user.id)
    # add the new user to the database
    db.session.add(new_personal)
    db.session.commit()

    return redirect(url_for('contact'))


@auth.route('/ContactSubmit', methods=['POST'])
def contactSub():

    Email = request.form.get('Email')
    Address = request.form.get('Address')
    City = request.form.get('City')
    District = request.form.get('District')
    Phone = request.form.get('Phone')


    user = User.query.filter_by(email=Email).first()

    new_contact = Contact(Address=Address, City=City, District=District, Phone=Phone, user_id=user.id)
    # add the new user to the database
    db.session.add(new_contact)
    db.session.commit()

    return redirect(url_for('health'))


@auth.route('/login', methods=['POST', 'GET'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    admin = Admin.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not admin or not check_password_hash(admin.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(admin, remember=remember)
    return redirect(url_for('profile'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup_post():
    email = request.form.get('email')
    fname = request.form.get('first_name') #give an input the name='first_name' on your front end
    lname = request.form.get('last_name') #give an input the name='last_name' on your front end
@auth.route('/signup_donor', methods=['GET', 'POST'])


def signup_donor():
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    password = request.form.get('password')


    user = User.query.filter_by(email=email).first()  # if this returns a user, then the email already exists in
    # database
    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup_donor'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.

    new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password, method='sha256'))
    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('personal', first_name=first_name))


@auth.route('/signup_doc', methods=['POST'])
def signup_doc():
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    password = request.form.get('password')

    admin = Admin.query.filter_by(email=email).first()  # if this returns a user, then the email already exists in
    # database
    if admin:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup_doc'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_admin = Admin(first_name=first_name, last_name=last_name, email=email, password=generate_password_hash(password, method='sha256'))
    print(new_admin)
    # add the new user to the database
    db.session.add(new_admin)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.py'))
