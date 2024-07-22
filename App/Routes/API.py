from flask import Blueprint, request, jsonify, session
from App.Models import User
from App.Database import Get_Database
import sqlalchemy
import sys

Blueprints = Blueprint('API', __name__, url_prefix='/api')

# Define Signup Route
@Blueprints.route('/users', methods=['POST'])
def Signup():
  Data = request.get_json()
  Database = Get_Database()
  
	# Attempt To Create A New User
  try:
    NewUser = User(
			Username = Data['Username'],
			Email = Data['Email'],
			Password = Data['Password']
		)
    # Save In Database
    Database.add(NewUser)
    Database.commit()
    # Show Success Message
    print('Success!')
  
  # New User Insert Failed
  except AssertionError:
    print('Validation Error')
  except sqlalchemy.exc.IntegrityError:
    print('MySQL Error')
  except:
    print(sys.exc_info()[0])
    # Rollback Last Commit
    Database.rollback()
    # Send Error To Front-End
    return jsonify(message = 'Signup Failed'), 500
  
  # Add User Session To The App
  # Clear Any Existing Session Data
  session.clear()
  # Add `User_Id` Session Property To Aid Future Database Queries
  session['User_Id'] = NewUser.Id
  # Add `LoggedIn` Session Boolean Property For Templates To Use To Conditionally Render Elements
  session['LoggedIn'] = True
  
  return jsonify(Id = NewUser.Id)

# Define Logout Route
@Blueprints.route('/users/logout', methods=['POST'])
def Logout():
  # Remove Session Variables
  session.clear()
  # Status Code Of 204 Indicates There Is No Content
  return '', 204

# Define Login Route
@Blueprints.route('/users/login', methods=['POST'])
def Login():
  Data = request.get_json()
  Database = Get_Database()
  # Check Wether The User's Posted Email Address Exists In Database
  try:
    Users = Database.query(User).filter(User.Email == Data['Email']).one()
  except:
    print(sys.exc_info()[0])
    return jsonify(message = 'Incorrect Credentials'), 400
	# If Email Exists, Verify Password
  if Users.Verify_Password(Data['Password']) == False:
    return jsonify(message = 'Incorrect Credentials'), 400
  # Create New User Session
  session.clear()
  session['User_Id'] = Users.Id
  session['LoggedIn'] = True
  # Send Back Valid Response
  return jsonify(Id = Users.Id)