# reports/visualizer.py
import matplotlib.pyplot as plt

class Visualizer:
    @staticmethod
    def plot_bar_chart(data, title, xlabel, ylabel, filename='bar_chart.png'):
        
        labels = list(data.keys())
        values = list(data.values())

        plt.bar(labels, values)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
        print(f"Gráfico guardado en {filename}")

    @staticmethod
    def plot_pie_chart(data, title, filename='pie_chart.png'):
       
        labels = list(data.keys())
        sizes = list(data.values())

        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(title)
        plt.axis('equal')
        plt.savefig(filename)
        plt.close()
        print(f"Gráfico guardado en {filename}")

    @staticmethod
    def plot_line_chart(data, title, xlabel, ylabel, filename='line_chart.png'):
        
        labels = list(data.keys())
        values = list(data.values())

        plt.plot(labels, values, marker='o')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
        print(f"Gráfico guardado en {filename}")
