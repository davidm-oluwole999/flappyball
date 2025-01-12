import pygame, pgzrun
from random import randint

TITLE= "Flappy Ball"
WIDTH= 800
HEIGHT= 600
GRAVITY= 4000

class Ball:
    def __init__(self, x, y, r, c):
        self.x= x
        self.y= y
        self.vx= 100
        self.vy= 0
        self.radius= r
        self.c= c
    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, self.c)

ball= Ball(100, 100, 40, "blue")
ball2= Ball(500,400, 80, "pink")


def draw():
    screen.clear()
    ball.draw()
    ball2.draw()

def update(dt):
    cv= ball.vy
    ball.vy+= GRAVITY* dt
    ball.y+= (cv+ ball.vy)* 0.5* dt
    if ball.y> HEIGHT- ball.radius:
        ball.y= HEIGHT-ball.radius
        ball.vy= -ball.vy* 0.9
    ball.x+= ball.vx* dt
    if ball.x< ball.radius or ball.x> WIDTH- ball.radius:
        ball.vx= -ball.vx

def on_key_down(key):
    if key == keys.SPACE:
        ball.vy= -500








pgzrun.go()