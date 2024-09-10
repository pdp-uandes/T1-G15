# robots/attack.py

class Attack:
    def __init__(self, name, attack_type, objective, damage, precision, recharge):
        self.name = name
        self.attack_type = attack_type
        self.objective = objective
        self.damage = damage
        self.precision = precision
        self.recharge = recharge
        self.turns_until_ready = 0
        self.usage_count = 0  # Contador de uso

    def is_ready(self):
        return self.turns_until_ready == 0

    def use(self):
        if self.is_ready():
            self.turns_until_ready = self.recharge
            self.usage_count += 1  # Incrementar el contador de uso
            return self.damage
        else:
            return 0

    def recharge_turn(self):
        if self.turns_until_ready > 0:
            self.turns_until_ready -= 1
