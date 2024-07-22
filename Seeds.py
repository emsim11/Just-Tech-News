# Seed Database With Command: `python3 Seeds.py`

# Import Database And Tables
from App.Models import User, Post, Comment, Vote
from App.Database import Session, Base, Engine

# Drop And Rebuild Tables
Base.metadata.drop_all(Engine)
Base.metadata.create_all(Engine)

# Establish Temporary Session Connection With `Session` Class
Database = Session()

# Insert Users
Database.add_all([
  User(Username='testuser', Email='testing@example.com', Password='Password123456'),
  User(Username='jwilloughway1', Email='jwilloughway1@gmail.com', Password='Password123456'),
  User(Username='cstoneman2', Email='cstoneman2@outlook.com', Password='Password123456'),
  User(Username='dstanton3', Email='dstanton3@aol.com', Password='Password123456'),
  User(Username='juliaroberts4', Email='juliaroberts4@yahoo.com', Password='Password123456')
])

# Insert Posts
Database.add_all([
  Post(Title='Donec Posuere Metus Vitae Ipsum', Post_URL='https://buzzfeed.com/in/imperdiet/et/commodo/vulputate.png', User_Id=1),
  Post(Title='Morbi Non Quam Nec Dui Luctus Rutrum', Post_URL='https://nasa.gov/donec.json', User_Id=1),
  Post(Title='Donec Diam Neque, Vestibulum Eget, Vulputate Ut, Ultrices Vel, Augue', Post_URL='https://europa.eu/parturient/montes/nascetur/ridiculus/mus/etiam/vel.aspx', User_Id=2),
  Post(Title='Nunc Purus', Post_URL='http://desdev.cn/enim/blandit/mi.jpg', User_Id=3),
  Post(Title='Pellentesque Eget Nunc', Post_URL='http://google.ca/nam/nulla/integer.aspx', User_Id=4)     
])

# Insert Comments
Database.add_all([ 
  Comment(Comment_Text='Nunc rhoncus dui vel sem.', User_Id=1, Post_Id=2),
  Comment(Comment_Text='Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.', User_Id=1, Post_Id=3),
  Comment(Comment_Text='Aliquam erat volutpat. In congue.', User_Id=2, Post_Id=1),
  Comment(Comment_Text='Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.', User_Id=2, Post_Id=3),
  Comment(Comment_Text='In hac habitasse platea dictumst.', User_Id=3, Post_Id=3)
])

# Insert Votes
Database.add_all([
    Vote(User_Id=3, Post_Id=1),
    Vote(User_Id=1, Post_Id=2),
    Vote(User_Id=4, Post_Id=2),
    Vote(User_Id=1, Post_Id=4),
    Vote(User_Id=2, Post_Id=4),
    Vote(User_Id=3, Post_Id=4),
])

# Run `INSERT` Statements
Database.commit()

# Close Session Connection Once Finished Making Database Transactions
Database.close()