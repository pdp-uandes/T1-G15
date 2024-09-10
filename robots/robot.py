# robots/robot.py

class Robot:
    def __init__(self, name, energy, attacks, skills):
        self.name = name
        self.energy = energy
        self.attacks = attacks
        self.skills = skills

    def __str__(self):
        return f"Robot(name={self.name}, energy={self.energy})"

    def take_damage(self, amount):
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0

    def is_alive(self):
        return self.energy > 0
