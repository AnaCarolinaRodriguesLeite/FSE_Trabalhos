from time import sleep
import semaforo
import botao
import verifica_carro
from controlar_velocidade import ControleVelocidade
import velocidade
import mensagem

modo_noturno = False
modo_emergencia = False

def ativar_modo_noturno(cruzamento):
    while modo_noturno:
        semaforo.modo_noturno(cruzamento)
    
    controlar_semaforo(cruzamento)

def ativar_modo_emergencia(cruzamento):
    while modo_emergencia:
        semaforo.abrir_via_principal(cruzamento)
    
    controlar_semaforo(cruzamento)

def controlar_via_principal(cruzamento):
    semaforo.abrir_via_principal(cruzamento)

    controle_sensor = ControleVelocidade(cruzamento['sensor_via_principal1'], cruzamento['sensor_via_principal2'])

    tempo_max = 20
    tempo_min = 10
    botao_pressionado = False
    sensor_presenca_acionado = False

    # cronômetro
    while (tempo_max > 0):
        sleep(0.7)
        tempo_max = tempo_max - 1

        if(botao.verificar_botao_acionado(cruzamento['botao_pedestre1'])
            and (tempo_max <= tempo_min) 
            and ( not botao_pressionado)):
            botao_pressionado = True
            break

        if (botao.verificar_botao_acionado(cruzamento['botao_pedestre1'])
            and (tempo_max > tempo_min) 
            and ( not botao_pressionado)):
            botao_pressionado = True
        
        if ((verifica_carro.verificar_carro(cruzamento['sensor_via_principal1'], 'presenca') 
            or verifica_carro.verificar_carro(cruzamento['sensor_via_principal2'], 'presenca'))
            and (tempo_max <= tempo_min) 
            and ( not sensor_presenca_acionado)):
            break

        if ((verifica_carro.verificar_carro(cruzamento['sensor_via_principal1'], 'presenca') 
            or verifica_carro.verificar_carro(cruzamento['sensor_via_principal2'], 'presenca'))
            and (tempo_max > tempo_min) 
            and ( not botao_pressionado)):
            sensor_presenca_acionado = True

        controle_sensor.verificar_sensor_velociadade_principal()

        if(modo_noturno):
            ativar_modo_noturno(cruzamento)
        
        if(modo_emergencia):
            ativar_modo_emergencia(cruzamento)
        
        if((tempo_max % 2) == 0):
            qnt_carros = int(controle_sensor.qnt_carros + controle_sensor.qnt_carros)
            if (qnt_carros == 0):
                velocida_media = 0
            else:
                velocida_media = (controle_sensor.velocidade_total)/(controle_sensor.qnt_carros)
            mensagem.enviar_mensagem_qnt_carros(qnt_carros, 0, velocida_media, cruzamento)

    semaforo.alertar_via_principal(cruzamento)
    sleep(3)

    qnt_infracao = int(controle_sensor.qnt_infracao)
    mensagem.enviar_mensagem_infracao_velocidade(qnt_infracao, cruzamento)


def controlar_via_aux(cruzamento):
    semaforo.abrir_via_aux(cruzamento)

    controle_sensor = ControleVelocidade(cruzamento['sensor_via_auxiliar1'], cruzamento['sensor_via_auxiliar2'])
    
    tempo_max = 10
    tempo_min = 5
    botao_pressionado = False
    sensor_presenca_acionado = False

    # cronômetro
    while (tempo_max > 0):
        sleep(0.7)
        tempo_max = tempo_max - 1

        if(botao.verificar_botao_acionado(cruzamento['botao_pedestre2'])
            and (tempo_max <= tempo_min) 
            and ( not botao_pressionado)):
            botao_pressionado = True
            break

        if (botao.verificar_botao_acionado(cruzamento['botao_pedestre2'])
            and (tempo_max > tempo_min) 
            and ( not botao_pressionado)):
            botao_pressionado = True
        
        if ((controle_sensor.verificar_carro_esperando())
            and (tempo_max <= tempo_min) 
            and ( not sensor_presenca_acionado)):
            break

        if ((controle_sensor.verificar_carro_esperando())
            and (tempo_max <= tempo_min) 
            and ( not sensor_presenca_acionado)):
            sensor_presenca_acionado = True
        
        if((verifica_carro.verificar_carro(cruzamento['sensor_via_auxiliar1'], 'presenca')) and (verifica_carro.verificar_carro(cruzamento['sensor_via_auxiliar2'], 'presenca'))):
            controle_sensor.adicionar_carro()
        
        if(controle_sensor.verificar_infracao()):
            controle_sensor.adicionar_infracao()
        
        controle_sensor.verificar_sensor_velociadade_auxiliar()

        if(modo_noturno):
            ativar_modo_noturno(cruzamento)
        
        if(modo_emergencia):
            ativar_modo_emergencia(cruzamento)

        if((tempo_max % 2) == 0):
            qnt_carros = int(controle_sensor.qnt_carros)
            mensagem.enviar_mensagem_qnt_carros(0, qnt_carros, 0, cruzamento)

    semaforo.alertar_via_aux(cruzamento)
    sleep(3)

    qnt_infracao = int(controle_sensor.qnt_infracao)
    mensagem.enviar_mensagem_infracao_semaforo(qnt_infracao, cruzamento)

def controlar_semaforo(cruzamento):
    while True:
        semaforo.fechar_semaforo(cruzamento)
        sleep(1)
        controlar_via_principal(cruzamento)
        semaforo.fechar_semaforo(cruzamento)
        sleep(1)
        controlar_via_aux(cruzamento)


def iniciar_controle_cruzamento(cruzamento, tipo = None):
    semaforo.iniciar_semaforo(cruzamento)

    botao.iniciar_botao(cruzamento['botao_pedestre1'])
    botao.iniciar_botao(cruzamento['botao_pedestre2'])
    verifica_carro.verificar_carro(cruzamento['sensor_via_auxiliar1'], 'presenca')
    verifica_carro.verificar_carro(cruzamento['sensor_via_auxiliar2'], 'presenca')
    verifica_carro.verificar_carro(cruzamento['sensor_via_principal1'], 'presenca')
    verifica_carro.verificar_carro(cruzamento['sensor_via_principal2'], 'presenca')
    verifica_carro.verificar_carro(cruzamento['sensor_via_auxiliar1'], 'velocidade')
    verifica_carro.verificar_carro(cruzamento['sensor_via_auxiliar2'], 'velocidade')
    verifica_carro.verificar_carro(cruzamento['sensor_via_principal1'], 'velocidade')
    verifica_carro.verificar_carro(cruzamento['sensor_via_principal2'], 'velocidade')

    controlar_semaforo(cruzamento)