import json
import getpass
from pathlib import Path

from time import sleep

from ring_doorbell import Ring, Auth
from oauthlib.oauth2 import MissingTokenError

cache_file = Path("token.cache")

from consoleColors import bcolors as c

from motionSonos import *

from toDictionary import *


def token_updated(token):
    cache_file.write_text(json.dumps(token))


def otp_callback():
    auth_code = input("2FA code: ")
    return auth_code


if cache_file.is_file():
    auth = Auth("MyProj/1.0", json.loads(cache_file.read_text()), token_updated)
else:
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    auth = Auth("MyProj/1.0", None, token_updated)
    try:
        auth.fetch_token(username, password)
    except MissingTokenError:
        auth.fetch_token(username, password, otp_callback())

ring = Ring(auth)
ring.update_data()

devices = ring.devices()
# print(devices)

doorbells = devices["doorbots"]
chimes = devices["chimes"]
stickup_cams = devices["stickup_cams"]

# print(doorbells)
# print(chimes)
# print(stickup_cams)

devices = ring.devices()

dataCount = 0


def check_alerts():
    print(c.yellow)
    print('input desired wait time between checks. (default 3): ')
    waitTime = input()

    w = 3
    try:
        w = int(waitTime)
    except:
        if waitTime == '':
            w = 3

    if w >= 11:
        w = 3
    if w <= 0:
        w = 3
    print(w)
    while True:
        global dataCount
        ringcheck = Ring(auth)
        ringcheck.update_dings()
        data = ringcheck.dings_data
        # print(ringcheck.dings_data)
        if data != []:
            l = str(data)
            kind = toDict(l)["kind"]
            print(c.red + "[alert] " + c.green + kind + c.yellow + " ")
            playSound()
        if data == []:
            dataCount += 1
            xx = (c.red + 'x' + c.cyan)
            print(c.cyan + f"[{xx}]" + c.blue + f' {dataCount}' + c.yellow + " ")

        sleep(3)


check_alerts()
