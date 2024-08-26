def eh_bissexto(ano):
  """Verifica se um ano é bissexto."""
  if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    return f"O ano {ano} é bissexto."
  else:
    return f"O ano {ano} não é bissexto."

# Entrada do usuário
ano = int(input("Digite um ano: "))

# Chamada da função e impressão do resultado
print(eh_bissexto(ano))