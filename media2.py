#algoritimo media: criar um algoritmo que leia 4 notas
#e apresente uma media final

print("olá! vamos ver qual será sua media.")

nota1 = float(input("digite sua primeira nota:"))
nota2 = float(input("digite sua segunda nota:"))
nota3 = float(input("digite sua terceira nota:"))
nota4 = float(input("digite sua quarta nota:"))

media = (nota1 + nota2 + nota3 + nota4)/4

print("sua média foi", media)
if(media >= 80) :
    print("parabens, voce foi aprovado")
else:
    print("que pena, voce está a baixo da média")
    
    print("continue o bom trabalho")

