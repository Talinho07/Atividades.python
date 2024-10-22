def C_para_F(celsius):
    return (celsius * 9/5) + 32
def C_para_K(celsius):
    return celsius + 273.15

def F_para_C(fahrenheit):
    return (fahrenheit - 32) * 5/9
def F_para_K(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.1

def K_para_C(kelvin):
    return kelvin - 273.15
def K_para_F(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def menu():
    print("Conversor de Temperatura com míltiplas escalas")
    print("1. Converta de Celsius para Fahrenheit")
    print("2. Converta de Celsiud para Kelvin")
    print("3. Converta de Fahreneit para Celsius")
    print("4. Converta de Fahrenheit para Kelvin")
    print("5. Converta de Kelvin para Celsius")
    print("6. Converta de Kelvin para Fahrenheit")
    print("7. Sair")

while True:
    menu()
    opcao = int(input("escolha uma opção: "))

    if opcao == 7:
        print("Saindo do programa")
        break
    temperatura = float(input("Digite o valor da temperatura: "))

    if opcao == 1:
        print(f"{temperatura}°C é igual a {C_para_F(temperatura)}°F")
    elif opcao == 2:
        print(f"{temperatura}°C é igual a {C_para_K(temperatura)}K")
    elif opcao == 3:
        print(f"{temperatura}°F é igual a {F_para_C(temperatura)}°C")
    elif opcao == 4:
        print(f"{temperatura}°F é igual a {F_para_K(temperatura)}K")
    elif opcao == 5:
        print(f"{temperatura}K é igual a {K_para_C(temperatura)}°C")
    elif opcao == 6:
        print(f"{temperatura}K é igual a {K_para_F(temperatura)}°F")
    else:
        print("Arquivo não encontrado")