nome = "Victória Cardoso"
altura = 1.60
peso = 60.3
imc = peso/(altura ** 2)
#com concatenação e conversão
print(nome, "tem " + str(altura) + " de altura, pesa " + str(peso) + " quilos e seu IMC é " + str(imc))
#sem concatenação e conversão
print(nome, "tem", altura, "de altura,", "pesa", peso, "quilos", "e seu IMC é", imc)