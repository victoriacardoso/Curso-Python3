nome = input("Informe seu nome: ")

tamanho_nome = len(nome)
if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print("Seu nome é curto.")
    elif 5 <= tamanho_nome <= 6:
        print("Seu nome é normal.")
    else:
        print("Seu nome é muito grande.")
else:
    print("Digite mais de um dígito.")