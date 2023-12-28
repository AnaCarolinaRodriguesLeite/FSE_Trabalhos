import RPi.GPIO as GPIO

def iniciar_sensor_velocidade(sensor):
    GPIO.add_event_detect(sensor, GPIO.RISING, bouncetime=100)