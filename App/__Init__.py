from flask import Flask # Import `Flask()` function
from App.Routes import Home, Dashboard # Import Routes
from App.Database import Init_Database # Import Database Connection
from App.Utilities import Filters # Register Custom Filter Functions With Jinja Template Environment

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
  
  # Register Custom Filter Functions
  App.jinja_env.filters['Format_URL'] = Filters.Format_URL
  App.jinja_env.filters['Format_Date'] = Filters.Format_Date
  App.jinja_env.filters['Format_Plural'] = Filters.Format_Plural

  # Initiate Database Once Flask App Is Ready
  Init_Database(App)
  
  # `return` Is The Route's Response
  return App