'''
Faça um programa que calcule a tabuada de um número, 
com valores iniciais e finais informados pelo usuário
'''

numero = int(input("Tabuada de: \n")) 
inicio = int(input("Início: \n"))
fim = int(input("Fim: \n"))   

x = inicio
while x <= fim:
    print(f"{numero} x {x} = {numero * x}")
    x += 1  

