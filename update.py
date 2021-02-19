import os
try:
    import requests
except:
    os.system("pip install requests")
Source = requests.get("https://raw.githubusercontent.com/Realcodoudou/GDPS-Api/main/gdps.py")
with open("gdps.py",'wb') as f:
	f.write(Source.content)
