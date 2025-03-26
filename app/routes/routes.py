from flask import Blueprint, render_template

global_routes = Blueprint('global', __name__)

@global_routes.route('/')  # GET http://127.0.0.1:5000/
def home():
    return render_template("home.html")

from flask import Blueprint, render_template
from flask_login import login_required

dashboard_bp = Blueprint('dashboard', __name__)

@global_routes.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')