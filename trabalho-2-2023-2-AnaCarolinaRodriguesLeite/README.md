# Trabalho 2 (2023-2)

Trabalho 2 da disciplina de Fundamentos de Sistemas Embarcados (2023/2)

## Objetivos

O trabalho envolve o desenvolvimento do software que efetua o controle completo de um elevador incluindo o controle de movimentação, acionamento dos botões internos e externos e monitoramento de temperatura. O movimento do elevador é controlado à partir de um motor elétrico e a posição é sinalizada à partir de sensores de posição e um encoder.
O controle do elevador deve responder aos comandos dos usuários por meio de botões externos (andares) ou internos (painel de botões do elevador).

Botões de Entrada

Painel Interno (Térreo, 1º Andar, 2º Andar, 3º Andar, Emergência)
Andares (Sobe e/ou Desce)

# Execução
## Instalação do temperatura
Para fazer o uso do projeto, deve instalar as dependências da temperatura:

```
pip install smbus2
pip install bmp280
```

## Execução do projeto
Para executar o projeto entre na pasta src, e execute o comando abaixo:

```
python3 main.py
```

## Funcionamento do projeto
Após executar o arquivo main.py, o programa irá guiar o uso através do terminal.

Para sair do programa, basta pressionar Ctrl+C.

## Video

https://github.com/FSE-2023-2/trabalho-2-2023-2-AnaCarolinaRodriguesLeite/assets/49570180/f8b31c6f-8ba5-431b-a660-451f5f3dee53


https://github.com/FSE-2023-2/trabalho-2-2023-2-AnaCarolinaRodriguesLeite/assets/49570180/cfa31a4f-98d8-4df1-9bca-8f84d3b46d38

https://github.com/FSE-2023-2/trabalho-2-2023-2-AnaCarolinaRodriguesLeite/assets/49570180/07f76b2f-d6b6-4545-9038-0b9fcdd95c67


NOVO:
![WhatsApp-Video-2023-11-25-at-14 20 53](https://github.com/FSE-2023-2/trabalho-2-2023-2-AnaCarolinaRodriguesLeite/assets/49570180/b58592fe-8f9b-4eea-8e50-a717b176d886)


