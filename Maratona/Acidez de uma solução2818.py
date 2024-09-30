ph = float(input("Digite o pH da solucao:\n"))

if ph < 0 or ph >14:
    print("Valor do pH deve estar entre 0 e 14")

else:
    if ph == 7.0:
      print("Solucao neutra") 
    elif ph < 7:
      print("Solucao acida")
    elif ph > 7:
      print("Solucao basica")
