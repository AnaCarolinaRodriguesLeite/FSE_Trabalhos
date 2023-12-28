import mensagem

class Menu:
    def __init__(self):
        self.opcao = 0

    def menu_principal(self):
        while True:
            print("======================= MENU =====================\n")
            print("1 - Monitoramento dos semáforos")
            print("2 - Acionamento do modos noturno ou de emergência\n")
            # print("3 - Informações por cruzamento\n")
            self.opcao  = int(input("Selecione uma das opções: "))
            if (self.opcao  == 1):
                self.painel_monitoramento()
            elif (self.opcao  == 2):
                self.menu_modos()
            # elif(self.opcao == 3):
            #     self.menu_informacoes()
    
    def menu_modos(self):
        while True:
            print("==================== MENU =================\n")
            print("1 - Modo noturno")
            print("2 - Modo emergência")
            print("3 - Voltar ao meu principal\n")
            self.opcao = int(input("Selecione uma das opções: ")) 
            if (self.opcao == 1): 
                self.menu_modo_noturno()     
            elif (self.opcao == 2): 
                self.menu_modo_emergencia()
            elif(self.opcao == 3):
                self.menu_principal()

    def menu_informacoes(self):
        while True:
            print("================ Informações =============\n")
            print("1 - Informações de quantidade de carros nas duas via e velocidade media:\n")
            print("2 - Voltar ao meu principal\n")
            self.opcao = int(input("Selecione uma das opções: "))
            if (self.opcao == 1):
                mensagem.imprimir_mensagem(1)
            elif (self.opcao == 2):
                self.menu_principal()
    
    def menu_modo_noturno(self):
        while True:
            print("================ MODO NOTURNO =============\n")
            print("1 - Cruzamentos 1 e 2")
            print("2 - Voltar ao meu principal\n")
            self.opcao = int(input("Selecione uma das opções: "))
            if (self.opcao == 1):
                mensagem.enviar_mensagem(1, 0, 1)
                self.desativar_modo_noturno()
            elif (self.opcao == 2):
                self.menu_modos()

    def menu_modo_emergencia(self):
        while True:
            print("============ MODO EMERGÊNCIA ============\n")
            print("1 - Todos cruzamentos\n")
            print("2 - Voltar ao meu principal\n")
            self.opcao = int(input("Selecione uma das opções: "))
            if (self.opcao == 1):
                mensagem.enviar_mensagem(0, 1, 1)
                self.desativar_modo_emergencia()
            elif (self.opcao == 2):
                self.menu_modos()
    
    def desativar_modo_noturno(self):
        while True:
            print("Deseja desativar o modo noturno?")
            print("1 - Sim\n")
            opcao_destivar = int(input("Selecione um para desativar: "))
            if (opcao_destivar == 1):
                mensagem.enviar_mensagem(0, 0, self.opcao)
                self.menu_modo_noturno()

    def desativar_modo_emergencia(self):
        while True:
            print("Deseja desativar o modo de emergência?")
            print("1 - Sim\n")
            opcao_destivar = int(input("Selecione um para desativar: "))
            if (opcao_destivar == 1):
                mensagem.enviar_mensagem(0, 0, self.opcao)
                self.menu_modo_noturno()

    def painel_monitoramento(self):
        print("========= MONITORAMENTO ==========\n")
        print("Monitoramento acionado!!!!!\n")
        print("1 - Para desativar o monitoramento\n")
        mensagem.acionar_monitoramento(1)

        while True:
            opcao_destivar = int(input(""))
            if (opcao_destivar == 1):
                mensagem.acionar_monitoramento(0)
                self.menu_principal()