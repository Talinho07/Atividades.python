def voto_obrigatorio(idade):
  """Verifica se o voto é obrigatório, opcional ou não permitido."""
  if 16 <= idade < 18 or idade >= 65:
    return "Voto opcional."
  elif 18 <= idade <= 65:
    return "Voto obrigatório."
  else:
    return "Voto não permitido."

# Entrada do usuário
idade = int(input("Digite sua idade: "))

# Chamada da função e impressão do resultado
print(voto_obrigatorio(idade))