primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

if primeiro_valor >= segundo_valor:
    print("Primeiro valor=", primeiro_valor,  "é maior ou igual que segundo valor=", segundo_valor)
elif segundo_valor > primeiro_valor:
    print("Segundo valor=", segundo_valor,  "é maior que primeiro valor=", primeiro_valor)

#Usando .format()
if primeiro_valor >= segundo_valor:
    print(f"{primeiro_valor=} é maior ou igual que {segundo_valor=}")
else:
    print(f"{segundo_valor=} é maior que {primeiro_valor=}")
