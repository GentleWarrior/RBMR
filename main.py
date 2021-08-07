from flask import Flask, render_template, blueprints
from scriptspy import views
from scriptspy import create_app
from flask_login import login_required, current_user


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


@app.route('/Dashboard.html')
@login_required
def profile():
    return render_template('Dashboard.html', name=current_user.name)

if __name__ == "__main__":

    app.run(host='localhost', port='5000', debug=True)