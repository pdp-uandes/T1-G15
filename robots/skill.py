# robots/skill.py

class Skill:
    def __init__(self, name, trigger, trigger_value, duration, objective, effect, effect_value):
        self.name = name
        self.trigger = trigger
        self.trigger_value = trigger_value
        self.duration = duration
        self.objective = objective
        self.effect = effect
        self.effect_value = effect_value
        self.active_turns = 0
        self.activation_count = 0  # Contador de activaciones

    def activate(self, condition):
        if condition == self.trigger and self.active_turns == 0:
            self.active_turns = self.duration
            self.activation_count += 1  # Incrementar el contador de activaciones
            return True
        return False

    def apply_effect(self):
        if self.active_turns > 0:
            self.active_turns -= 1
            return self.effect, self.effect_value
        return None, None
