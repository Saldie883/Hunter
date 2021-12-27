from abc import ABC
from creature import Creature
import pygame


class Runner(Creature, ABC):

    def run_away(self, target):
        desired = target - self.pos
        desired.scale_to_length(self.max_speed)

        steer = desired - self.vel
        steer = self.vec_limit(steer, self.max_force)
        steer = -steer
        return steer

    def run_away_objs(self, objects):
        sum_vec = pygame.Vector2(0, 0)
        amount = 0

        for obj in objects:
            dist = self.pos.distance_to(obj.pos)

            if dist > 0:
                diff_vec = self.pos - obj.pos
                diff_vec.normalize_ip()
                diff_vec /= dist

                sum_vec += diff_vec
                amount += 1

        if amount > 0:
            sum_vec /= amount
            sum_vec.normalize_ip()
            sum_vec *= self.max_speed

            steer = sum_vec - self.vel
            steer = self.vec_limit(steer, self.max_force)
            return steer
        else:
            return pygame.Vector2(0, 0)
