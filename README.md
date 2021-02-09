# GDPS-Api

GDPS-Api is an api where you can fetch/manage your gdps using python

Example:

```py
# Fetching profile stats
import o
logindata=o.login("Your domain","your entire database username here","your database password here")
connection = logindata[0]
cursor = logindata[1]
o.seturl("Url to the server (or a place with a bunch of php files including getGJScores20.php)")
print(o.profile(connection,cursor,"codoudou")) # Should print a json string if you did everything correct
```
