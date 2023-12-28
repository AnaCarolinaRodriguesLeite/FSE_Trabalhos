from time import sleep
import RPi.GPIO as GPIO

def set_up_gpio(cruzamento):
    GPIO.setwarnings(False)

    #GPIO OUT
    GPIO.setup(cruzamento['semaforo1_pino1'], GPIO.OUT)
    GPIO.setup(cruzamento['semaforo1_pino2'], GPIO.OUT)
    GPIO.setup(cruzamento['semaforo2_pino1'], GPIO.OUT)
    GPIO.setup(cruzamento['semaforo2_pino2'], GPIO.OUT)
    GPIO.setup(cruzamento['buzzer'], GPIO.OUT)
    #GPIO IN
    GPIO.setup(cruzamento['botao_pedestre1'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(cruzamento['botao_pedestre2'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(cruzamento['sensor_via_auxiliar1'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(cruzamento['sensor_via_auxiliar2'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(cruzamento['sensor_via_principal1'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(cruzamento['sensor_via_principal2'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def fechar_semaforo(cruzamento):
    # via principal
    GPIO.output(cruzamento['semaforo1_pino1'], GPIO.HIGH)
    GPIO.output(cruzamento['semaforo1_pino2'], GPIO.HIGH) 

    # via aux
    GPIO.output(cruzamento['semaforo2_pino1'], GPIO.HIGH)
    GPIO.output(cruzamento['semaforo2_pino2'], GPIO.HIGH)

def abrir_via_principal(cruzamento):
    # via principal
    GPIO.output(cruzamento['semaforo1_pino1'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo1_pino2'], GPIO.HIGH)

    # via aux
    GPIO.output(cruzamento['semaforo2_pino1'], GPIO.HIGH)
    GPIO.output(cruzamento['semaforo2_pino2'], GPIO.HIGH)

def alertar_via_principal(cruzamento):
    # via principal
    GPIO.output(cruzamento['semaforo1_pino1'], GPIO.HIGH)
    GPIO.output(cruzamento['semaforo1_pino2'], GPIO.LOW)

    # via aux
    GPIO.output(cruzamento['semaforo2_pino1'], GPIO.HIGH)
    GPIO.output(cruzamento['semaforo2_pino2'], GPIO.HIGH)

def abrir_via_aux(cruzamento):
    # via principal
    GPIO.output(cruzamento['semaforo1_pino1'], GPIO.HIGH)
    GPIO.output(cruzamento['semaforo1_pino2'], GPIO.HIGH) 

    # via aux
    GPIO.output(cruzamento['semaforo2_pino1'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo2_pino2'], GPIO.HIGH)

def alertar_via_aux(cruzamento):
    # via principal
    GPIO.output(cruzamento['semaforo1_pino1'], GPIO.HIGH)
    GPIO.output(cruzamento['semaforo1_pino2'], GPIO.HIGH) 

    # via aux
    GPIO.output(cruzamento['semaforo2_pino1'], GPIO.HIGH)
    GPIO.output(cruzamento['semaforo2_pino2'], GPIO.LOW)

def modo_noturno(cruzamento):
    # via principal
    GPIO.output(cruzamento['semaforo1_pino1'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo1_pino2'], GPIO.LOW) 

    # via aux
    GPIO.output(cruzamento['semaforo2_pino1'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo2_pino2'], GPIO.LOW)

    sleep(1)
    GPIO.output(cruzamento['semaforo1_pino1'], GPIO.HIGH)
    GPIO.output(cruzamento['semaforo2_pino1'], GPIO.HIGH)
    sleep(1)

def iniciar_semaforo(cruzamento):
    GPIO.setmode(GPIO.BCM)
    set_up_gpio(cruzamento)