import statistics

# Função para validar a entrada, garantindo que seja um número inteiro
def obter_numero_inteiro(indice):
    while True:
        try:
            numero = int(input(f"Digite o {indice}º número inteiro: "))
            return numero
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

# Lista para armazenar os números fornecidos pelo usuário
numeros = []

# Solicitar ao usuário 5 números inteiros com validação
for i in range(1, 6):
    numero = obter_numero_inteiro(i)
    numeros.append(numero)

# Calcular o maior, menor, soma, média, mediana, e contagem de positivos e negativos
maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = soma / len(numeros)
mediana = statistics.median(numeros)
positivos = len([num for num in numeros if num > 0])
negativos = len([num for num in numeros if num < 0])

# Exibir os resultados
print("\nResultados:")
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"A soma de todos os números é: {soma}")
print(f"A média dos números é: {media:.2f}")
print(f"A mediana dos números é: {mediana}")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
