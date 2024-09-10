# robots/robot.py

from robots.attack import Attack
from robots.skill import Skill

class Robot:
    def __init__(self, name, energy, attacks, skills):
        self.name = name
        self.energy = energy
        self.attacks = [Attack(**attack) for attack in attacks] #uso en ambas una list comprehension para ser mas conciso
        self.skills = [Skill(**skill) for skill in skills]

    def __str__(self):
        return f"Robot(name={self.name}, energy={self.energy})"

    def take_damage(self, amount):
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0

    def is_alive(self):
        return self.energy > 0

    def choose_attack(self):
        available_attacks = [attack for attack in self.attacks if attack.is_ready()]
        if available_attacks:
            return available_attacks[0]  # aca podemos mejorar la seleccion
        return None

    def apply_skills(self, condition):
        for skill in self.skills:
            if skill.activate(condition):
                print(f"{self.name} ha activado la habilidad {skill.name}")

    def end_turn(self):
        for attack in self.attacks:
            attack.recharge_turn()
