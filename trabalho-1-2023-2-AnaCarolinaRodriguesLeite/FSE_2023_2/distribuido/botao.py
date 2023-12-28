import RPi.GPIO as GPIO

def verificar_botao_acionado(botao):
    GPIO.remove_event_detect(botao)
    if GPIO.event_detected(botao):
        GPIO.add_event_detect(botao, GPIO.RISING)
        return True
    else:
        GPIO.add_event_detect(botao, GPIO.FALLING)
        return False

def iniciar_botao(botao):
    GPIO.remove_event_detect(botao)
    GPIO.add_event_detect(botao, GPIO.RISING)