# GDPS-Api

GDPS-Api is an api where you can fetch/manage your gdps using python

Examples:

```py
from gdps import GDPSApi

# connecting the api

gdps = GDPSApi("example.com")

# Fetching profile stats

user = gdps.get_user("codoudou") # returns a dict object of the user

print(user) # Prints the json table
print(f"{user['Username']} has {user['stars']} Stars.") # Codoudou has 150 stars

# Fetching level stats
level = gdps.get_level(214) # level id is 213

print(level) # print the dict
print(level["Downloads"]) # A d1fferent w0rld has 21 Downloads.
```
