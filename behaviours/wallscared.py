from behaviours import Creature
import pygame


class WallScared(Creature):
    WALL_AFRAID_RADIUS = 75

    def __init__(self,
                 walls_rect=(pygame.Vector2(-450, 300), pygame.Vector2(450, -300)),
                 **kwargs):
        super().__init__(**kwargs)
        self.walls_rect = walls_rect

    def watch_out_wall(self):
        top_left = self.walls_rect[0]
        bottom_right = self.walls_rect[1]

        desired = pygame.Vector2(0, 0)
        if self.pos.x < top_left.x + self.WALL_AFRAID_RADIUS:
            desired += pygame.Vector2(self.max_speed, self.vel.y)
        elif self.pos.x > bottom_right.x - self.WALL_AFRAID_RADIUS:
            desired += pygame.Vector2(-self.max_speed, self.vel.y)

        if self.pos.y > top_left.y - self.WALL_AFRAID_RADIUS:
            desired += pygame.Vector2(self.vel.x, -self.max_speed)
        elif self.pos.y < bottom_right.y + self.WALL_AFRAID_RADIUS:
            desired += pygame.Vector2(self.vel.x, self.max_speed)

        if desired.length() > 0:
            steer = desired - self.vel
            steer = self.vec_limit(steer, self.max_force)
            steer.scale_to_length(self.max_force)
            return steer
        else:
            return pygame.Vector2(0, 0)
