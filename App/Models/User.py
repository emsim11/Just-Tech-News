# Import Dependencies
from App.Database import Base # Parent Class Used To Make Table
from sqlalchemy import Column, Integer, String # Module Classes Used To Define Table Columns & Their Data Types
from sqlalchemy.orm import validates # Function Decorator Used To Validate Data Before Inserting Into Database
import bcrypt # `bcrypt` Module To Create Salt To Hash Password Against

# Generate Random Salt Value Used In Password Hashing Function
Salt = bcrypt.gensalt()

# Define The Class
class User(Base):
  __tablename__ = 'Users'
  Id = Column(Integer, primary_key=True)
  Username = Column(String(50), nullable=False)
  Email = Column(String(50), nullable=False, unique=True)
  Password = Column(String(100), nullable=False)
    
  # Email Validation Method
  @validates('Email')
  def Validate_Email(Self, key, Email):
    # Require Email Address To Contain At-Sign (`@`) Character
    assert '@' in Email, 'User Object Is Missing At-Sign `@` Character In Email Property'
    # If Email Is Valid, Return Value & Continue 
    return Email
    
  # Password Validation Method
  @validates('Password')
  def Validate_Password(Self, key, Password):
    # Require Password To Be 8+ Characters
    assert len(Password) > 8, 'User Object Has Invalid Password Length (Must Be At Least 8 Characters)'
    # Encrypt Password 
    return bcrypt.hashpw(Password.encode('utf-8'), Salt)
  	# If Password Is Valid, Return Value & Continue
    return Password
  
# NOTES:
# `assert` Statements Will Throw An Error If Condition Is False & Prevent Moving To Next Command