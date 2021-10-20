import pygame
import sys
from pygame.locals import *

from openthedoorfunc import *

from ringGUI import *

from consoleColors import bcolors as c


class action():
    def openGDTest(self):
        openGarageDoorTest()

    def openGD(self):
        openGarageDoor()

    def ringAllTest(self):
        ring_all_test()

    def ringAll(self):
        ring_all()

    def inProgress(self):
        print('not available yet, in progress.')

    def notWorking(self):
        print('this feature is currently unavailable.')
    
    def closeGD(self):
        closeGarageDoor()

    def checkAlerts(self):
        pass
