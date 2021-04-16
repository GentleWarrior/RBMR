from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__, static_folder='static', template_folder='template')


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("Home.html")


@views.route('/', methods=['GET', 'POST'])
def howit():
    return render_template("How it Works.html")


@views.route('/',  methods=['GET', 'POST'])
def register():
    return render_template("Register.html")


@views.route('/',  methods=['GET', 'POST'])
def contact():
    return render_template("Personal details.html")


@views.route('/',  methods=['GET', 'POST'])
def personal():
    return render_template("Contact Details.html")


@views.route('/',  methods=['GET', 'POST'])
def health():
    return render_template("Health Details.html")


@views.route('/', methods=['GET', 'POST'])
def dash():
    return render_template('Dashboard.html')
