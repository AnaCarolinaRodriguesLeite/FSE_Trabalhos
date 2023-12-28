from multiprocessing import connection
import socket
import threading
import json
import cruzamento
import socket_distribuido
import sys

# cruzamentos
cruzamento1 ={
    'semaforo1_pino1': 9,
    'semaforo1_pino2': 11,
    'semaforo2_pino1': 5,
    'semaforo2_pino2': 6,
    'botao_pedestre1': 13,
    'botao_pedestre2': 19,
    'sensor_via_auxiliar1': 26,
    'sensor_via_auxiliar2': 22,
    'sensor_via_principal1': 0,
    'sensor_via_principal2': 27,
    'buzzer': 17
}

def enviar_msg(msg):
    global socket_distr
    socket_distr.sendall(bytes((json.dumps(msg)),encoding="utf-8"))

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Informe o host e as portas para cada cuzamento:\n")
        print("python3 main.py + HOST + PORTA_CRUZAMENTO1\n")
        sys.exit()

    thread_socket1 = threading.Thread(target=socket_distribuido.iniciar_socket, args=(sys.argv[1], int(sys.argv[2]), 1))
    thread_cruzamento1 = threading.Thread(target=cruzamento.iniciar_controle_cruzamento, args=(cruzamento1,))
    
    thread_socket1.start()
    thread_cruzamento1.start()
    