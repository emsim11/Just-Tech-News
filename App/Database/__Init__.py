# Connect To Database With Script: `python3 App/Database/__Init__.py`
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

load_dotenv()

# Connect To Database Using Environment Variables
Engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=Engine)
Base = declarative_base()

# Initial Database Connection
def Init_Database(App):
  Base.metadata.create_all(Engine)
  # Run `Close_Database()` Automatically Whenever A Context Is Destroyed
  App.teardown_appcontext(Close_Database)

# Return New Session-Connection Object
def Get_Database():
  if 'Database' not in g:
    # Store Database Connection In App Context
    g.Database = Session()
  # Return Connection From `g` Object Instead Of Creating New `Session` Instance Each Time
  return g.Database

def Close_Database(e=None):
  # `pop()` Method Finds & Removes `Database` From `g` Object
  Database = g.pop('Database', None)
  # If `Database` Exists, End The Connection
  if Database is not None:
    Database.close()
# NOTES:
#
# Engine variable manages the overall database connection.
# Session variable generates temporary connections for performing CRUD operations.
# Base class variable helps map the models to real MySQL tables.