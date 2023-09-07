hora_str = input("Informe a hora em números inteiros: ")

try:
    hora_int = int(hora_str)

    if 0 <= hora_int <= 11:
        print("Bom dia!")
    elif 12 <= hora_int <= 17:
        print("Boa tarde!")
    elif 18 <= hora_int <= 23:
        print("Boa noite!")
    else:
        print("hora inválida.")
except:
    print("Você não digitou inteiros.")
