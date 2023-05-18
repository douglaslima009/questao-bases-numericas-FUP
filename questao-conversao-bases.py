def decimal_para_binario(decimal):
    return bin(decimal)[2:]

def binario_para_decimal(binario):
    return int(binario, 2)

def decimal_para_hexadecimal(decimal):
    return hex(decimal)[2:].upper()

def exibir_menu():
    print("Menu:")
    print("1 - Converter um número Decimal para Binário")
    print("2 - Converter um número Binário para Decimal")
    print("3 - Converter um número Decimal em Hexadecimal")
    print("0 - Encerrar")

def main():
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            decimal = int(input("Digite um número decimal: "))
            binario = decimal_para_binario(decimal)
            print(f"O número binário correspondente é: {binario}")
        elif opcao == "2":
            binario = input("Digite um número binário: ")
            decimal = binario_para_decimal(binario)
            print(f"O número decimal correspondente é: {decimal}")
        elif opcao == "3":
            decimal = int(input("Digite um número decimal: "))
            hexadecimal = decimal_para_hexadecimal(decimal)
            print(f"O número hexadecimal correspondente é: {hexadecimal}")
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, digite uma opção válida.")

if __name__ == "__main__":
    main()
