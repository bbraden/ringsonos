import pygame
import sys
from pygame.locals import *

from openthedoorfunc import *

from ringGUI import *

from consoleColors import bcolors as c


def main():
    pygame.init()

    DISPLAY = pygame.display.set_mode((500, 400), 0, 32)

    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)

    DISPLAY.fill(WHITE)

    font_path = "/Users/braden/vs/fonts/Quick Zap.ttf"
    font_size = 25
    myfont = pygame.font.Font(font_path, font_size)

    label = myfont.render("Click Button To Open Garage Doors", True, (0, 0, 0))
    x = DISPLAY.blit(label, (50, 100))

    # render text

    while True:

        ringButton = pygame.draw.rect(DISPLAY, BLUE, (150, 150, 50, 50))

        garageButton = pygame.draw.rect(DISPLAY, BLUE, (300, 150, 50, 50))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if ringButton.collidepoint(pygame.mouse.get_pos()):
                    ring_all_test()
                if garageButton.collidepoint(pygame.mouse.get_pos()):
                    openGarageDoorTest()

        pygame.time.delay(10)
        pygame.display.update()


main()
