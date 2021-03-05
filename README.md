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
print(f"{level["Name"]} has {level["Downloads"]} Downloads.") # A d1fferent w0rld has 21 Downloads.
```
Printing the docs of every function of this api:
```py
from gdps import GDPSApi
# connecting the api
gdps = GDPSApi("http://www.example.com") # It doesn't matter which url you put when only printing the function docs
print("set_url() function info:\n")
print(gdps.set_url.__doc__)
print("connect_db() function info:\n")
print(gdps.connect_db.__doc__)
print("ban_user() function info:\n")
print(gdps.ban_user.__doc__)
print("unban_user() function info:\n")
print(gdps.unban_user.__doc__)
print("creator_ban_user() function info:\n")
print(gdps.creator_ban_user.__doc__)
print("creator_unban_user() function info:\n")
print(gdps.creator_unban_user.__doc__)
print("get_user() function info:\n")
print(gdps.get_user.__doc__)
print("create_account() function info:\n")
print(gdps.create_account.__doc__)
print("get_gauntlet() function info:\n")
print(gdps.get_gauntlet.__doc__)```
