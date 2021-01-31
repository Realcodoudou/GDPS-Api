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
def banuser(connection,cursor,user):
    script = f"UPDATE `users` SET `isBanned` = '1' WHERE `users`.`userName` = '{user}';"
    cursor.execute(script)
    connection.commit()
    print("Banned")
def unbanuser(connection,cursor,user):
    script = f"UPDATE `users` SET `isBanned` = '0' WHERE `users`.`userName` = '{user}';"
    cursor.execute(script)
    connection.commit()
    print("Unbanned")
def cbanuser(connection,cursor,user):
    script = f"UPDATE `users` SET `isCreatorBanned` = '1' WHERE `users`.`userName` = '{user}';"
    cursor.execute(script)
    connection.commit()
    print("Creator Banned")
def cunbanuser(connection,cursor,user):
    script = f"UPDATE `users` SET `isCreatorBanned` = '0' WHERE `users`.`userName` = '{user}';"
    cursor.execute(script)
    connection.commit()
    print("Creator Unbanned")
