import pygame
import constant


class Screen:
    def __init__(self):
        self.screen = pygame.Surface(constant.SIZE)


class MenuScreen(Screen):
    def __init__(self):
        super().__init__()

    def draw_menu(self):
        self.screen.blit(self.screen, constant.SIZE)

    def draw_bottom(self):
        pass

    def hover_bottom(self):
        pass

    def click_bottom(self):
        pass


class GameScreen(Screen):
    pass
