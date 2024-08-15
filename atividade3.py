"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

print (40 * '-')
print ('Olá!')

try: 
    numero = int(input('Digite um numero inteiro:')) # Convertendo o input em um numero inteiro
    if numero %2 == 0: # checando se o numero é par
        print (f'Seu numero {numero} é par.')
    else: # Caso o numero for impar
        print(f'Seu numero {numero} é impar.')
except ValueError: # Caso não for um numero inteiro
    print('Você não digitou um numero inteiro.')

print ('Obrigado!')
print (40 *'-')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

print (40 * '-')
nome = input ('Olá, qual é o seu nome? ')
try:
    hora = int(input('Me informe a hora com dois digitos por favor:'))
    if 0 <= hora <= 11:
        print (f'Bom dia, {nome}! :D')
    elif 12 <= hora <= 17:
        print (f'Boa tarde, {nome}! :P')
    elif 18 <= hora <= 23:
        print (f'Boa noite, {nome}! zzz')
    else:
        print ('Digite apenas numeros de 0 a 23')
except ValueError:
    print ('Digite apenas numeros de 0 a 23')
print ('Obrigado!')
print (40 * '-')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
print (40 * '-')
nome = input ('Olá, qual é o seu primeiro nome? ')
if len(nome) <= 4:
        print ('Seu nome é curto!')
elif 4 < len(nome) <= 6:
        print ('Seu nome é normal!')
elif 6 < len(nome) :
        print ('Seu nome é grande!')

print('Obrigado!')
print(40 * '-')
