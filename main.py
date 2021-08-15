from flask import Flask, render_template, blueprints
from scriptspy import views
from scriptspy import create_app
from flask_login import login_required, current_user
from scriptspy.models import User, Admin, Personal, Contact


app = create_app()


@app.route("/Home.html")
def home():
    return render_template('Home.html')


@app.route("/Learn More.html")
def about():
    return render_template('Learn More.html')


@app.route("/How To.html")
def how():
    return render_template('How To.html')


@app.route("/Register.html")
def register():
    return render_template('Register.html')


@app.route("/Personal details.html")
def personal():
    return render_template('Personal details.html')


@app.route("/Contact Details.html")
def contact():
    return render_template('Contact Details.html')


@app.route("/Health Details.html")
def health():
    return render_template('Health Details.html')


@app.route("/Dashboard.html")
def dash():
    return render_template('Dashboard.html')

@app.route("/Donors.html")
def don():
    donors = User.query.all()
    details = Personal.query.all()
    contacts = Contact.query.all()

    return render_template('Donors.html', email=current_user.email, donors=donors, details=details,
                           contacts=contacts)

@app.route("/Donor Records.html")
def records():
    donors = User.query.all()
    details = Personal.query.all()
    contacts = Contact.query.all()

    return render_template('Donor Records.html', email=current_user.email, donors=donors, details=details, contacts=contacts)

@app.route("/Doctors.html")
def doctors():
    doctors = Admin.query.all()
    doctorcount = Admin.query.count()

    return render_template('Doctors.html', email=current_user.email, doctors=doctors, doctorcount=doctorcount)


@app.route('/profile')
@login_required
def profile():
    donors = User.query.all()
    doctorcount=Admin.query.count()
    print(doctorcount)
    donorcount=User.query.count()
    print(donorcount)
    details = Personal.query.all()
    contacts = Contact.query.all()

    return render_template('Dashboard.html', email=current_user.email, donors=donors, details=details, contacts=contacts, donorcount=donorcount, doctorcount=doctorcount)


if __name__ == "__main__":
    app.run(host='localhost', port='5000', debug=True)
