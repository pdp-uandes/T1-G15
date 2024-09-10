# competitions/playoff.py
from competitions.competition import Competition

class Playoff(Competition):
    def organize_battles(self):
        # Organizar las batallas de eliminación directa
        self.battles = [(self.robots[i], self.robots[i + 1]) for i in range(0, len(self.robots), 2)]

    def start(self, mode='auto'):
        while len(self.robots) > 1:
            self.organize_battles()
            winners = []
            for battle in self.battles:
                winner = self.simulate_battle(battle[0], battle[1], mode)
                winners.append(winner)
            self.robots = winners
        # El ganador final es el último robot que queda en la lista
        self.add_result(self.robots[0].name)
        print(f"¡{self.robots[0].name} es el campeón del Playoff!")
