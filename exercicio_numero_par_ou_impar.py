num_str = input("Digite um número inteiro: ")

try:
    num_int = int(num_str)
    if num_int % 2 == 0:
        print(f"{num_int} é um número par.")
    else:
        print(f"{num_int} é um número ímpar.")

except:
    print("%s não é um número inteiro" % num_str)
