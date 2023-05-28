import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass
    def move(self, dirnx, dirny):
        pass
    def draw(self, surface, eyes=False):
        pass

class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        # The head of the snake is equal to the cube at the given position
        self.head = cube(pos)
        # Append to the body the head
        self.body.append(self.head)
        # Direction for moving our snake, can only be moving in one direction at the same time
        self.dirnx = 0
        self.dirny = 1
    def move(self):
        for event in pygame.event.get()L
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    # Add a key which is the current position of the head of our snake, equal to what direction we turned
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    # Add a key which is the current position of the head of our snake, equal to what direction we turned
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    # Add a key which is the current position of the head of our snake, equal to what direction we turned
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    # Add a key which is the current position of the head of our snake, equal to what direction we turned
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        # I for index and c for cube. Get the cube object in self.body
        for i, c in enumerate(self.body):
                # Grab the cube object position and see if that position is in the turn list
                p = c.pos[:]
                if p in self.turns:
                    # The turn where snake will be moving is equal to the turns list at that index
                    turn = self.turns[p]
                    # Move in direction x and direction y
                    c.move(turn[0],turn[1])
                    # If snake is on the last cube remove the turn
                    if i == len(self.body)-1:
                        self.turns.pop(p)
                else:
                    # Checking whether or not we've reached the edge of the screen
                    # If we're moving left and the exposition of the cub is less than or equal to 0, change the position so that is goes to the right side of the screen
                    if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                    elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0, c.pos[1])
                    elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                    elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                    else: c.move(c.dirnx,c.dirny)
    
def drawGrid(w, rows, surface):
    # Figure out how big each square in the grid is gonna be
    # Make sure we don't get large decimal number
    sizeBtwn = w // rows
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
    # Draw two lines every loop of the for loop. Arguments are the start position of the line amd the end position
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x,w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redrawWindow(surface):
    global rows, width
    # Fill screen with black color
    surface.fill((0, 0, 0))
    drawGrid(width, rows, surface)
    pygame.display.update()


# Main Func
def main():
    global width, rows
    width = 500
    # If you want to make it harder set it to 10 there won't be enough room for the snake to move around
    rows = 20
    # Height not necessary we are just gonna draw a square
    surface = pygame.display.set_mode((width, width))
    # Snake color and position
    s = snake((255, 0, 0), (10, 10))
    flag = True
    # Clock object to make sure the game doesn't run at more than 10 games per second, snake will move ten blocks in one second
    clock = pygame.time.Clock()
    while flag:
        # Delay for 50 milliseconds so the program doesn't run too fast
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)
    pass