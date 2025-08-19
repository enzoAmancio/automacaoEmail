'''
O usuário informa a distância percorrida (em km) e a quantidade de combustível
 gasto (em litros). Calcule o consumo médio e classifique:

< 8 km/l = "Venda o carro!"

8 a 14 km/l = "Econômico"

14 km/l = "Super econômico"
'''

distancia = float(input("Digite a distância percorrida (em km): ")) 
litros = float(input("Digite a quantidade de combustível gasto (em litros): "))

consumoMedio = distancia / litros

if consumoMedio < 8:
    print("Venda o carro")
