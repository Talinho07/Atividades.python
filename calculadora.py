def fatorial_while(numero):
  """Calcula o fatorial de um número utilizando o loop while.

  Args:
    numero: O número para o qual o fatorial será calculado.

  Returns:
    O fatorial do número.
  """

  if numero < 0:
    return "Fatorial não definido para números negativos."
  elif numero == 0:
    return 1
  else:
    fatorial = 1
    contador = 1
    while contador <= numero:
      fatorial *= contador
      contador += 1
    return fatorial

# Obtendo o número do usuário
numero = int(input("Digite um número para calcular o fatorial: "))

# Chamando a função e imprimindo o resultado
resultado = fatorial_while(numero)
print(f"O fatorial de {numero} é {resultado}")