def verificar_ano_bissexto(ano):
    if ano % 400 == 0:
        return True, f"O ano {ano} é divisível por 400, portanto, é bissexto e tem 366 dias."
    if ano % 100 == 0:
        return False, f"O ano {ano} é divisível por 100 mas não por 400, portanto, não é bissexto e tem 365 dias."
    if ano % 4 == 0:
        return True, f"O ano {ano} é divisível por 4 mas não por 100, portanto, é bissexto e tem 366 dias."
    return False, f"O ano {ano} não é divisível por 4, portanto, não é bissexto e tem 365 dias."
def main():
    print("Este programa determina se um ano é bissexto de acordo com o calendário gregoriano.")
    ano = int(input("Por favor, insira o ano que deseja verificar: "))
    bissexto, mensagem = verificar_ano_bissexto(ano)
    print(mensagem)
if __name__ == "__main__":
    main()