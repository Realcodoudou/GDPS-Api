import os # Imports the os lib. Used to install the required libs if not installed
# Checking if libs are installed or not
import math
import datetime,base64
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
              p = f"targetAccountID={user}&secret=Wmfd2893gb7" 
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
                    "accid": acccid,
                    "Username": user
                }
                Things = True
                break
    if Things == False:
        return "User doesn't exist."
    else:
        return Response
def level(connection,cursor,level:int):
    LevelExists = False
    script = "SELECT * FROM `levels`"
    cursor.execute(script)
    rows = cursor.fetchall()
    for row in rows:
            if row[3] == level:
                LvlPass = str(row[10])
                LvlPass = LvlPass[1:]
                Objects = int(row[14])
                Stars = int(row[26])
                Song = int(row[13])
                Length = int(row[7])
                if Length == 0:
                        Length = "Tiny"
                elif Length == 1:
                        Length = "Short"
                elif Length == 2:
                        Length = "Medium"
                elif Length == 3:
                        Length = "Long"
                elif Length == 4:
                        Length = "XL"
                UploadDate = int(row[27])
                UploadDate = datetime.datetime.fromtimestamp(UploadDate)
                UploadDate = f"{UploadDate.strftime('%m')}/{UploadDate.strftime('%d')}/{UploadDate.strftime('%Y')}"
                ReuploadOrNot = int(row[38])
                Thing = bytes(row[5],'utf-8')
                DecodedDesc = base64.b64decode(Thing).decode()
                Things = True
                Response = {
                    "levelpass": LvlPass,
                    "Objects": Objects,
                    "Stars": Stars,
                    "Length": Length,
                    "SongId": Song,
                    "UploadDate": UploadDate,
                    "Reuploaded": bool(ReuploadOrNot),
                    "Desc": DecodedDesc,
                    "Downloads": row[22],
                    "Author": row[2],
                    "Likes": row[23],
                    "Coins": row[15],
                    "Name": row[4]
                }
    if not Things == True:
        return "Level doesn't exist."
    else:
        return Response
