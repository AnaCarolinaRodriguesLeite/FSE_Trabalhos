import serial
from time import sleep

class Uart:
    def __init__(self, port="/dev/serial0", baudrate=115200):
        self.serial = serial.Serial(port, baudrate, timeout=0.5)
        self.check_connection()
        self.is_connected = False
            
    def check_connection(self):
        if self.serial.is_open:
            print("Conexão UART estabelecida :)")
        self.is_connected = self.serial.is_open
        if not self.is_connected:
            print("Erro na conexão UART :(")        

    def write(self, message, value=None):
        self.serial.flushInput()
        self.serial.write(message)
    
    def read(self):
        received_data = self.serial.read()
        return received_data

    def close(self):
        if self.serial.is_open:
            self.serial.close()
