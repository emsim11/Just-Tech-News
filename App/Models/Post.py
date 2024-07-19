# Import Dependencies
from App.Database import Base # Parent Class Used To Make Table
from .Vote import Vote # Python Class Is Used To Attach A Vote Total To A Post
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func # Module Classes Used To Define Table Columns & Their Data Types
from sqlalchemy.orm import relationship, column_property # Function Decorators Used To Establish Connections Between Tables Based On Foreign Key Relationships & To Define Custom Behaviors/Constraints For Table Columns
from datetime import datetime # Python Built-In Module To Generate Timestamps

# Define The Class
class Post(Base):
  __tablename__ = 'Posts'
  Id = Column(Integer, primary_key=True)
  Title = Column(String(100), nullable=False)
  Post_URL = Column(String(100), nullable=False)
  User_Id = Column(Integer, ForeignKey('Users.Id')) # `ForeignKey` References `Users` Table
  Created_At = Column(DateTime, default=datetime.now) # Uses Python's Built-In `datetime` Module To Generate Timestamps
  Updated_At = Column(DateTime, default=datetime.now, onupdate=datetime.now) # Uses Python's Built-In `datetime` Module To Generate Timestamps
  User = relationship('User') # Dynamic Property Queries A User (Not Apart Of The `Post` Table)
  Comment = relationship('Comment', cascade='all,delete') # Dynamic Property Queries A Comment & Its User (Not Apart Of The `Post` Table)
  Votes = relationship('Vote', cascade='all,delete') # Dynamic Property Queries Information About Number Of Votes A Post Has (Not Apart Of The `Post` Table)
  Vote_Count = column_property(select(func.count(Vote.Id)).where(Vote.Post_Id == Id)) # Dynamic Property Performs A `SELECT` & SQLAlchemy `func.count()` Method To Add Up Votes

# NOTES:
# `cascade='all,delete'` Is Used To Delete Corresponding Foreign Key Records When A Record From `Posts` Table Is Deleted
# If A Post Is Deleted, Every Vote And Comment Associated With It Is Also Deleted