def redrawWindow(surface):
    # Fill screen with black color
    win.fill((0, 0, 0))
    drawGrid(surface)
    pygame.display.update()


# Main Func
def main():
    width = 500
    height = 500
    # If you want to make it harder set it to 10 there won't be enough room for the snake to move around
    rows = 20
    win = pygame.display.set_mode((width, height))
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