#Aluno: Douglas Lima Menezes
#Engenharia de software 2023.1

print("Menu:")
print("1 - Converta Decimal para Binário.")
print("2 - Converta Binário para Decimal.")
print("3 - Converta Decimal em Hexadecimal.")
print("0 - Encerrar o programa.")

opcao = input("Escolha uma opção válida: ")
while opcao != "0":
    if opcao == "1":
        dec = int(input("Digite um número decimal: "))
        decorigem = dec
        bin = ""
        while dec > 0:
            resto = dec % 2
            bin = str(resto) + bin
            dec = dec // 2
        print(f"O número decimal {decorigem} corresponde ao número binário: {bin}")
    elif opcao == "2":
        bin = int(input("Digite um número binário: "))
        binorigen = bin
        dec = 0
        exp = 0
        while bin > 0:
            resto = bin % 10
            dec = dec + resto * (2 ** exp)
            bin = bin // 10
            exp = exp + 1
        print(f"O número binário {binorigen} corresponde ao número decimal: {dec}")
    elif opcao == "3":
        dec = int(input("Digite um número decimal: "))
        decorigem = dec
        hexloc = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        hex = ""
        while dec > 0:
            resto = dec % 16
            if resto >= 10:
                resto = hexloc[resto]
            hex = str(resto) + hex
            dec = dec // 16
        print(f"O número decimal {decorigem} corresponde ao número hexadecimal: {hex}")
    else:
        print("O número digitado não é uma opção válida. Por favor, digite novamente.")
    
    print("Menu:")
    print("1 - Converta Decimal para Binário")
    print("2 - Converta Binário para Decimal")
    print("3 - Converta Decimal em Hexadecimal")
    print("0 - Encerrar o programa")

    opcao = input("Escolha uma opção válida: ")
print("Encerrado.")
