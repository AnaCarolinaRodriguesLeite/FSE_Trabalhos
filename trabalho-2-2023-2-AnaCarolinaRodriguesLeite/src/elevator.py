from pid import PID
from pwm import PWMController
from bme import TemperatureSensor
from uart import Uart
from modbus import Modbus
from time import sleep
from threading import Thread, Event
import struct
from rpi_lcd import LCD

class Elevator:
    def __init__(self):
        self.pid = PID()
        self.bmp = TemperatureSensor()
        self.uart = Uart()
        self.pwm = PWMController()
        self.modbus = Modbus()
        self.lcd = LCD()
        self.is_on = False
        self.direction = 0  # 0: Parado, 1: Subindo, -1: Descendo
        self.temperatura_ambiente = 0
        self.display_update_counter = 3
        self.display_update_interval = 1  # Atualização do display a cada 1 segundo
        self.reference = 7000
        self.display_info = " "
        self.button_pressed = None
        self.matricula = bytes([int('1',16)]) + bytes([int('7',16)]) + bytes([int('9',16)]) + bytes([int('2',16)])
        self.elevator_floors = [1192, 5166, 10145, 17125]
        self.button_values = [
            b'\x00',  # Botão Terreo Sobe
            b'\x01',  # Botão 1 And. Desce
            b'\x02',  # Botão 1 And. Sobe
            b'\x03',  # Botão 2 And. Desce
            b'\x04',  # Botão 2 And. Sobe
            b'\x05',  # Botão 3 And. Desce
            b'\x06',  # Botão Elevador Emergência
            b'\x07',  # Botão Elevador T
            b'\x08',  # Botão Elevador 1
            b'\x09',  # Botão Elevador 2
            b'\x0A'   # Botão Elevador 3
        ]
        self.response_up = {
            b'\x00',
            b'\x02',
            b'\x04',
            b'\x09',
            b'\x08',
            b'\x07',
        }
        self.response_down = {
            b'\x01',
            b'\x03',
            b'\x05',
            b'\x0A',
            b'\x09',
            b'\x07',
        }
        self.response_stop = {
            b'\x06',
        }

    def initialize(self):
        print("Elevator initialized!!!")
        self.pwm.start(0)
            
    def read_encoder(self, matricula): #TA FUNCIONANDO
        command = b'\x01\x23\xc1' + self.matricula
        modbus_message = self.modbus.code_message(command)
        self.uart.write(modbus_message)
        sleep(0.05)
        response = self.uart.read()
        
        if response:
            encoder_value = int.from_bytes(response[3:7], 'little', signed=False)
            return encoder_value
    
    def control_signal(self, control_signal): #TA FUNCIONANDO
        valor = (round(control_signal)).to_bytes(4, 'little', signed=True)
        command = b'\x01\x16\xc2' + valor + self.matricula
        modbus_message = self.modbus.code_message(command)
        self.uart.write(modbus_message)
        response = self.uart.read()
        
        if response:
            return control_signal

    def send_temperature(self): #TA FUNCIONANDO
        self.temperatura_ambiente = self.bmp.get_current_temperature()
        temperature_bytes = struct.pack('!f', self.temperatura_ambiente)
        temperature_bytes = temperature_bytes[::-1]
        
        command = b'\x01\x16\xd1' + temperature_bytes + self.matricula
         
        modbus_message = self.modbus.code_message(command)
        self.uart.write(modbus_message)
        response = self.uart.read()
        
        if response:
            return self.temperatura_ambiente

    def read_button_registers(self): #TA FUNCIONANDO
        command = b'\x01\x03\x00' + b'\x0b' + self.matricula

        modbus_message = self.modbus.code_message(command)
        self.uart.write(modbus_message)
        response = self.uart.read()
            
        if response:
            return response

    def write_button_registers(self): #TA FUNCIONANDO
        command = b'\x01\x06' + b'\x00' + b'\x01' + b'\x01' + self.matricula

        modbus_message = self.modbus.code_message(command)
        self.uart.write(modbus_message)
        response = self.uart.read()
        
        if response:
            return response
        
    # def control_elevator(self, button_pressed):
    #     if self.is_on:
    #             encoder = self.read_encoder(self.matricula)
    #             # self.pid.update_reference(self.elevator_floors)
    #             pid_control_signal = self.pid.control(5000)
    #             control_signal = self.control_signal(pid_control_signal)
    #             print("encoder", encoder)
    #             print("Valor do sinal a partir do PID:", control_signal)
    #             if self.button_pressed is not None:
    #                 response = self.read_button_registers(self.button_pressed)
    #                 print("botão", self.button_pressed)

    #                 # Determina a ação com base na resposta dos botões
    #                 if response in self.response_up:
    #                     self.pwm.apply_signal(1, 0)  # Movendo para cima
    #                     self.pwm.change_potm_duty_cycle(control_signal)
    #                 if response in self.response_down:
    #                     self.pwm.apply_signal(0, 1)  # Descendo o movimento
    #                     self.pwm.change_potm_duty_cycle(control_signal)
    #                 if response in self.response_stop:
    #                     self.pwm.apply_signal(0, 0)  # Parando o movimento
    #                     self.pwm.change_potm_duty_cycle(0)
    #                 # else:
    #                 #     # Verifica se o elevador está no andar desejado para acionar o freio
    #                 #     current_floor = encoder  # Supondo que o valor do encoder representa o andar atual
    #                 #     target_floor = self.elevator_floors[3]  # Exemplo de andar desejado

    #                 #     if current_floor == target_floor:
    #                 #         self.pwm.apply_signal(0, 0)  # Parando o movimento
    #                 #         self.pwm.change_potm_duty_cycle(0)
    #                 #     else:
    #                 #         self.pwm.apply_signal(1, 1)  # Freando o movimento
    #                 #         self.pwm.change_potm_duty_cycle(0)

    #                 # Atualizar o display LCD, se necessário
    #                 # self.update_display()
    #                 sleep(0.5)
    
    def control_elevator(self):
        if self.is_on:
            encoder = self.read_encoder(self.matricula)
            self.pid.update_reference(self.elevator_floors)
            pid_control_signal = self.pid.control(encoder)
            control_signal = self.control_signal(pid_control_signal)
            response = self.read_button_registers()
            print("encoder", encoder)
            if response is not None:
                if response in self.response_up:
                    self.pwm.apply_signal(1, 0)  # Movendo para cima
                    self.pwm.change_potm_duty_cycle(control_signal)
                elif response in self.response_down:
                    self.pwm.apply_signal(0, 1)  # Descendo o movimento
                    self.pwm.change_potm_duty_cycle(control_signal)
                elif response in self.response_stop:
                    self.pwm.apply_signal(0, 0)  # Parando o movimento
                    self.pwm.change_potm_duty_cycle(0)
                else:
                    self.pwm.apply_signal(0, 0)  # Parando o movimento
                    self.pwm.change_potm_duty_cycle(0)

                # Atualizar o display LCD, se necessário
                self.update_display()
                
                sleep(0.5)
            
    def update_display(self):
        if self.is_on:
            self.lcd.clear()
            self.temperatura_ambiente = self.send_temperature()
            if self.display_update_counter >= self.display_update_interval:
                if self.direction == 0:
                    self.display_info += "Subindo"
                    print("Subindo!")
                elif self.direction < 100:
                    self.display_info += "Descendo"
                    print("Descendo!")
                else:
                    self.display_info += "Parado"
                    print("Parado!")
                self.lcd.text(f"Estado: {self.display_info}",1)
                self.lcd.text(f'Temp:{round(self.temperatura_ambiente, 2)}', 2)
                self.display_update_counter = 0
            else:
                self.display_update_counter += 1
                
    def trata_ctrl_c(self):
        try:
            while True:
                sleep(1)
        except KeyboardInterrupt:
            self.stop()
            self.lcd.clear()
        else:
            pass   
    
    def rotina(self):
        if self.is_on:
            while True:
                self.control_elevator()
                self.trata_ctrl_c()   

    def start(self):
        self.is_on = True
        try:
            control_thread = Thread(target=self.rotina)
            control_thread.start()
        except Exception as e:
            self.trata_ctrl_c()
            print(f"Erro na Thread-2: {e}")

    def stop(self):
        self.is_on = False
        self.pwm.stop()
        self.uart.close()