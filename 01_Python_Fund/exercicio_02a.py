'''
Substituindo caractere repetido
Escreva um programa Python para obter uma string de uma determinada string em que todas as 
ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere
Ex:
fifa 23 → fi#a 23
restart→ resta#t
'''

texto = input("Digite uma string: ")
primeiro_caractere = texto[0]
resultado = primeiro_caractere + texto[1:].replace(primeiro_caractere, '$')
print("String resultante:", resultado)  

