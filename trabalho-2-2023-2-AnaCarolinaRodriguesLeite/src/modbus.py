import struct
from crc16 import calculoCRC
import serial

class Modbus:
    def __init__(self):
        self.is_connected = False

    def code_message(self, command, value=None):
        mensagem = bytes(command)
        
        # Adiciona o valor à mensagem se existir
        if value is not None:
            if isinstance(value, int):
                value_bytes = value.to_bytes(4, byteorder='little', signed=True)
            elif isinstance(value, float):
                value_bytes = struct.pack('<f', value)
            else:
                raise ValueError("Tipo de valor inválido")
            
            mensagem += value_bytes
        
        # Calcula o CRC apenas da parte da mensagem (sem o próprio CRC)
        crc = calculoCRC(mensagem).to_bytes(2, "little")
        
        # Adiciona o CRC calculado à mensagem
        return mensagem + crc

    def decode_message(self, message):
        if not message:
            print('Nenhuma mensagem recebida')
            return None
        
        buffer_tam = len(message)
        
        if buffer_tam != 9:
            print('Mensagem recebida incorretamente: {}'.format(message))
            return None
        
        data = message[3:7]
        crc16_recebido = message[7:9]
        crc16_calculado = calculoCRC(message[0:7], 7).to_bytes(2, 'little')

        if crc16_recebido != crc16_calculado:
            print('Mensagem recebida com CRC inválido: {}'.format(message))
            return None

        return data
