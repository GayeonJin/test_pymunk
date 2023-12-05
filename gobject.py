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
    def __init__(self, pos, mass = 10, radius = 10) :
        inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
        self.body = pymunk.Body(mass, inertia)
        self.body.position = pos

        self.shape = pymunk.Circle(self.body, radius)
        self.shape.density = 1
        self.shape.elasticity = 1
        self.shape.collision_type = 1

    def set_elasticity(self, elasticity, friction) :
        self.shape.elasticity = elasticity
        self.shape.friction = friction

    def set_velociy(self, vel_x, vel_y) :
        self.body.velocity = (vel_x, vel_y)

class wall :
    def __init__(self, pos1, pos2, collision_type = None, radius = 2) :
        self.body = pymunk.Body(body_type = pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, pos1, pos2, radius)
        self.shape.elasticity = 1
        if collision_type != None :
            self.shape.collision_type = collision_type

if __name__ == '__main__' :
    print('pymunk object')