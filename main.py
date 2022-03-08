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

move_increment = 10
orientation_increment = math.pi / 16
force_increment = 0.1


#
max_iterations = 100
upper_bound = 16
min_val = -1.9
max_val = 0.3

################################################################################################
#                                           FUNCTIONS
################################################################################################
def map(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

def draw_mandelbrot_set():
    screen.fill((255, 255, 255))
    for i in range(width):
        for j in range(height):
            a = map(i, 0, width, min_val, max_val)
            b = map(j, 0, height, min_val, max_val)

            ca = a
            cb = b

            n = 0
            z = 0

            while(n < 100):
                aa = a * a - b * b
                bb = 2 * a * b

                a = aa + ca
                b = bb + cb

                if (abs(a + b) > upper_bound):
                    break

                n += 1

            pixel_value = map(math.sqrt(n / max_iterations), 0, 1, 0, 255)

            if n == max_iterations:
                pixel_value = 0
            # else:
            #     print("pixel_value = ", str(pixel_value))

            screen.set_at((i, j), (pixel_value, pixel_value, pixel_value))
    print("calculated!")
################################################################################################
#                                           MAIN LOOP
################################################################################################

draw_mandelbrot_set()
pygame.display.flip()



while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ##################################################################
    # DRAW CODE
    ##################################################################
    

    # textsurface = myfont.render('Ticks = ' + str(ticks), False, (0, 0, 0))
    # screen.blit(textsurface, (0, 0))

    
    ##################################################################
    # Flip the display
    ##################################################################
    max_val -= 0.1
    min_val += 0.2
    print("max_val = ", str(max_val))
    draw_mandelbrot_set()
    pygame.display.flip()
    

# Done! Time to quit.
pygame.quit()