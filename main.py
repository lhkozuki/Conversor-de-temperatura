# Conversor de temperatura

#Usuário seleciona o tipo de conversão
while True:
    print("---------------")
    print("@ Conversor de temperatura")
    print("---------------")
    print("1 - Conversão de Celsius para Fahrenheit:")
    print("2 - Conversão de Fahrenheit para Celsius:")
    print("3 - Sair")

    try:
        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            celsius = float(input("Digite a temperatura em Celsius: "))
            #Variável fahrenheit e conversão
            fahrenheit = (celsius*1.8)+32
            #Exibe o resultado formatado
            print(f"{celsius:.1f}°C equivale a {fahrenheit:.1f}°F")

        elif opcao == 2:
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            #Variável celsius e conversão
            celsius = (fahrenheit-32)/1.8
            #Exibe o resultado formatado
            print(f"{fahrenheit:.1f}°F equivale a {celsius:.1f}°C")

        elif opcao == 3:
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")

    except ValueError:
            print("Entrada inválida! Digite um número válido.")