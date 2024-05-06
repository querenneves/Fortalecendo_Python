
'''Sintaxe

Exercício 1
Escreva um programa que imprima o seguinte texto:

Olá, mundo!
'''

print("Hello world!")

'''
Exercício 2
Escreva um programa que imprima o resultado da seguinte operação matemática:
'''
variavel_1 = 2
variavel_2 = 5

soma = variavel_1 + variavel_2

print('A soma de', variavel_1, 'mais', variavel_2, 'é', soma)


'''
Variáveis

Exercício 1

Declare uma variável chamada nome e atribua-lhe o seu nome. Em seguida, imprima o valor da variável.
'''
nome = "Queren" #string
print('O nome é:', nome)

'''
Exercício 2
Declare uma variável chamada idade e atribua-lhe a sua idade. Em seguida, imprima o valor da variável.
'''
idade = 18 #inteiro
print('A idade é:', idade)

'''
Tipos de dados

Exercício 1
Escreva um programa que declare uma variável numero do tipo int e atribua-lhe o valor 10. Em seguida, imprima o valor da variável.
'''
number = 10 #inteiro
print('O valor é:', number)

'''
Exercício 2
Escreva um programa que declare uma variável texto do tipo str e atribua-lhe a string "Olá, mundo!". 
'''
str = "Olá, mundo!" #string
print(str)

'''
Condicionais

Exercício 1
Escreva um programa que verifique se a idade de uma pessoa é maior de idade. Se for, imprima a mensagem "A pessoa é maior de idade".
 Se não for, imprima a mensagem "A pessoa é menor de idade".

'''
# Pede ao usuário para inserir a idade
idade = int(input("Digite a idade da pessoa: "))

# Verifica se a pessoa é maior de idade
if idade >= 18:
    print("A pessoa é maior de idade.")
else:
    print("A pessoa é menor de idade.")
'''
 Exercício 2
Escreva um programa que verifique se um número é par ou ímpar. Se o número for par, imprima a mensagem "O número é par".
 Se não for, imprima a mensagem "O número é ímpar".
'''
# Pede ao usuário para inserir um número
numero = int(input("Digite um número: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

'''
 Loops
 
Exercício 1
Escreva um programa que imprima os números de 1 a 10.
'''
# Loop for para imprimir números de 1 a 10
for numero in range(1, 11):  # range(1, 11) gera números de 1 até 10
    print(numero)


'''Exercício 2
Escreva um programa que imprima a tabuada de 9.
'''
# Imprime a tabuada do 9
for i in range(1, 11):  # Loop de 1 a 10
    resultado = 9 * i
    print("9 x", i, "=", resultado)
