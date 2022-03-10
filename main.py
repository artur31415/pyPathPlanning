import math
import pygame
from random import *

pygame.init()
pygame.font.init()

# seed random number generator
#seed(1)
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

current_path = [(35, 35)]

clock = pygame.time.Clock()
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

    for i in range(grid_width):
        s_v_pos = (i * cell_size, 0)
        e_v_pos = (i * cell_size, height)

        s_h_pos = (0, i * cell_size)
        e_h_pos = (width, i * cell_size)

        pygame.draw.line(DISPLAY, (0, 0, 0), s_v_pos, e_v_pos)
        pygame.draw.line(DISPLAY, (0, 0, 0), s_h_pos, e_h_pos)

def draw_path(DISPLAY, path):
    last_node = None
    for path_node in path:
        path_node_color = (255, 0, 0)
        path_node_radius = cell_size / 4
        path_node_cartesian = grid_to_cartesian(path_node, cell_size)
        path_node_cartesian = (path_node_cartesian[0] + cell_size / 2, path_node_cartesian[1] + cell_size / 2)
        #last_node_cartesian = grid_to_cartesian(path_node, cell_size)
        if last_node != None:
            pygame.draw.line(DISPLAY, path_node_color, last_node, path_node_cartesian, 2)
        else:
            path_node_color = (0, 0, 255)
            path_node_radius = cell_size / 2
        last_node = path_node_cartesian

        pygame.draw.circle(DISPLAY, path_node_color, path_node_cartesian, path_node_radius)

def is_node_free(path_node, world_grid):
    return world_grid[int(path_node[0])][int(path_node[1])] == 0

def grid_to_cartesian(path_node, factor):
    return (path_node[0] * factor, path_node[1] * factor)
################################################################################################
#                                           MAIN LOOP
################################################################################################

init_grid()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    last_node = current_path[-1]
    while(True):
        new_node = (last_node[0] + randint(-1, 1), last_node[1] + randint(-1, 1))
        new_node_cartesian = grid_to_cartesian(new_node, cell_size)
        if new_node_cartesian[0] >= 0 and new_node_cartesian[0] <= width and new_node_cartesian[1] >= 0 and new_node_cartesian[1] <= height and not (new_node in current_path) and is_node_free(new_node, grid):
            current_path.append(new_node)
            #print("new_node = ", str(new_node))
            break

    ##################################################################
    # DRAW CODE
    ##################################################################

    # textsurface = myfont.render('Ticks = ' + str(ticks), False, (0, 0, 0))
    # screen.blit(textsurface, (0, 0))

    draw_grid(screen)
    draw_path(screen, current_path)
    ##################################################################
    # Flip the display
    ##################################################################
    pygame.display.flip()

    clock.tick(10)
    

# Done! Time to quit.
pygame.quit()