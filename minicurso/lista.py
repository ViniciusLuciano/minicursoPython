l = [1, 2, 3, 4, 8]
l.append(5)

l2 = [5, 6, 7, 8]
l.extend(l2)

l.insert(0, 0)
l.remove(5)

l.pop(1)

#l.clear()

print(l.count(8))

print('index do 5: {}'.format(l.index(5)))

#print(sorted(l, reverse=True))
print(l)
l.reverse()
print(l)

print('Tamanho da lista: ', len(l))
print('Maior valor: ', max(l))
print('Menor valor: ', min(l))

