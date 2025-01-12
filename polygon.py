import pygame

pygame.init()

screen= pygame.display.set_mode((600, 600))
screen.fill("white")
pygame.display.update()

class Polygon:
    def __init__(self, colour, dimensions):
        self.colour= colour
        self.dimensions= dimensions
        self.surface= screen
    def draw(self):
        self.drawrect= pygame.draw.rect(screen, self.colour, self.dimensions)

red= Polygon("red", (50, 400, 180, 180))

red.draw()

pygame.display.update()