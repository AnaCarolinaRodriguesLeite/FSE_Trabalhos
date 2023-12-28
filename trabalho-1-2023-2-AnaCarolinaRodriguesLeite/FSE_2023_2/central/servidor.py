import socket
import json
import mensagem
from time import sleep
from threading import Thread

socket_cruzamento = None
socket_conexao = None
conexao = []

def mostrar_mensagem(socket_conexao):
    while True:
        data = socket_conexao.recv(1024)
        if not data:
            break
        else:
            msg = json.loads(data) 
            print("mensagem:")
            print(msg)

            mensagem.imprimir_mensagem(msg)
    sleep(1)

def iniciar_socket(host, port, id_cruzamento):
    try:
        if(id_cruzamento == 1):
            global socket_cruzamento
            socket_cruzamento = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_cruzamento.bind((host, port))
            socket_cruzamento.listen(5)
            
            global socket_conexao
            conn, addr = socket_cruzamento.accept()
            socket_conexao = conn
            conexao.append(socket_conexao)
            mostrar_mensagem(socket_conexao)

    except ConnectionRefusedError:
        print("Error de conexão!")


def enviar_msg(msg, socket_conexao):
    try:
        msg = json.dumps(msg)
        socket_conexao.send((msg.encode()))
        sleep(5)
    except ConnectionRefusedError:
        print("Erro no envio da mensagem!")