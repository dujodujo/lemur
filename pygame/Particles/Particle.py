from System import*

import pygame
from pygame.locals import*

import math
import random

class Particle:
    def __init__(self, x, y, angle = 0, duration = 500):
        self.start_x = x
        self.start_y = y
        self.duration = duration
        self.velocity = 0.01
        self.angle = angle
        self.time = 0

    def reset(self, position = None):
        if position:
            self.start_x, self.start_y = position
        self.x, self.y = self.start_x, self.start_y

    def move(self):
        self.time += pygame.time.get_ticks() * 0.05
        self.x = self.start_x + (math.cos(self.angle) * self.velocity * pygame.time.get_ticks())
        self.y = self.start_y + (math.sin(self.angle) * self.velocity * pygame.time.get_ticks())

class ParticleSystem:
    particles = dict()
    search_path = os.path.join('data', 'particles')

    def __init__(self, image, num_particles, position, rotation = 3):
        if ParticleSystem.particles[image]:
            self.image = ParticleSystem.particles[image]
        else:
            self.image = ImageObject(Texture(os.path.join(ParticleSystem.search_path, 'star.png')))

        self.image.set_scale(0.25, 0.25)
        if rotation == 1:
            self.particles = [Particle(position[0], position[1], random.randint(-90, 90))
                for i in range(num_particles)]
        elif rotation == 2:
            self.particles = [Particle(position[0], position[1], random.randint(-180, 180))
                for i in range(num_particles)]
        elif rotation == 3:
            self.particles = [Particle(position[0], position[1], random.randint(0, 90))
                for i in range(num_particles)]


    def reset(self, position = None):
        for particle in self.particles:
            particle.reset(position)

    def draw(self):
        for particle in self.particles:
            particle.move()
            if particle.time >= particle.duration:
                alpha = (particle.duration/particle.time)
            else:
                alpha = 1.0
            self.image.set_position(particle.x, particle.y)
            self.image.set_color((1,1,1, alpha))
            self.image.draw()

    @classmethod
    def load_particle_sprites(cls):
        for sprite in os.listdir(ParticleSystem.search_path):
            ParticleSystem.particles[sprite.split('.png')[0]] = ImageObject(Texture(
                os.path.join(ParticleSystem.search_path, sprite)))