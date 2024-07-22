# Import `Blueprint()` & `render_template()` Functions
from flask import Blueprint, render_template, session

# Prefix Every Route In `Blueprint()` With `/dashboard`
Blueprints = Blueprint('Dashboard', __name__, url_prefix='/dashboard')

# Define `/dashboard` Route
@Blueprints.route('/')
def Dashboard():
  # Render `Dashboard.html` Template
  return render_template('Dashboard.html', LoggedIn=session.get('LoggedIn'))

# Define `/dashboard/edit/<Id>` Route
@Blueprints.route('/edit/<id>')
def Edit(Id):
  # Render `Edit-Post.html` Template
  return render_template('Edit-Post.html')