import pygame
from pygame.locals import*

mouse_clicks = list()
finished = False

def mouse_move(position):
    global mouse_position
    display_surface = pygame.display.get_surface()
    mouse_position = (position[0]*(800/display_surface.get_width()),
        (600 - position[1]*(600/display_surface.get_height())))

def mouse_click(mouse_position):
    mouse_clicks.append(mouse_position)

def mouse_click_reset():
    mouse_clicks[:] = list()

def reset():
    mouse_click_reset()

def update():
    global finished
    while True:
        event = pygame.event.poll()
        if event.type == NOEVENT:
            break
        elif event.type == QUIT:
            finished = True
            break
        elif event.type == MOUSEMOTION:
            mouse_move(event.pos)
        elif event.type == MOUSEBUTTONDOWN:
            mouse_click(mouse_position)