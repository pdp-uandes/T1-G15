# competitions/league.py
from competitions.competition import Competition

class League(Competition):
    def organize_battles(self):
        # Organizar batallas entre todos los robots
        self.battles = []
        for i in range(len(self.robots)):
            for j in range(i + 1, len(self.robots)):
                self.battles.append((self.robots[i], self.robots[j]))

    def start(self, mode='auto'):
        # Iniciar todas las batallas organizadas en la liga
        self.organize_battles()
        for battle in self.battles:
            winner = self.simulate_battle(battle[0], battle[1], mode)
            self.add_result(winner.name)

    def generate_victory_table(self):
        # Generar tabla de victorias
        victory_count = {}
        for result in self.get_results():
            if result not in victory_count:
                victory_count[result] = 0
            victory_count[result] += 1

        sorted_victory_count = sorted(victory_count.items(), key=lambda item: item[1], reverse=True)
        print("Tabla de victorias:")
        for robot, victories in sorted_victory_count:
            print(f"{robot}: {victories} victorias")
