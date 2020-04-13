lista = [1,3,-1,15,9]

listaDobles = map(lambda x: x*2, lista)

listaPares= filter(lambda x: x % 2 == 0, lista)


print(list(listaDobles))

print(list(listaPares))
