pessoas_maxima = 7
peso_maximo = 560.0

p_inicial = 0
total_peso = 0.0

while True:
    peso = float(input()) 

    if peso == 0 or p_inicial >= pessoas_maxima or total_peso + peso > peso_maximo:
        break

    p_inicial += 1
    total_peso += peso

print(p_inicial)
print(f"{total_peso:.1f}") 