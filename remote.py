from re import S
import sys

from messages import msgs
from openthedoorfunc import *
from consoleColors import bcolors as c
from ringGUI import *
from actions import action
from termcolor import colored

import os
import subprocess

remote = True
realMode = False

print(c.red + msgs.msg3)
print(c.green + c.bol + 'commands:')
print(c.cyan + 'a = open garage doors, ' + c.blue + 'b = ring doorbell,\n' + c.green + 'c = start sonos alert system, ', c.red + 'exit = exit program')

while True: 
    while remote and realMode == False:
        print(colored('enter command: ', 'magenta'))
        inputCmd = input()
        if inputCmd == 'a':
            print(c.BOLD + 'one moment please...')
            action().openGDTest()
            print('\n')

        if inputCmd == 'b':
            print(c.BOLD + 'one moment please...')
            action().ringAllTest()
            print('\n')

        if inputCmd == 'c':
            action().checkAlerts()
            action().inProgress()

        if inputCmd == 'd':
            action().inProgress()
            print('\n')
        
        if inputCmd == 'real mode on':
            realMode = True
            print('\n')

        if inputCmd == 'exit':
            print(c.red + 'are you sure?' + c.green +  ' (y/n)')
            ans = input()
            if ans == 'y':
                sys.exit()
            elif ans == 'n':
                print('not exited.')
            elif ans == '':
                sys.exit()
            else:
                print(f"error: incorrect input '{ans}'")

# --------
# real mode
# --------
    if realMode == True:
        print(colored('REAL MODE', 'red'))

    while remote and realMode:
        print(colored('(REAL)', 'red'), colored('enter command: ', 'magenta'))
        inputCmd = input()
        if inputCmd == 'a':
            action().openGD()
            print('\n')

        if inputCmd == 'b':
            action().ringAll()
            print('\n')

        if inputCmd == 'c':
            action().checkAlerts()
            action().inProgress()

        if inputCmd == 'd':
            action().inProgress()
            print('\n')
        
        if inputCmd == 'real mode off':
            print('\n')
            realMode = False

        if inputCmd == 'exit':
            print(c.red + 'are you sure?' + c.green +  ' (y/n)')
            ans = input()
            if ans == 'y':
                sys.exit()
            elif ans == 'n':
                print('not exited.')
            elif ans == '':
                sys.exit()
            else:
                print(f"error: incorrect input '{ans}'")
