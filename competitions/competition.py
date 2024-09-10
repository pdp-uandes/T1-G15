# competitions/competition.py
import random

class Competition:
    def __init__(self, robots):
        self.robots = robots  #lista robots que participan en la compe
        self.results = []  # almacena los resultados de las batallas

    def organize_battles(self):
        raise NotImplementedError("este metodo debe ser implementado por las subclases.")

    def start(self, mode='auto'):
        raise NotImplementedError("este metodo debe ser implementado por las subclases.")

    def add_result(self, battle_result):
        self.results.append(battle_result)

    def get_results(self):
        return self.results

    def simulate_battle(self, robot1, robot2, mode='auto'):
        # simulacion de una batalla por turnos entre dos robots
        while robot1.is_alive() and robot2.is_alive():
            if mode == 'auto':
                attack1 = robot1.choose_attack()
                attack2 = robot2.choose_attack()
            else:
                attack1 = self.get_user_attack_choice(robot1)
                attack2 = self.get_user_attack_choice(robot2)

            if attack1:
                robot2.apply_skills('before_attack')
                damage1 = attack1.use()
                modified_damage1 = robot2.modify_damage_received(damage1)
                robot2.take_damage(modified_damage1)
                print(f"{robot1.name} usa {attack1.name} y causa {modified_damage1} puntos de daño a {robot2.name}.")

            if attack2 and robot2.is_alive():
                robot1.apply_skills('before_attack')
                damage2 = attack2.use()
                modified_damage2 = robot1.modify_damage_received(damage2)
                robot1.take_damage(modified_damage2)
                print(f"{robot2.name} usa {attack2.name} y causa {modified_damage2} puntos de daño a {robot1.name}.")

            # fin de turno para ambos robots
            robot1.end_turn()
            robot2.end_turn()

        # determinar el ganador
        winner = robot1 if robot1.is_alive() else robot2
        print(f"{winner.name} gana la batalla entre {robot1.name} y {robot2.name}!")
        return winner

    def get_user_attack_choice(self, robot):
        # metodo todo para elegir manualmente el ataque en modo participativo
        print(f"Es el turno de {robot.name}. Elige un ataque:")
        for i, attack in enumerate(robot.attacks):
            print(f"{i + 1}: {attack.name} (daño: {attack.damage}, precisión: {attack.precision}%)")
        
        while True:
            choice = input("Introduce el número del ataque que quieres usar: ")
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(robot.attacks):
                    return robot.attacks[idx]
                else:
                    print("Selección inválida, intenta de nuevo.")
            except ValueError:
                print("Por favor, introduce un número.")
