import socket_distribuido
import cruzamento

def verificar_mensagem(msg):
    if(msg['modo_noturno'] == 1):
        cruzamento.modo_noturno = True
    else:
        cruzamento.modo_noturno = False
    
    if(msg['modo_emergencia'] == 1):
        cruzamento.modo_emergencia = True
    else:
        cruzamento.modo_emergencia = False

def enviar_mensagem_qnt_carros(qnt_carros_principal, qnt_carros_aux, velocidade_media, cruzamento):
    msg = {
        'tipo': 1,
        'qnt_carros_principal': qnt_carros_principal,
        'qnt_carros_aux': qnt_carros_aux,
        'velocidade_media': velocidade_media
    }

    if (cruzamento['semaforo1_pino1'] == 1):
        socket_distribuido.enviar_msg(msg, socket_distribuido.socket_cruzamento1)
    
    if (cruzamento['semaforo2_pino1'] == 2):
        socket_distribuido.enviar_msg(msg, socket_distribuido.socket_cruzamento2)


def enviar_mensagem_infracao_velocidade(qnt_infracao, cruzamento):
    msg = {
        'tipo': 2,
        'infracao_velocidade': qnt_infracao
    }

    if (cruzamento['semaforo1_pino1'] == 1):
        socket_distribuido.enviar_msg(msg, socket_distribuido.socket_cruzamento1)
    
    if (cruzamento['semaforo2_pino1'] == 2):
        socket_distribuido.enviar_msg(msg, socket_distribuido.socket_cruzamento2)

def enviar_mensagem_infracao_semaforo(qnt_infracao, cruzamento):
    msg = {
        'tipo': 3,
        'infracao_semaforo': qnt_infracao
    }

    if (cruzamento['semaforo1_pino1'] == 1):
        socket_distribuido.enviar_msg(msg, socket_distribuido.socket_cruzamento1)
    
    if (cruzamento['semaforo2_pino1'] == 2):
        socket_distribuido.enviar_msg(msg, socket_distribuido.socket_cruzamento2)