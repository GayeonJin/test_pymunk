#!/usr/bin/python

import os
import sys
import csv

import pygame
import pymunk
import pymunk.pygame_util
import random
from time import sleep

from gresource import *

TITLE_STR = "Test PyMunk"

INFO_HEIGHT = 40
INFO_OFFSET = 10
INFO_FONT = 14

def draw_info() :
    font = pygame.font.SysFont('Verdana', INFO_FONT)
    info = font.render('F1/F2 : Load/Save field file    space : toggle', True, COLOR_BLACK)

    pygame.draw.rect(gctrl.surface, COLOR_PURPLE, (0, gctrl.height - INFO_HEIGHT, gctrl.width, INFO_HEIGHT))
    gctrl.surface.blit(info, (INFO_OFFSET * 2, gctrl.height - 2 * INFO_FONT - INFO_OFFSET)) 

def draw_message(str) :
    font = pygame.font.Font('freesansbold.ttf', 40)
    text_suf = font.render(str, True, COLOR_BLACK)
    text_rect = text_suf.get_rect()
    text_rect.center = ((gctrl.width / 2), (gctrl.height / 2))

    gctrl.surface.blit(text_suf, text_rect)
    pygame.display.update()
    sleep(2)

def terminate() :
    pygame.quit()
    sys.exit()
      
def test() :
    global clock

    pygame.init()
    clock = pygame.time.Clock()

    pad_width = 640
    pad_height = 480

    gctrl.set_surface(pygame.display.set_mode((pad_width, pad_height)))
    pygame.display.set_caption(TITLE_STR)

    space = pymunk.Space()
    space.gravity = 0, 980

    draw_options = pymunk.pygame_util.DrawOptions(gctrl.surface)

    '''
    static =[
                pymunk.Segment(space.static_body, (-5, 0), (-5, 650), 5),
                pymunk.Segment(space.static_body, (-5, 650), (650, 650), 5),
                pymunk.Segment(space.static_body, (650, 650), (650, -5), 5),
                pymunk.Segment(space.static_body, (-5, -5), (650, -5), 5),
            ]
    '''
    boarder_width = 5
    sx = 0 - boarder_width
    sy = 0 - boarder_width
    ex = pad_width + boarder_width
    ey = pad_height + boarder_width
    static =[
                pymunk.Segment(space.static_body, (sx, sy), (sx, ey), boarder_width),
                pymunk.Segment(space.static_body, (sx, ey), (ex, ey), boarder_width),
                pymunk.Segment(space.static_body, (ex, ey), (ex, sy), boarder_width),
                pymunk.Segment(space.static_body, (sx, sy), (ex, sy), boarder_width),
                pymunk.Segment(space.static_body, (sx+100, sy+80), (ex-100, ey-80), boarder_width),
            ]

    for s in static:
        s.collision_type = 1
    space.add(*static)

    timeStep = 1.0 / 60

    running = True
    while running:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False
                continue

            if event.type == pygame.MOUSEBUTTONDOWN :
                l_button, wheel, r_button = pygame.mouse.get_pressed()
            if event.type == pygame.MOUSEBUTTONUP :
                mouse_pos = pygame.mouse.get_pos()

                body = pymunk.Body(1, 1666)
                body.position = mouse_pos

                if l_button == True :
                    shape = pymunk.Poly.create_box(body, (20, 20))
                elif r_button :
                    shape = pymunk.Circle(body, 10)
                    shape.elasticity = .9
                elif wheel :
                    vertices = [(0, 0), (30, 0), (15, 30)]
                    shape = pymunk.Poly(body, vertices)
                    shape.friction = 0.5
                    shape.collision_type = 1
                    shape.density = 0.1

                space.add(body, shape)

        gctrl.surface.fill(COLOR_BLACK)

        space.debug_draw(draw_options)

        space.step(timeStep)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__' :
    test()
