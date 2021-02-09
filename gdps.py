import os # Imports the os lib. Used to install the required libs if not installed
# Checking if libs are installed or not
import math
from urllib.request import urlopen,Request 
url = ""
try:
    import pymysql
except:
    os.system("pip install pymysql") # Installs the required libs if not installed
def login(host,user,pw):
    connection = pymysql.connect(host=f"{host}",user=f"{user}",passwd=f"{pw}",database=f"{user}") # Connects to the database
    cursor = connection.cursor() # Gets the cursor
    return connection,cursor # Returns the tuple
def seturl(url1):
    global url
    url = url1
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
def profile(connection,cursor,user):
    def users(user,url):
              Thing= []
              url = f"{url}/getGJUserInfo20.php" 
              print("ok")
              p = f"targetAccountID={user}&secret=Wmfd2893gb7" 
              print("ok")
              p = p.encode() 
              data = urlopen(url,p).read().decode()
              if data == "-1": 
                return "User Fetch Failed"
              else:
                  data = data.split('|')
                  try:
                      for i in range(0,len(data)):
                        data1 = data[i].split(":")
                        Thing = data1
                      return Thing
                  except IndexError:
                      return f"ERROR: There was an error in the code."
    Friends = ""
    script = "SELECT * FROM `accounts`"
    cursor.execute(script)
    rows = cursor.fetchall()
    for row in rows:
            if row[0]==user:
                acccid = row[4]
                Friends = row[19]
                break
    script = "SELECT * FROM `users`"
    cursor.execute(script)
    rows = cursor.fetchall()
    Things = False
    for row in rows:
            if row[3] == user and not row[3] == "Player" and not row[3] == "":
                Stars = row[4]
                Demons = row[5]
                userId = row[1]
                OfficialCoins = row[10]
                UserCoins = row[11]
                Diamonds = row[25]
                CP = int(math.floor(row[22]))
                UserData = users(acccid,url)
                RankLb = UserData[len(UserData)-13]
                Mod = UserData[len(UserData)-1]
                Response = {
                    "stars": Stars,
                    "demons": Demons,
                    "userId": userId,
                    "userCoins": UserCoins,
                    "diamonds": Diamonds,
                    "CP": CP,
                    "rank": RankLb,
                    "mod": Mod,
                    "friends": Friends,
                    "accid": acccid
                }
                Things = True
                break
    if Things == False:
        return "User doesn't exist."
    else:
        return Response
