def soma_pares_ate(numero):
  """Calcula a soma dos números pares até um determinado número.

  Args:
    numero: O número limite até onde a soma será calculada.

  Returns:
    A soma dos números pares.
  """

  soma = 0
  contador = 2
  while contador <= numero:
    soma += contador
    contador += 2
  return soma

# Obtendo o número do usuário
numero = int(input("Digite um número: "))

# Chamando a função e imprimindo o resultado
resultado = soma_pares_ate(numero)
print(f"A soma dos números pares até {numero} é: {resultado}")