# competitions/league.py
from competitions.competition import Competition

class League(Competition):
    def organize_battles(self):
        self.battles = []
        for i in range(len(self.robots)):
            for j in range(i + 1, len(self.robots)):
                self.battles.append((self.robots[i], self.robots[j]))

    def start(self):
        self.organize_battles()
        for battle in self.battles:
            result = self.simulate_battle(battle[0], battle[1])
            self.add_result(result)

    def simulate_battle(self, robot1, robot2):
        # Aquí iría la lógica de la batalla entre robot1 y robot2.
        # Como ejemplo, podemos decidir el ganador aleatoriamente.
        import random
        winner = random.choice([robot1, robot2])
        print(f"{winner.name} ganó la batalla entre {robot1.name} y {robot2.name}")
        return winner.name
