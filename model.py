from abc import ABC, abstractclassmethod, abstractmethod

class model(ABC):

    @abstractclassmethod
    def printTable(self, lines, columns, data):
        for x in range(lines):
            print("[", end = ' ')
            for y in range(columns):
                print(f"{data[x][y]};", end = ' ')
            print(']')