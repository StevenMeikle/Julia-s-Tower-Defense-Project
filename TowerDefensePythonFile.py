import pygame
from pygame import *

#Initialize pygame
pygame.init()

#We are creating variables to define the dimensions of the window, separately.

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 400
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

#Create window
GAME_WINDOW = display.set_mode(WINDOW_RES)
#900 pixels for the width, 400 pixels for the height

display.set_caption("Tower Defense Game")

pizza_img = image.load(" ")
#Convert the image to a surface
pizza_surf = Surface.convert_alpha(cat_img)

VAMPIRE_PIZZA = transform.scale(cat_surf, (100, 100))

#Display the enemy image to the screen
GAME_WINDOW.blit(VAMPIRE_PIZZA, (900, 400))

draw.circle(GAME_WINDOW, (0, 0, 255), (925, 425), 25, 0)
draw.rect(GAME_WINDOW, (160, 82, 45), (895, 395, 110, 110), 5)
draw.rect(GAME_WINDOW, (160, 82, 45), (895, 295, 110, 110), 0)

#A tuple is data type that contains data separated by commas, and contained within parentheses
#Start Main Game Loop
game_running = True

#Boolean: Is true or false values.

while game_running:
    for event in pygame.event.get():
        #Exit the loop on quit
        if event.type == QUIT:
            game_running = False
        display.update()

pygame.quit()
