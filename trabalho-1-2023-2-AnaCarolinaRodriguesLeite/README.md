[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11988581&assignment_repo_type=AssignmentRepo)
# Trabalho 1 (2023-2)

Trabalho 1 da disciplina de Fundamentos de Sistemas Embarcados (2023/2)

## 1. Objetivos

Este trabalho tem por objetivo a criação de um sistema distribuído para o controle e monitoramento de um grupo de cruzamentos de sinais de trânsito. O sistema deve ser desenvolvido para funcionar em um conjunto de placas Raspberry Pi com um ***servidor central*** responsável pelo controle e interface com o usuário controlador e ***servidores distribuídos*** para o controle local e monitoramento dos sinais do cruzamento junto aos respectivos sensores que monitoram as vias. Dentre os dispositivos envolvidos estão: o controle de temporizaçãio e acionamento dos sinais de trânsito, o acionmento de botões de passagens de pedestres, o monitoramento de sensores de passagem de carros bem como a velocidade da via e o avanço de sinal vermelho.

O vídeo explicativo dessa atividade pode ser vista [aqui](https://youtu.be/5nnLyXrGQrc).

## Execução do Projeto

### Servidor Central
*  Para o funcionamento do projeto, deve-se, primeiramente, inicializar o servidor central. Portanto, acesse o diretório do servidor central:
```
cd FSE_2023_2/central
```
* Execute o seguinte comando:
```
python3 main.py
```
* E depois rode o comando, para adentrar no menu:
```
python3 main.py HOST + PORTA_CRUZAMENTO
```

### Servidore distribuído do cruzamento 1
* Após a inicialização do servidor central, acesse o diretório do servidor distribuído:
```
cd FSE_2023_2/distribuido
```
* Execute o comando abaixo. O código, então, irá inicializar o cruzamento 1 da placa em:
```
python3 dist1.py HOST + PORTA_CRUZAMENTO1
```


### Servidor distribuído do cruzamento 2
* Após a inicialização do servidor central, acesse o diretório do servidor distribuído:
```
cd FSE_2023_2/distribuido
```
* Execute o comando abaixo. O código, então, irá inicializar o cruzamento 2 da placa:
```
python3 dist2.py HOST + PORTA_CRUZAMENTO2
```

## Observações
Alguns dos itens requisitados pelo enunciado não foram implementados a tempo. São eles:
- Não foi adicionado o alarme para quando ocorre alguma infração.
