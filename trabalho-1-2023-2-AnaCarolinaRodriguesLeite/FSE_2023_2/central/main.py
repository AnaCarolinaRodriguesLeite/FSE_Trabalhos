import sys
import threading
from multiprocessing import Process
from threading import Thread
import servidor
from menu import Menu
   
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Informe o host e as portas para cada cuzamento:\n")
        print(" python3 main.py + HOST + PORTA_CRUZAMENTO\n")
        sys.exit()

    menu = Menu()

    thread_cruzamento = threading.Thread(target=servidor.iniciar_socket, args=(sys.argv[1], int(sys.argv[2]), 1))
    thread_menu = threading.Thread(target=menu.menu_principal)
    thread_cruzamento.start()
    thread_menu.start()