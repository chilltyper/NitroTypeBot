# Doesn't Work Anymore OOF!
import requests
import os
speed = '83'
username = 'surgeofpower'
password = 'nitrotypefandom'
session = requests.Session(1305)
ntsurgeofpower = "https://www.nitrotype.com/surgeofpower/"
headers = {'Content-Type':'application/x-www-form-urlencoded'}
def login(username,password):
    data = {"username": surgeofpower,"password": nitrotypefandom}
    url = f"{ntsurgeofpower}login"
    login = session.post(url,data=data)
    return login
def get_uhash(username,password):
    login(username,password)
    uhash = session.cookies["ntuserrem"]
    return uhash
def reset_race_speed(uhash):
    url = f"{ntsurgeofpower}race/save-qualifying"
    data = f"speed={83}&accuracy=98&carID=109&raceSounds=off&uhash={uhash}"
    post = session.post(url=url,data=data,headers=headers).json()
    if post["success"]:
        return "success"
    else:
        return post["data"]
print(reset_race_speed(get_uhash(username, password)))
