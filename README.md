# GDPS-Api

GDPS-Api is an api where you can fetch/manage your gdps using python

Examples:

```py
# Fetching profile stats
import gdps
logindata=gdps.login("Your domain","your entire database username here","your database password here")
connection = logindata[0]
cursor = logindata[1]
gdps.seturl("Url to the server (or a place with a bunch of php files including getGJScores20.php)")
user = gdps.profile(connection,cursor,"codoudou") # Should print a json string if you did everything correct
print(user) # Prints the json table
print(f"{user['Username']} has {user['stars']} Stars.) # Codoudou has 150 stars
# Fetching level stats
level = gdps.level(connection,cursor,214)
print(level) # Prints the entire json table
print(f"{level['Name']} has {level['Downloads']} Downloads.") # A d1fferent w0rld has 21 Downloads.
```
