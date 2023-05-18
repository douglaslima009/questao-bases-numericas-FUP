#Aluno: Douglas Lima Menezes
#Engenharia de software 2023.1

def dectobin(decimal):
    return bin(decimal)[2:]
def bintodec(binario):
    return int(binario, 2)
def dectohex(decimal):
    return hex(decimal)[2:].upper()

def exibir_menu():
    print("Menu:")
    print("1 - Conversão de Decimal para Binário")
    print("2 - Conversão de Binário para Decimal")
    print("3 - Conversão de Decimal em Hexadecimal")
    print("0 - Encerrar")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            dec = int(input("Digite um número decimal: "))
            bin = dectobin(dec)
            print(f"O número decimal {dec} em binário corresponde a: {bin}")
        elif opcao == "2":
            bin = input("Digite um número binário: ")
            dec = bintodec(bin)
            print(f"O número binário {bin} em decimal corresponde a: {dec}")
        elif opcao == "3":
            dec = int(input("Digite um número decimal: "))
            hex = dectohex(dec)
            print(f"O número decimal {dec} em hexadecimal corresponde a: {hex}")
        elif opcao == "0":
            print("Encerrado.")
            break
        else:
            print("Não foi possível realizar esta operação. Por favor, digite uma opção válida.")

if __name__ == "__main__":
    main()
