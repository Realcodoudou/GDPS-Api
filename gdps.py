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
def createaccount(connection,cursor,username,pw):
    url = f"{url}/accounts/registerGJAccount.php" 
    p = f"userName={username}&password={pw}&email=nah@nah.f"
    p = p.encode() 
    data = urlopen(url,p).read().decode()
    url = f"{url}/accounts/loginGJAccount.php" 
    p = f"udid=nz&userName={username}&password={pw}"
    p = p.encode() 
    data1 = urlopen(url,p).read().decode()
    return data1
def getGauntlet(connection,cursor,gauntlet):
    def nametogauntlettype(name:str):
        if name.lower() == "fire":
            return 1
        elif name.lower() == "ice":
            return 2
        elif name.lower() == "poison":
            return 3
        elif name.lower() == "shadow":
            return 4
        elif name.lower() == "lava":
            return 5
        elif name.lower() == "bonus":
            return 6
        elif name.lower() == "chaos":
            return 7
        elif name.lower() == "demon":
            return 8
        elif name.lower() == "time":
            return 9
        elif name.lower() == "crystal":
            return 10
        elif name.lower() == "magic":
            return 11
        elif name.lower() == "spike":
            return 12
        elif name.lower() == "monster":
            return 13
        elif name.lower() == "doom":
            return 14
        elif name.lower() == "death":
            return 15
        elif name.lower() == "unknown":
            return 16
        else:
            return 100
    script = "SELECT * FROM `gauntlets`"
    cursor.execute(script)
    rows = cursor.fetchall()
    for row in rows:
        if row[0] == nametogauntlettype(gauntlet):
            Response = {
                "Level 1": row[1],
                "Level 2": row[2],
                "Level 3": row[3],
                "Level 4": row[4],
                "Level 5": row[5]
            }
            break
    return Response
