from smbus2 import SMBus as I2Cbus, i2c_msg as I2CMessage
from bmp280 import BMP280

class TemperatureSensor:
    def get_current_temperature(self):
        try:
            bus = I2Cbus(1)
            sensor = BMP280(i2c_dev=bus)
            current_temp = sensor.get_temperature()
            return current_temp
        except Exception as e:
            return f"Erro ao obter temperatura: {e}"
