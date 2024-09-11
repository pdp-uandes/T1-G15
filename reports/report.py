# reports/report.py
import csv
import matplotlib.pyplot as plt
from collections import defaultdict
from reports.visualizer import Visualizer

class Report:
    def __init__(self, competition):
        self.competition = competition  # La competición de la que se generarán los reportes

    def generate_victory_table(self, filename='victory_table.csv'):
        # Generar tabla de victorias y derrotas
        victory_count = defaultdict(int)
        for result in self.competition.get_results():
            victory_count[result] += 1

        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['Robot', 'Victorias']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for robot, victories in victory_count.items():
                    writer.writerow({'Robot': robot, 'Victorias': victories})
            
            print(f"Tabla de victorias guardada en {filename}")
        except Exception as e:
            print(f"Error al generar la tabla de victorias: {e}")

    def generate_attack_usage_bar_chart(self, filename='attack_usage.png'):
        # Generar gráfico de barras con la cantidad de veces que se utilizó cada ataque
        attack_usage = defaultdict(int)
        
        try:
            for robot in self.competition.robots:
                for attack in robot.attacks:
                    attack_usage[attack.name] += attack.usage_count
            
            plt.bar(attack_usage.keys(), attack_usage.values())
            plt.xlabel('Ataques')
            plt.ylabel('Cantidad de usos')
            plt.title('Uso de ataques durante la competición')
            plt.savefig(filename)
            plt.close()

            print(f"Gráfico de uso de ataques guardado en {filename}")
        except Exception as e:
            print(f"Error al generar el gráfico de uso de ataques: {e}")

    def generate_skill_usage_bar_chart(self, filename='skill_usage.png'):
        # Generar gráfico de barras con la cantidad de veces que se activó cada habilidad
        skill_usage = defaultdict(int)
        
        try:
            for robot in self.competition.robots:
                for skill in robot.skills:
                    skill_usage[skill.name] += skill.activation_count
            
            plt.bar(skill_usage.keys(), skill_usage.values())
            plt.xlabel('Habilidades')
            plt.ylabel('Cantidad de activaciones')
            plt.title('Activación de habilidades durante la competición')
            plt.savefig(filename)
            plt.close()

            print(f"Gráfico de uso de habilidades guardado en {filename}")
        except Exception as e:
            print(f"Error al generar el gráfico de uso de habilidades: {e}")

    def generate_battle_summary_table(self, filename='battle_summary.csv'):
        # Generar tabla con cada batalla disputada, indicando el ganador, la cantidad de turnos, y la energía total del ganador
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['Batalla', 'Ganador', 'Turnos', 'Energía restante']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for i, result in enumerate(self.competition.get_results(), 1):
                    battle_info = result.get('battle_info')
                    if battle_info:
                        writer.writerow({
                            'Batalla': f'Batalla {i}',
                            'Ganador': battle_info['winner'],
                            'Turnos': battle_info['turns'],
                            'Energía restante': battle_info['remaining_energy']
                        })
            
            print(f"Resumen de batallas guardado en {filename}")
        except Exception as e:
            print(f"Error al generar el resumen de batallas: {e}")
            
    def generate_attack_usage_bar_chart(self, filename='attack_usage.png'):
        attack_usage = defaultdict(int)
        for robot in self.competition.robots:
            for attack in robot.attacks:
                attack_usage[attack.name] += attack.usage_count

        Visualizer.plot_bar_chart(
            data=attack_usage,
            title='Uso de ataques durante la competición',
            xlabel='Ataques',
            ylabel='Cantidad de usos',
            filename=filename
        )

