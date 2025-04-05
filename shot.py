from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
