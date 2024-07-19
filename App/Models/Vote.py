# Import Dependencies
from App.Database import Base # Parent Class Used To Make Table
from sqlalchemy import Column, Integer, ForeignKey # Module Classes Used To Define Table Columns & Their Data Types

class Vote(Base):
  __tablename__ = 'Votes'
  Id = Column(Integer, primary_key=True)
  User_Id = Column(Integer, ForeignKey('Users.Id')) # `ForeignKey` References `Users` Table
  Post_Id = Column(Integer, ForeignKey('Posts.Id')) # `ForeignKey` References `Posts` Table
  
# NOTES:
# The `Votes` Python Class Doesn't Store Any Unique Information.
# A `Vote` Requires References To:
# - A `Post` That Is Being Upvoted
# - A `User` Id Of The Person Who Upvoted The Post