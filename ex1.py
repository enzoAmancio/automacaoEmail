'''
Um caixa eletrônico só tem notas de R$100, R$50, R$20 e R$10.
Peça ao usuário um valor inteiro e calcule a menor quantidade de cédulas
possível para aquele saque.
Use laços e condicionais para calcular e exibir a quantidade de cada cédula.
'''

caixaEletronico = [100, 50, 20, 10]

entrada = int(input("Digite quanto você quer sacar "))

if entrada <= 0:
    print("Valor impossivel, tente novamente.")
else:
    for nota in caixaEletronico:
        quantidade = entrada // nota
        if quantidade > 0:
            print(f"{quantidade} cédulas de R${nota}")
            entrada -= quantidade * nota
    if entrada > 0:
        print(f"Não foi possível sacar o valor restante de R${entrada}.")
        