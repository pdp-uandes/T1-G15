# competitions/playoff.py
from competitions.competition import Competition

class Playoff(Competition):
    def organize_battles(self):
        self.battles = [(self.robots[i], self.robots[i + 1]) for i in range(0, len(self.robots), 2)]

    def start(self):
        while len(self.robots) > 1:
            self.organize_battles()
            winners = []
            for battle in self.battles:
                winner = self.simulate_battle(battle[0], battle[1])
                winners.append(winner)
            self.robots = winners

    def simulate_battle(self, robot1, robot2):
        import random
        winner = random.choice([robot1, robot2])
        print(f"{winner.name} ganó la batalla entre {robot1.name} y {robot2.name}")
        return winner
