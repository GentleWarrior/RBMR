from flask import Flask, render_template, blueprints
from scriptspy import views
from scriptspy import create_app
from flask_login import login_required, current_user


app = create_app()


@app.route("/Home.html")
def home():
    return render_template('Home.html')


@app.route("/How it works.html")
def about():
    return render_template('How it Works.html')


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


@app.route('/login.html')
@login_required
def profile():
    return render_template('login.html', name=current_user.name)


#Using this for testing
@app.route('/testcreateac')
def test():
    from scriptspy.models import User
    from werkzeug.security import generate_password_hash
    from scriptspy import db

    new = User(email='test@test.com', first_name='John',last_name='Doe', password=generate_password_hash('test', method='sha256'))

    # add the new user to the database
    db.session.add(new)
    db.session.commit()
    return 'Added user to db'

if __name__ == "__main__":

    app.run(host='localhost', port='5000', debug=True)