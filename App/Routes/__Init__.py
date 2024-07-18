# Import `Blueprints` From Modules & Rename Them
from .Home import Blueprints as Home
from .Dashboard import Blueprints as Dashboard

# IMPORTANT: 
# Without This App File, Import In `App/__Init__.py`
# Is `App.Routes.Home import Blueprints as Home`