# Import `Flask()` function
from flask import Flask

# Import Routes
from App.Routes import Home, Dashboard

# Use `def` Keyword To Define `create_app()` Function
def create_app(test_config=None):
  # Declare New `App` Variable
  App = Flask(__name__, static_url_path='/')
  # Setup App Flask Config
  # Serve Any Static Resources From Root Directory
  App.url_map.strict_slashes = False
  # Use The `Super_Secret_Key` Key When Creating Server-Side Sessions
  App.config.from_mapping(
    SECRET_KEY='Super_Secret_Key'
  )
  
  # Create `Hello` Route
  # Turn `Hello()` Function Into A Route
  @App.route('/hello')
  # Create `Hello()` Inner Function To Return A String
  def Hello():
    return 'Hello World! 🌈'
  
  # Register Routes
  App.register_blueprint(Home) # Home Routes
  App.register_blueprint(Dashboard) # Dashboard Routes
  
  # `return` Is The Route's Response
  return App