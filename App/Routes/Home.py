# Import `Blueprint()` & `render_template()` Functions
from flask import Blueprint, render_template

# `Blueprint()` Consolidates Routes Onto Single Object That Parent App Registers
Blueprints = Blueprint('Home', __name__, url_prefix='/')

# Define `/` Route
@Blueprints.route('/')
def Index():
  # Render `Homepage.html` Template
  return render_template('Homepage.html')

# Define `/login` Route
@Blueprints.route('/login')
def Login():
  # Render `Login.html` Template
  return render_template('Login.html')

# `<Id>` Route Parameter Becomes Function Parameter In `Single(Id)` Function
@Blueprints.route('/post/<Id>')
def Single(Id):
  # Render `Single-Post.html` Template
  return render_template('Single-Post.html')