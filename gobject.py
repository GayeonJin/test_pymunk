#!/usr/bin/python

import pygame
import pymunk
import pymunk.pygame_util

class retangle_object :
    def __init__(self, pos, width = 20, height= 20) :
        self.body = pymunk.Body(1, 1666)
        self.body.position = pos
        
        self.shape = pymunk.Poly.create_box(self.body, (width, height))

class circle_object :
    def __init__(self, pos, radius = 10) :
        self.body = pymunk.Body(1, 1666)
        self.body.position = pos

        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = .9

class triangle_object :
    def __init__(self, pos, vertices = [(0, 0), (30, 0), (15, 30)]) :
        self.body = pymunk.Body(1, 1666)
        self.body.position = pos                    
        
        self.shape = pymunk.Poly(self.body, vertices)
        self.shape.friction = 0.5
        self.shape.collision_type = 1
        self.shape.density = 0.1

class ball :
    def __init__(self, pos, radius = 10) :
        self.body = pymunk.Body()
        self.body.position = pos

        self.shape = pymunk.Circle(self.body, radius)
        self.shape.density = 1
        self.shape.elasticity = 1
        self.shape.collision_type = 1

    def set_velociy(self, vel_x, vel_y) :
        self.body.velocity = (vel_x, vel_y)

if __name__ == '__main__' :
    print('pymunk object')