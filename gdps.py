import os # Imports the os lib. Used to install the required libs if not installed
# Checking if libs are installed or not
import math
import datetime, base64, pymysql
from urllib.request import urlopen


class GDPSApi:
    def __init__(self, url: str=""):
        self.url = url
        
    def set_url(self, url: str):
        self.url = url # short for GDPSApi().url = ""
        
    def connect_db(self, host: str, user: str, password: str):
        # TODO: use async
        conn = pymysql.connect(host=host, user=user, passwd=password, database=user) # Connects to the database
        cursor = conn.cursor() # Gets the cursor
        
        self.conn = conn
        self.cursor = cursor

    def ban_user(self, username: str):
        self.cursor.execute("""UPDATE `users`
                            SET `isBanned` = '1'
                            WHERE `userName` = %s;""", username) # no unsafe formats
        self.conn.commit()

    def unban_user(self, username: str):
        self.cursor.execute("""UPDATE `users`
                       SET `isBanned` = '0'
                       WHERE `userName` = %s;""", username)
        self.conn.commit()

    def creator_ban_user(self, username: str):
        self.cursor.execute("""UPDATE `users`
                            SET `isCreatorBanned` = '1'
                            WHERE `userName` = %s;""", username)
        self.conn.commit()

    def creator_unban_user(self, username: str):
        self.cursor.execute("""UPDATE `users`
                            SET `isCreatorBanned` = '0'
                            WHERE `userName` = %s;""", username)
        self.conn.commit()

    def profile(self, username: str):
        # this entire function needs to be rewritten with pep-8 standards and better code
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
        self.cursor.execute(script)
        rows = self.cursor.fetchall()
        for row in rows:
                if row[0]==username:
                    accid = row[4]
                    Friends = row[19]
                    break
        script = "SELECT * FROM `users`"
        self.cursor.execute(script)
        rows = self.cursor.fetchall()
        Things = False
        for row in rows:
                if row[3] == username and not row[3] == "Player" and not row[3] == "":
                    Stars = row[4]
                    Demons = row[5]
                    userId = row[1]
                    OfficialCoins = row[10]
                    UserCoins = row[11]
                    Diamonds = row[25]
                    CP = int(math.floor(row[22]))
                    UserData = users(accid, self.url)
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
                        "accid": accid,
                        "Username": username
                    }
                    Things = True
                    break
        if Things == False:
            return "User doesn't exist."
        else:
            return Response

    def get_level(self, level: int):
        # this entire function needs to be rewritten with pep-8 standards and better code
        LevelExists = False
        script = "SELECT * FROM `levels`"
        self.cursor.execute(script)
        rows = self.cursor.fetchall()
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
