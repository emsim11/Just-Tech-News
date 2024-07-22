# Import Flask Functions
from flask import Blueprint, render_template, session, redirect

# Import Database Connections & Defined Models
from App.Database import Get_Database
from App.Models import Post

# `Blueprint()` Consolidates Routes Onto Single Object That Parent App Registers
Blueprints = Blueprint('Home', __name__, url_prefix='/')

# Define `/` Route
@Blueprints.route('/')
def Index():
  # Return Session Connection That's Tied To This Route's Context
  Database = Get_Database()
  # Use `query()` Method On Connection Object To Query `Post` Model For All Posts In Descending Order & Save Results In `Posts` Variable
  Posts = Database.query(Post).order_by(Post.Created_At.desc()).all()
  # Render `Homepage.html` Template With `Posts` Data & Pass `LoggedIn` Session To Template
  return render_template('Homepage.html', Posts=Posts, LoggedIn=session.get('LoggedIn'))

# Define `/login` Route
@Blueprints.route('/login')
def Login():
  # If User Is Not Logged In Yet, Direct To Login Page
  if session.get('LoggedIn') is None:
    return render_template('Login.html')
  # If User Is Logged In, Redirect To Dashboard
  return redirect('/dashboard')

# `<Id>` Route Parameter Becomes Function Parameter In `Single(Id)` Function
@Blueprints.route('/post/<Id>')
def Single(Id):
  Database = Get_Database()
  # Query A Single Post By `Post.Id`
  Posts = Database.query(Post).filter(Post.Id == Id).one()
  # Render `Single-Post.html` Template With A Post's Data & Pass `LoggedIn` Session To Template
  return render_template('Single-Post.html', Post=Posts, LoggedIn=session.get('LoggedIn'))