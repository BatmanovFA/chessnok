import pygame
import sys
import constant

class Event:
    def choose_event(self, event_1):
        if event_1.type == pygame.QUIT:
            self.quit()

        if event_1.type == pygame.MOUSEMOTION:
            pass

    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()


pygame.init()

screen = pygame.display.set_mode(constant.SIZE)

events = Event()

while True:
    for event in pygame.event.get():
        events.choose_event(event)
