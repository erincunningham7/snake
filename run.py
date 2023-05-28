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