# competitions/tournament.py
from competitions.competition import Competition
from competitions.playoff import Playoff
import random

class Tournament(Competition):
    def organize_battles(self):
        # Dividir los robots en grupos
        self.groups = [self.robots[i:i+4] for i in range(0, len(self.robots), 4)]
        self.battles = []
        for group in self.groups:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    self.battles.append((group[i], group[j]))

    def start(self, mode='auto'):
        self.organize_battles()
        group_winners = []
        for group in self.groups:
            winners = []
            for robot in group:
                if len([r for r in group if r != robot]) > 0:
                    winner = self.simulate_battle(robot, random.choice([r for r in group if r != robot]), mode)
                else:
                    winner = robot
                winners.append(winner)
            group_winners.append(max(winners, key=lambda r: winners.count(r)))

        # Iniciar el Playoff con los ganadores de los grupos
        playoff = Playoff(group_winners)
        playoff.start(mode)
