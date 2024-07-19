# CONNECT DATABASE SCRIPT: `python3 App/Database/__Init__.py`
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Connect To Database Using Environment Variables
Engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=Engine)
Base = declarative_base()

# NOTES:
#
# Engine variable manages the overall database connection.
# Session variable generates temporary connections for performing CRUD operations.
# Base class variable helps map the models to real MySQL tables.