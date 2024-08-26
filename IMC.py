def calcular_imc(peso, altura):
  """Calcula o IMC e retorna a classificação."""
  imc = peso / (altura ** 2)

  if imc < 18.5:
    return f"Seu IMC é {imc:.2f}. Você está abaixo do peso."
  elif imc < 25:
    return f"Seu IMC é {imc:.2f}. Você está no peso ideal."
  elif imc < 30:
    return f"Seu IMC é {imc:.2f}. Você está com sobrepeso."
  else:
    return f"Seu IMC é {imc:.2f}. Você está obeso."

# Entrada do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Chamada da função e impressão do resultado
print(calcular_imc(peso, altura))