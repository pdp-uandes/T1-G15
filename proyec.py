import random
import matplotlib.pyplot as plt
import pandas as pd 
# panda para q se vea mas bonito

# def la clase Robot
class Robot:
    def __init__(self, name, energy, attacks):
        self.name = name
        self.energy = energy
        self.max_energy = energy
        self.attacks = attacks
        self.victories = 0
        self.defeats = 0
        self.attack_usage = {attack['name']: 0 for attack in attacks}
    
    def choose_attack(self):
        return random.choice(self.attacks)
    
    def reset(self):
        self.energy = self.max_energy

# def la clase Liga

class Liga:
    def __init__(self, robots, report_options=None):
        self.robots = robots
    #Adicionamos ese parametro para que el usuário pueda definir quais relatórios desea generar
    
        self.report_options = report_options if report_options is not None else["tabela", "grafico"]
        #Puede ser uma lista que inclui 'tabela', 'grafico' o ambos

    def simulate(self):
        for i in range(len(self.robots)):
            for j in range(i + 1, len(self.robots)):
                print(f"Batalla  simulada entre {self.robots[i].name} y {self.robots[j].name}")
                self.battle(self.robots[i], self.robots[j])
    
    def battle(self, robot1, robot2):
        robot1.reset()
        robot2.reset()
        print(f"\nInicia la batalla entre:{robot1.name} y {robot2.name}!")

        while robot1.energy > 0 and robot2.energy > 0:
            attacker, defender = (robot1, robot2) if random.choice([True, False]) else (robot2, robot1)
            attack = attacker.choose_attack()
            print(f"{attacker.name} elegió el ataque '{attack['name']}'")
   
            if random.randint(1, 100) <= attack['precision']:
                defender.energy -= attack['damage']
                print(f" Ataque efectivo!! {defender.name} sufrió {attack['damage']} de daño.")
            else:
                print(f"Ataque fallo")

            print(f" Energia restante de {defender.name} es: {defender.energy}")
            attacker.attack_usage[attack['name']] += 1
        
        if robot1.energy > 0:
            print(f"\n{robot1.name} ganó la batalla contra {robot2.name}!")
            robot1.victories += 1
            robot2.defeats += 1
        else:
            print(f"\n{robot2.name} ganó la batala contra {robot1.name}!")
            robot2.victories += 1
            robot1.defeats += 1

    def report(self):
        if "tabela" in self.report_options:   
        #Modificamos ese método para verificar y generar los relatorios deseados
            # Generar tabla de victorias y derrotas
            data = {'Robot': [robot.name for robot in self.robots],
                'Victorias': [robot.victories for robot in self.robots],
                'Derrotas': [robot.defeats for robot in self.robots]}
            df = pd.DataFrame(data)
            print("Tabla de Victorias y Derrotas:")
            print(df)

        if "grafico" in self.report_options:    

         # Gráfico de barras para usos de ataques
            for robot in self.robots:
                plt.figure()
                plt.bar(robot.attack_usage.keys(), robot.attack_usage.values())
                plt.title(f'Uso de Ataques para {robot.name}')
                plt.xlabel('Ataque')
                plt.ylabel('Cantidad de usos')
                plt.show()

# Carga robots
robots_data = [
    {"name": "fuegazo", "energy": 75, "attacks": [{"name": "arco", "damage": 20, "precision": 80, "recharge": 1},
                                                {"name": "cabezazo", "damage": 15, "precision": 95, "recharge": 0}]},
    {"name": "aguatero_suplente", "energy": 80, "attacks": [{"name": "chorro", "damage": 40, "precision": 70, "recharge": 2},
                                                   {"name": "espada de agua", "damage": 10, "precision": 95, "recharge": 0}]},
    # Agregar más robots según sea necesario
]


robots = [Robot(robot['name'], robot['energy'], robot['attacks']) for robot in robots_data]

#Se debe generar una tabla, un grafico o ambos

report_options = ["tabela", "grafico"] 

# Simular la liga
liga = Liga(robots, report_options )
liga.simulate()
liga.report()
