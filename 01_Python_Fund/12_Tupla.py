gamesTuple = ("Fifa23", "Red Dead 2", "Star Wars", "The Legend of Zelda", "Red Dead 2")
print(gamesTuple)
print(type(gamesTuple))

exampleTuple = ("Fifa23")
exampleTuple2 = ("Fifa23",20, True)
print(type(exampleTuple2)) 
print(exampleTuple2)

# 1 Busque ois dois primeiros itens da tupla
print(gamesTuple[0:2])

# 2 Busque o último item da tupla
print(gamesTuple[-1])   

# 3 Busque jogos até uma posição
print(gamesTuple[:2])   

# 4 Busque jogos a partir de uma posição
print(gamesTuple[2:])   

# 5 Recupera um item da tupla pelo indice
print(gamesTuple.index("Fifa23 "))

# Não possibilita adicionar ou remover itens da tupla, pois é imutável
# Não possibilita ordenar a tupla, pois é imutável


