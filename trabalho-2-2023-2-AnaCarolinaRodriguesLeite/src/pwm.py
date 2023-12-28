import RPi.GPIO as GPIO

class PWMController:
    def __init__(self, dir1_pin=20, dir2_pin=21, potm_pin=12, sensor_terreo=18, sensor_1_andar=23, sensor_2_andar=24, sensor_3_andar=25, frequency=1000):
        self.dir1_pin = dir1_pin
        self.dir2_pin = dir2_pin
        self.potm_pin = potm_pin
        self.sensor_terreo = sensor_terreo
        self.sensor_1_andar = sensor_1_andar
        self.sensor_2_andar = sensor_2_andar
        self.sensor_3_andar = sensor_3_andar
        self.frequency = frequency
        self.duty_cycle = 80

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # Configure os pinos do motor
        GPIO.setup(self.dir1_pin, GPIO.OUT)
        GPIO.setup(self.dir2_pin, GPIO.OUT)
        GPIO.setup(self.potm_pin, GPIO.OUT)

        # Configure os pinos dos sensores dos andares
        GPIO.setup(self.sensor_terreo, GPIO.OUT)
        GPIO.setup(self.sensor_1_andar, GPIO.OUT)
        GPIO.setup(self.sensor_2_andar, GPIO.OUT)
        GPIO.setup(self.sensor_3_andar, GPIO.OUT)

        # Create PWM objects
        self.potm_pwm = GPIO.PWM(self.potm_pin, self.frequency)

    def start(self, potm_duty_cycle):
        self.potm_pwm.start(potm_duty_cycle)

    def stop(self):
        self.potm_pwm.stop()

    def change_potm_duty_cycle(self, duty_cycle):
        self.potm_pwm.ChangeDutyCycle(duty_cycle)
    
    def check_floor_sensors(self):
        GPIO.output(self.sensor_terreo, GPIO.LOW)
        GPIO.output(self.sensor_1_andar, GPIO.LOW)
        GPIO.output(self.sensor_2_andar, GPIO.LOW)
        GPIO.output(self.sensor_3_andar, GPIO.LOW)
        # Verificar o estado dos sensores de andar
        if GPIO.input(self.sensor_terreo) == GPIO.HIGH:
            # Lógica para acender a luz do térreo
            print("Chegou no térreo - Acendendo luz do térreo")
            GPIO.output(self.sensor_terreo, GPIO.HIGH)
        elif GPIO.input(self.sensor_1_andar) == GPIO.HIGH:
            # Lógica para acender a luz do 1º andar
            print("Chegou no 1º andar - Acendendo luz do 1º andar")
            GPIO.output(self.sensor_1_andar, GPIO.HIGH)
        elif GPIO.input(self.sensor_2_andar) == GPIO.HIGH:
            # Lógica para acender a luz do 2º andar
            print("Chegou no 2º andar - Acendendo luz do 2º andar")
            GPIO.output(self.sensor_2_andar, GPIO.HIGH)
        elif GPIO.input(self.sensor_3_andar) == GPIO.HIGH:
            # Lógica para acender a luz do 3º andar
            print("Chegou no 3º andar - Acendendo luz do 3º andar")
            GPIO.output(self.sensor_3_andar, GPIO.HIGH)
    
    def apply_signal(self, direcao1, direcao2):
       # Aplicar o sinal de controle ao motor
        if direcao1 == 1 and direcao2 == 0:  # Se o sinal de controle for positivo, mova para frente
            # Definir ciclo de trabalho para mover para frente
            GPIO.output(self.dir1_pin, 1)
            GPIO.output(self.dir2_pin, 0)
            self.check_floor_sensors()
            print("move para frente!")
        if direcao1 == 0 and direcao2 == 1:  # Se for negativo, mova para trás
            # Definir ciclo de trabalho para mover para trás
            GPIO.output(self.dir1_pin, 0)
            GPIO.output(self.dir2_pin, 1)
            self.check_floor_sensors()
            print("move para trás!")
        if direcao1 == 0 and direcao2 == 0:  # Se o sinal for zero, motor livre
            GPIO.output(self.dir1_pin, 0)
            GPIO.output(self.dir2_pin, 0)
            self.check_floor_sensors()
            print("motor livre!")
        if direcao1 == 1 and direcao2 == 1:  # Se o sinal for um, motor freia
            GPIO.output(self.dir1_pin, 1)
            GPIO.output(self.dir2_pin, 1)
            self.check_floor_sensors()
            print("motor freio!")

    def cleanup(self):
        GPIO.cleanup()