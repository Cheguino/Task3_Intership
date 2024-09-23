# table.py
from judge import Judge

class Table:
    def __init__(self, names):
        self.names = names

    def print_table(self):
        # Imprime la cabecera con formato ASCII-graphic
        self.print_border(len(self.names))
        print(f"| {'PC \\ User':^12}", end="|")
        for name in self.names:
            print(f" {name:^10} ", end="|")
        print()

        # Línea separadora
        self.print_border(len(self.names))

        # Imprime las filas con los resultados00
        judge = Judge(len(self.names))
        for i, name in enumerate(self.names):
            print(f"| {name:^12}", end="|")
            for j in range(len(self.names)):
                print(f" {judge.decide(i, j):^10} ", end="|")
            print()

            # Línea separadora entre filas
            self.print_border(len(self.names))

    def print_border(self, num_columns):
        # Imprimir una línea de borde para la tabla
        print("+", end="")
        for _ in range(num_columns + 1):
            print("-" * 12 + "+", end="")
        print()
