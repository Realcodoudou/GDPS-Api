import os # Imports the os lib. Used to install the required libs if not installed
# Checking if libs are installed or not
try:
	import pymysql
except:
	os.system("pip install pymysql") # Installs the required libs if not installed
def login(host,user,pw):
	connection = pymysql.connect(host="{host}",user=f"{user}",passwd=f"{pw}",database=f"{user}") # Connects to the database
  cursor = connection.cursor() # Gets the cursor
	return connection,cursor # Returns the tuple
