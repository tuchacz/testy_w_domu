# # krotki są niezmienne
#
# #zapis
# numbers = (1, 2, 3)

"""# zapis alternatywny interpretuje to jako krotke
numbers = 1, 2, 3
# pusta krotka
numbers =()

numbers = (1,) # gdy chcemy wyświelić tylko jedną wartość bo innaczej będzie trakowanny jako elemnet w nawiasie

print(numbers[-1])

#printowanie
for i in numbers:
    print(i)

# wycinek jako kopię
print(numbers[1:2])

# kopia całości
print(numbers[:])
"""

# generowanie za pomocą tuple jako generatora wyrażeń
"""
numbers = tuple(x for x in range(10))
print(numbers)
"""

# różnice pomiędzy listami a krotkami
# są zniemnienne
"""
numbers = tuple(x for x in range(10))

print(numbers)

numbers[0] = 9999 # krotki są nie zmienne
del numbers[0] # nie da się usunąć elementu

del numbers # możńa usunąć caął krotkę
print(numbers)
print(numbers+numbers) # nie da się dodwać do tych wartości ani mnożyć 
print(numbers*2)

"""
"""
# konwersja listy na krotkę
numbers = [1,2,3]
numbers =tuple(numbers)
print(numbers)
print()
numbers = "Ala ma kota"
numbers =tuple(numbers)
print(numbers)

"""

