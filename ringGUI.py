import json
import getpass
from pathlib import Path

from time import sleep

from ring_doorbell import Ring, Auth
from oauthlib.oauth2 import MissingTokenError

cache_file = Path("token.cache")

from consoleColors import bcolors as c


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


def playring(choice):
    for dev in list(devices['stickup_cams'] + devices['chimes'] + devices['doorbots']):
        dev.update_health_data()
        dev.volume = 5
        if dev.family == 'chimes':
            dev.test_sound(kind=choice)


def ring_all():
    for dev in list(devices['stickup_cams'] + devices['chimes'] + devices['doorbots']):
        dev.update_health_data()
        # print('Volume:     %s' % dev.volume)
        dev.volume = 5
        # print('Volume:     %s' % dev.volume)

        # play dev test sound
        if dev.family == 'chimes':
            dev.test_sound(kind='ding')
            dev.test_sound(kind='motion')
            print(c.OKGREEN + "[ring api] " + c.OKCYAN + "Successfully Rung Braden's Doorbell.")


def check_alerts():
    while True:
        ringcheck = Ring(auth)
        ringcheck.update_dings()
        print(ringcheck.dings_data)
        sleep(5)


testers = 0

amnt = 0
def ring_all_test():
    global amnt
    amnt = 0
    for dev in list(devices['stickup_cams'] + devices['chimes'] + devices['doorbots']):
        dev.update_health_data()
        # print('Volume:     %s' % dev.volume)
        dev.volume = 5
        # print('Volume:     %s' % dev.volume)

        # play dev test sound
        if dev.family == 'chimes':
            # dev.test_sound(kind='ding')
            # dev.test_sound(kind='motion')
            if amnt <= 0:
                amnt += 1
                print(c.OKGREEN + "[ring api] " + c.OKCYAN + f"Successfully Rung Braden's Doorbell. (test)")


def ring_ring():
    for dev in list(devices['stickup_cams'] + devices['chimes'] + devices['doorbots']):
        dev.update_health_data()
        # print('Volume:     %s' % dev.volume)
        dev.volume = 5
        # print('Volume:     %s' % dev.volume)

        # play dev test sound
        if dev.family == 'chimes':
            dev.test_sound(kind='ding')
            print(c.OKGREEN + "[ring api] " + c.OKCYAN + "Successfully Rung Braden's Doorbell.")


def ring_chimes():
    for dev in list(devices['stickup_cams'] + devices['chimes'] + devices['doorbots']):
        dev.update_health_data()
        # print('Volume:     %s' % dev.volume)
        dev.volume = 5
        # print('Volume:     %s' % dev.volume)

        # play dev test sound
        if dev.family == 'chimes':
            dev.test_sound(kind='motion')
            print(c.OKGREEN + "[ring api] " + c.OKCYAN + "Successfully Rung Braden's Doorbell.")


def ring_voice():
    pass
