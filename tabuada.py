def tabuada_while(numero):
  """Imprime a tabuada de um número utilizando o loop while.

  Args:
    numero: O número para o qual a tabuada será gerada.
  """

  contador = 1
  while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1

# Obtendo o número do usuário
numero = int(input("Digite um número para ver sua tabuada: "))

# Chamando a função para gerar a tabuada
tabuada_while(numero)