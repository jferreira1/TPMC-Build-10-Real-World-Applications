import time
from datetime import datetime as dt

hosts_temp = r".\The Python Mega Course\App3 - Websites Blocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.reddit.com", "reddit.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 14) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 19):
        print("Work time...")
        with open(hosts_temp, "r+") as file:
            content = file.read()
            for website in website_list:
                if website not in content:
                    file.write(redirect+" "+website+"\n")
                    
    else:
        with open(hosts_temp, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

        print("Fun time...")
    time.sleep(60)
        
