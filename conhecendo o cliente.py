totalVendas = 0
totalVista = 0.0
totalCartao = 0.0
idadeJovem = float('inf')
maiorCompra = 0.0
somaVista = 0.0
contadorVista = 0

while True:
    idade = int(input()) 
    valorCompra = float(input())  
    tipoPagamento = input() 
    continuar = input()  


    totalVendas += 1
    if tipoPagamento == 'V':
        totalVista += valorCompra
        somaVista += valorCompra
        contadorVista += 1
    else:
        totalCartao += valorCompra


    if idade < idadeJovem:
        idadeJovem = idade

    if valorCompra > maiorCompra:
        maiorCompra = valorCompra

    if continuar == 'N':
        break

mediaVista = somaVista / contadorVista if contadorVista > 0 else 0.0

print(totalVendas)
print(f"{totalVista:.2f}")
print(f"{totalCartao:.2f}")
print(idadeJovem if idadeJovem != float('inf') else 0)  # Se não houver cliente, retorna 0
print(f"{maiorCompra:.2f}")
print(f"{mediaVista:.2f}")