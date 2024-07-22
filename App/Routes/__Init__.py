# Import `Blueprints` From Modules & Rename Them
from .Home import Blueprints as Home
from .Dashboard import Blueprints as Dashboard
from .API import Blueprints as API

# NOTES: 
# Without This App File, Import In `App/__Init__.py`
# Would Be `App.Routes.Home import Blueprints as Home`