# Format Dates As Mon Jan 31, 2022 at 11:59PM (More Options: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
def Format_Date(Date):
  # Receive a `datetime` Object
  # Use `strftime()` Method To Convert To String
  return Date.strftime('%a %b %d, %Y at %I:%M%p')

# Remove Extraneous Info From URL String
def Format_URL(URL):
  # Only Keep Domain Name (Remove Query Parameters)
  return URL.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# Correctly Pluralize Words
def Format_Plural(Amount, Word):
  # If Amount Is Greater Than 1, Pluralize
  if Amount != 1:
    return Word + 's'
  # Otherwise, Return The Word Unaltered
  return Word

# 🧪 TEST: `python App/Utilities/Filters.py`
# ➡️ RETURNS: `Mon Jul 22, 2024 at 4:09PM` ☑️
from datetime import datetime
print(Format_Date(datetime.now()))

# 🧪 TEST: `python App/Utilities/Filters.py`
# ➡️ RETURNS: `google.com` ☑️
print(Format_URL('http://google.com/test/'))
# ➡️ RETURNS: `google.com` ☑️
print(Format_URL('https://www.google.com?q=test'))

# 🧪 TEST: `python App/Utilities/Filters.py`
# ➡️ RETURNS: `Cats` ☑️
print(Format_Plural(2, 'Cat'))
# ➡️ RETURNS: `Dog` ☑️
print(Format_Plural(1, 'Dog'))