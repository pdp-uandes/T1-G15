# competitions/competition.py

class Competition:
    def __init__(self, robots):
        self.robots = robots
        self.results = []

    def organize_battles(self):
        raise NotImplementedError("este metodo debe ser implementado por subclases")

    def start(self):
        raise NotImplementedError("este metodo debe ser implementado por subclases")

    def add_result(self, battle_result):
        self.results.append(battle_result)

    def get_results(self):
        return self.results
