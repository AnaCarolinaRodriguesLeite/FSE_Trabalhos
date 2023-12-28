from elevator import Elevator

class Menu:
    def __init__(self):
        self.elevator = Elevator()
        self.matricula = [1, 7, 9, 2]

    def main(self):
        self.elevator.initialize()
        self.elevator.start()

if __name__ == "__main__":
    menu = Menu()
    menu.main()