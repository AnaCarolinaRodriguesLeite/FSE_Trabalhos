import RPi.GPIO as GPIO
import time

class ControleVelocidade:

    def __init__(self, sensorA, sensorB):
        self.sensorA = sensorA
        self.sensorB = sensorB
        self.tempoA = 0
        self.tempoB = 0
        self.qnt_carros = 0
        self.velocidade_total = 0
        self.qnt_infracao = 0
    
    def calcula_velocidade_via_auxiliar(self):
        tempo = self.tempoB - self.tempoA
        velocidade = ((1/tempo)*3.6) 

        self.tempoA = 0
        self.tempoB = 0

        self.qnt_carros += 1
        self.velocidade_total += velocidade

        if (velocidade > 60.0):
            self.adicionar_infracao()

    def calcula_velocidade_via_princial(self):
        tempo = self.tempoB - self.tempoA
        velocidade = ((1/tempo)*3.6) 

        self.tempoA = 0
        self.tempoB = 0

        self.qnt_carros += 1
        self.velocidade_total += velocidade

        if (velocidade > 80.0):
            self.adicionar_infracao()

    def verificar_sensor_velociadade_auxiliar(self):
        if GPIO.event_detected(self.sensorA):
            GPIO.remove_event_detect(self.sensorA)
            GPIO.add_event_detect(self.sensorA, GPIO.BOTH, bouncetime=200)
            self.tempoA = time.time()
        
        if GPIO.event_detected(self.sensorB):
            GPIO.remove_event_detect(self.sensorB)
            GPIO.add_event_detect(self.sensorB, GPIO.BOTH, bouncetime=200)
            self.tempoB = time.time()
        
        if ((self.tempoA != 0) and (self.tempoB != 0)):
            self.calcula_velocidade_via_auxiliar()

    def verificar_sensor_velociadade_principal(self):
        if GPIO.event_detected(self.sensorA):
            GPIO.remove_event_detect(self.sensorA)
            GPIO.add_event_detect(self.sensorA, GPIO.RISING, bouncetime=200)
            self.tempoA = time.time()
        
        if GPIO.event_detected(self.sensorB):
            GPIO.remove_event_detect(self.sensorB)
            GPIO.add_event_detect(self.sensorB, GPIO.RISING, bouncetime=200)
            self.tempoB = time.time()
        
        if ((self.tempoA != 0) and (self.tempoB != 0)):
            self.calcula_velocidade_via_princial()
    
    def verificar_carro_esperando(self):
        if GPIO.event_detected(self.sensorA):
            GPIO.remove_event_detect(self.sensorA)
            GPIO.add_event_detect(self.sensorA, GPIO.RISING, bouncetime=200)
            return True
        
        return False

    def verificar_infracao(self):
        if GPIO.event_detected(self.sensorB):
            GPIO.remove_event_detect(self.sensorB)
            GPIO.add_event_detect(self.sensorB, GPIO.RISING, bouncetime=200)
            return True

        return False
    
    def calcular_velocidade_media(self):
        return (self.velocidade_total/self.qnt_carros)
    
    def adicionar_carro(self):
        self.qnt_carros += 1
    
    def adicionar_infracao(self):
        self.qnt_infracao += 1