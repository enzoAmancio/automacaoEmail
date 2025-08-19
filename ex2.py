'''
Um sistema precisa registrar as entradas de visitantes. 
Peça o nome e a idade de cada visitante até que seja digitado "sair".

Só permita a entrada de pessoas com 18 anos ou mais.

Exiba uma mensagem personalizada para cada visitante aceito ou recusado.
'''

entrada = str(input("Digite seu nome (ou sair para encerrar): "))


while (entrada != 'sair'):
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("Pode entrar")
    else:
        print("Barrado")
    entrada = str(input("Digite seu nome (ou sair para encerrar): "))
        