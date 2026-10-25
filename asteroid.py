import pygame
import random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle: float = random.uniform(20, 50)
        first_move: pygame.Vector2 = self.velocity.rotate(angle)
        second_move: pygame.Vector2 = self.velocity.rotate(-angle)
        log_event("asteroid_split")
        new_radius: float = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid: Asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid: Asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = first_move * 1.2
        second_asteroid.velocity = second_move * 1.2
