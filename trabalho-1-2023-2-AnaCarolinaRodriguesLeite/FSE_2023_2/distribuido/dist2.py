from multiprocessing import connection
import socket
import threading
import json
import cruzamento
import socket_distribuido
import sys

cruzamento2 ={
    'semaforo1_pino1': 10,
    'semaforo1_pino2': 8,
    'semaforo2_pino1': 1,
    'semaforo2_pino2': 18,
    'botao_pedestre1': 23,
    'botao_pedestre2': 24,
    'sensor_via_auxiliar1': 25,
    'sensor_via_auxiliar2': 12,
    'sensor_via_principal1': 16,
    'sensor_via_principal2': 20,
    'buzzer': 21
}

def enviar_msg(msg):
    global socket_distr
    socket_distr.sendall(bytes((json.dumps(msg)),encoding="utf-8"))

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Informe o host e as portas para cada cuzamento:\n")
        print("python3 main.py + HOST + PORTA_CRUZAMENTO2\n")
        sys.exit()

    thread_socket2 = threading.Thread(target=socket_distribuido.iniciar_socket, args=(sys.argv[1], int(sys.argv[2]), 2))
    thread_cruzamento2 = threading.Thread(target=cruzamento.iniciar_controle_cruzamento, args=(cruzamento2,))
    
    thread_socket2.start()
    thread_cruzamento2.start()
    