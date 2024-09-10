# competitions/tournament.py
from competitions.competition import Competition
from competitions.playoff import Playoff
import random

class Tournament(Competition):
    def organize_battles(self):
        self.groups = [self.robots[i:i+4] for i in range(0, len(self.robots), 4)]
        self.battles = []
        for group in self.groups:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    self.battles.append((group[i], group[j]))

    def start(self):
        self.organize_battles()
        group_winners = []
        for group in self.groups:
            winners = []
            for robot in group:
                if len(group) > 1:
                    winner = self.simulate_battle(robot, random.choice([r for r in group if r != robot]))
                else:
                    winner = robot  # si solo hay un robot en el grupo, es ganador
                winners.append(winner)
            group_winners.append(max(winners, key=lambda r: winners.count(r)))

        playoff = Playoff(group_winners)
        playoff.start()

    def simulate_battle(self, robot1, robot2):
        winner = random.choice([robot1, robot2])
        print(f"{winner.name} ganó la batalla entre {robot1.name} y {robot2.name}")
        return winner
