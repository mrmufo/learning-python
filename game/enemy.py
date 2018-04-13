class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {dmg} points damage and have {hp} hp left".format(dmg=damage, hp=self.hit_points))
        else:
            self.lives -= 1
            print("Live lost")

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit points: {0.hit_points}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0.name}. {0.name} stomp you.".format(self))
