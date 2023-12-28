import servidor

monitoramento_acionado = False

def enviar_mensagem(modo_noturno, modo_emergencia, opcao):
    msg = {
        'modo_noturno': int(modo_noturno),
        'modo_emergencia': int(modo_emergencia)
    }

    if(opcao == 1):
        servidor.enviar_msg(msg, servidor.socket_conexao)
    
    elif(opcao == 2):
        servidor.enviar_msg(msg, servidor.socket_conexao)

def acionar_monitoramento(opcao):
    global monitoramento_acionado

    if(opcao == 1):
        monitoramento_acionado = True
    else:
        monitoramento_acionado = False

def imprimir_mensagem(msg):
    if ((msg['tipo'] == 1) and monitoramento_acionado):
        print("[QNT_CARROS/min] Via principal: " + str(msg['qnt_carros_principal']) + 
                "\n[QNT_CARROS/min] Via auxiliar: " + str(msg['qnt_carros_aux']) +
                "\nVelocidade média: " + str(msg['velocidade_media']) + "km/h\n")
    
    if ((msg['tipo'] == 2) 
        and monitoramento_acionado):
        print("[INFRACAO] Ultrapassou o limite de velocidade: " + str(msg['infracao_velocidade']) + "\n")

    if ((msg['tipo'] == 3) 
        and monitoramento_acionado):
        print("[INFRACAO] Ultrapassou o semáforo vermelho: " + str(msg['infracao_semaforo']) + "\n")