# Import Dependencies
from App.Database import Base # Parent Class Used To Make Table
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime # Module Classes Used To Define Table Columns & Their Data Types
from sqlalchemy.orm import relationship # Function Decorator Used To Establish Connections Between Tables Based On Foreign Key Relationships
from datetime import datetime # Python Built-In Module To Generate Timestamps

class Comment(Base):
  __tablename__ = 'Comments'
  Id = Column(Integer, primary_key=True)
  Comment_Text = Column(String(255), nullable=False)
  Post_Id = Column(Integer, ForeignKey('Posts.Id')) # `ForeignKey` References `Posts` Table
  User_Id = Column(Integer, ForeignKey('Users.Id')) # `ForeignKey` References `Users` Table
  Created_At = Column(DateTime, default=datetime.now) # Use Python's Built-In `datetime` Module To Generate Timestamps
  Updated_At = Column(DateTime, default=datetime.now, onupdate=datetime.now) # Use Python's Built-In `datetime` Module To Generate Timestamps
  User = relationship('User') # Dynamic Property Queries A User (Not Apart Of The `Post` Table)