import math
import pygame
from random import *

pygame.init()
pygame.font.init()

# seed random number generator
seed(1)
################################################################################################
#                                           VARIABLES
################################################################################################
width = 700
height = 700

screen = pygame.display.set_mode([width, height])

myfont = pygame.font.SysFont('Comic Sans MS', 20)

running = True


ticks = 0


grid = []
grid_width = 70
grid_height = 70

cell_size = 10

current_path = []
################################################################################################
#                                           FUNCTIONS
################################################################################################
def map(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

def init_grid():
    grid.clear()

    for i in range(grid_width):
        grid.append([])
        for j in range(grid_height):
            grid_value = 0
            if randint(0, 100) < 33:
                grid_value = randint(0, 1)

            grid[i].append(grid_value)

def draw_grid(DISPLAY):
    for i in range(grid_width):
        for j in range(grid_height):
            pixel = 255 * (1 - grid[i][j])
            pygame.draw.rect(DISPLAY, (pixel, pixel, pixel), (i * cell_size, j * cell_size, cell_size, cell_size))

def draw_path(DISPLAY, path):
    last_node = None
    for path_node in path:
        if last_node != None:
            pygame.draw.line(DISPLAY, (255, 0, 0), last_node, path_node, 2)
        last_node = path_node

        pygame.draw.circle(DISPLAY, (255, 0, 0), path_node, cell_size / 2)
################################################################################################
#                                           MAIN LOOP
################################################################################################

init_grid()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ##################################################################
    # DRAW CODE
    ##################################################################
    

    # textsurface = myfont.render('Ticks = ' + str(ticks), False, (0, 0, 0))
    # screen.blit(textsurface, (0, 0))

    draw_grid(screen)
    ##################################################################
    # Flip the display
    ##################################################################
    pygame.display.flip()
    

# Done! Time to quit.
pygame.quit()