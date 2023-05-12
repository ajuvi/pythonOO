import pygame

class Globals:

    #velocitat del joc
    FPS = 4
    incrFPS = 0.25
    
    #dimensions de la finestra
    screen_width=800
    screen_height=600

    #nombre de files i de columnes
    grid_rows=40
    grid_columns=30

    #dimensions de cada tile (cuadrat)
    tile_width = screen_width/grid_rows
    tile_height = screen_height/grid_columns
