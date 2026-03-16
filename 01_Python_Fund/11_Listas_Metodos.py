gameList = ["Fifa23", "Star Wars", "The Legend of Zelda", "Red Dead 2"]

# 1 Tamanho da lista
print(len(gameList))

# 2 Recupera um item pelo indice
print(gameList.index("Star Wars")) 
      
# 3 Adicionar um item no final da lista
gameList.append("GTA V")    
print(gameList) 

# 4 Ordenar a lista
gameList.sort()
# listaJogos.reverse() # Inverte a ordem da lista
print(gameList)

# 5 Copia os itens de uma lista para outra
gameReset = gameList.copy()
gameReset.remove("Fifa23")
gameReset.remove("Star Wars")
print(gameReset)

# 6 Remove todos os itens da lista
gameReset.clear()
print(gameReset)    