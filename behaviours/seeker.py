from .creature import Creature


class Seeker(Creature):

    def seek(self, target):
        desired = target - self.pos
        desired.scale_to_length(self.max_speed)

        steer = desired - self.vel
        steer = self.vec_limit(steer, self.max_force)
        return steer

    def arrive(self, target, arrive_radius=300):
        desired = target - self.pos
        dist = desired.length()

        if dist < arrive_radius:
            speed = (dist/arrive_radius)*self.max_speed
            desired.scale_to_length(speed)
        else:
            desired.scale_to_length(self.max_speed)

        steer = desired - self.vel
        print('Force before', steer.length())
        steer = self.vec_limit(steer, self.max_force)
        print('Force after', steer.length())
        return steer