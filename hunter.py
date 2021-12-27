import pygame

from behaviours import Creature


class Hunter(Creature):
    MOVING_FORCE = 300
    BULLET_SPEED = 500
    SHOOT_DISTANCE = 400

    BULLET_SPREAD = 3  # in degrees

    def __init__(self, pos):
        super().__init__(
            pos=pos,
            radius=7,
            color=(204, 0, 0)
        )

    def update(self, objs, dt):

        super().update(dt)

    def move(self, direction):
        if direction.length() > 0:
            direction = pygame.Vector2(direction)
            direction.scale_to_length(self.MOVING_FORCE)
            self.apply_force(direction)
