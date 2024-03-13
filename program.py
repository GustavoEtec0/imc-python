# num = int(input('Digite um numero: '))

# if num > 10 :
#     print(num, 'é maior que 10!')
# if num == 10 :
#     print(num,'!')
# if num < 10 :
#     print(num, 'é menor que 10!')

# NHT =  int(input('Digite o numero de horas trabalhadas: '))

# VPH =  int(input('Digite o valor pogo por horas: '))

# SB =  NHT * VPH

# SL = 0

# if SB < 1000 :
#     SL = SB - (SB * 0.05)
#     print('seu salario liquido é:',SL)
# elif SB >= 1000 and SB <= 2000 :
#     SL = SB - (SB * 0.1)
#     print('seu salario liquido é:',SL)
# else:
#     SL = SB - (SB * 0.15)
#     print('seu salario liquido é:',SL)

nome = input("Qual é o seu nome? " )
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua Altura: "))

imc = (peso / (altura * altura))

print(nome,"seu IMC é:", imc)

if imc < 18.5:
	print("voce esta abaixo do peso")
elif imc < 24.9:
	print("peso normal (parabéns)")
elif imc < 29.9:
	print("levemente acima do peso")
elif imc < 34.9:
	print("obesidade 1")
elif imc < 39.9:
	print("obesidade 2 (severa)")
else:
	print("obesidae 3 (mórbida)")