# reverse
numbers =[4,5,6,8,1]
print(numbers)
numbers.reverse()
print(numbers)

#sortowanie bąbelkowe
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

#int jest wypem niezmiennym

# lista jest zmienna czyli inna lista przypisana będzie zmieniać się wraz z listą zmienianą
# wycinanie slicing tworzeni enowej kopii listy
# list[start:end] pobiera od start do end-1
# modyfikacja slice nie zmieni nic w pierwotnej liście

# operato członkowstwa in not in

#wyrażenia listowe
squares = [x**2 for x in range(1,6)]
print(squares)

r_1 = [1,3,5]
r_2 = [1,4,7]

matrix = [r_1, r_2]
print(matrix)




