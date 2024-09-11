# main.py

import json
from robots.robot import Robot
from competitions.league import League
from competitions.playoff import Playoff
from competitions.tournament import Tournament
from reports.report import Report

def load_robots_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    robots = []
    for robot_data in data["robots"]:
        robot = Robot(
            name=robot_data["name"],
            energy=robot_data["energy"],
            attacks=robot_data["attacks"],
            skills=robot_data["skills"]
        )
        robots.append(robot)
    return robots

def main():
    # robots desde un archivo JSON
    robots = load_robots_from_json('robots.json')

    # seleccionar el tipo de compe
    print("Selecciona el tipo de competición:")
    print("1. Liga")
    print("2. Playoff")
    print("3. Torneo")
    choice = input("Introduce el número de la competición: ")

    if choice == "1":
        competition = League(robots)
    elif choice == "2":
        competition = Playoff(robots)
    elif choice == "3":
        competition = Tournament(robots)
    else:
        print("Selección no válida.")
        return

    # seleccionar el modo de batalla
    print("Selecciona el modo de batalla:")
    print("1. Automático")
    print("2. Participativo")
    mode_choice = input("Introduce el número del modo: ")

    if mode_choice == "1":
        mode = 'auto'
    elif mode_choice == "2":
        mode = 'participative'
    else:
        print("Selección no válida.")
        return

    # iniciar la compe
    competition.start(mode=mode)

    #generar reportes
    report = Report(competition)
    report.generate_victory_table()
    report.generate_attack_usage_bar_chart()
    report.generate_skill_usage_bar_chart()
    report.generate_battle_summary_table()

if __name__ == "__main__":
    main()
