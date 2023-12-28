import socket
import json
import mensagem
from time import sleep
import pickle

socket_cruzamento1 = None
socket_cruzamento2 = None
socket_cruzamento = None

def monitorar_socket(socket):
    while True:
        data = socket.recv(1024).decode('utf-8')
        msg = json.loads(data)   

        mensagem.verificar_mensagem(msg)
        sleep(1)

def iniciar_socket(host, port, cruzamento):
    try:
        if(cruzamento == 1):
            global socket_cruzamento1
            socket_cruzamento1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_cruzamento1.connect((host, port))

            print(f"Conectado no servidor {host} {port}")

            monitorar_socket(socket_cruzamento1)

            msg = {
                'tipo': 1,
                'qnt_carros_principal': qnt_carros_principal,
                'qnt_carros_aux': qnt_carros_aux,
                'velocidade_media': velocidade_media
            }

            try:
                while True:
                    enviar_msg(msg)
                    data = socket_cruzamento1.recv(1024)
            except:
                print("erro de enviar arquivo ou conexão")

            if(cruzamento == 2):
                global socket_cruzamento2
                socket_cruzamento2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket_cruzamento2.connect((host, port))
                print(f"Conectado no servidor {host} {port}")
                monitorar_socket(socket_cruzamento2)

                try:
                    while True:
                        enviar_msg(msg)
                        data = socket_cruzamento2.recv(1024)
                except:
                    print("erro de enviar arquivo ou conexão")
    except ConnectionRefusedError:
        print("Error de conexão!")


def enviar_msg(msg):
    try:
        # msg = json.dumps(msg)
        socket_cruzamento.send(pickle.dumps(msg))
        sleep(1)
    except:
        print("Erro de envio de mensagem!")