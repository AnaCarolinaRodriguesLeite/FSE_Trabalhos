import RPi._GPIO as GPIO

def verificar_carro(pino, tipo):
    GPIO.remove_event_detect(pino)
    if GPIO.event_detected(pino):
        if tipo == 'presenca':
            GPIO.add_event_detect(pino, GPIO.RISING, bouncetime=100)
        elif tipo == 'velocidade':
            GPIO.add_event_detect(pino, GPIO.FALLING, bouncetime=100)
        else:
            raise ValueError("Tipo de sensor inválido: use 'presenca' ou 'velocidade'")
        return True
    return False