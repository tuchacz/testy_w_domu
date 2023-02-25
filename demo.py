"""a = 1
b = 4

# printowanie klasyczne
print("a = ", a, "b = ", b)

# zamienić wartości zmiennych
tmp = a
a = b  # bo int jest niezmienne stąd tmp
b = tmp

print("a = ", a, "b = ", b)

# lub alternatywnie
a, b = b, a
print("a = ", a, "b = ", b)
"""

"""# zamiana dwóch elementów w liście
numbers = [1, 2, 3]
numbers[0], numbers[1] = numbers[1], numbers[0]
print(numbers)

"""
"""
letters = ["A", "C", " ", "B"]
print(ord("A"),ord("C")) # zdolnośc do sortowania znaków bierze się stąd że przypisana jest tutaj od[powiednia liczba w tym przypadku 65 i 67

print(ord("a"),ord("A")) # małe litery mają większe wartości odpowiedników liczbowych.
# stąd jest porządkowanie dużych liczb a potem małych wynika to z ascii table
print(letters)  # lista jest typem uporządkowanym
# sortowanie
letters.sort()
print(letters)
# reverse
letters.sort(reverse=True)
print(letters)
"""

"""
# lista jako typ referencyjny

list_1 = [9] # nazwa
list_2 = list_1 # lista 2 do niej podstawiam lista 1 wskazują obie listy na ten sam obszar pamięci
# stąd też podstawienie do listy 1 czy dwa daje wynik ten sam
# lista jest jedna są tylko dwie nazwy
list_2[0] = 13 # podstawienie 13

print(list_2)# wynik 13 
print(list_1) # wybik 13 też będzie w liście l chociaż zmiana nastąpiła tylko w obręcie listy 2 

"""

"""
# slicing
list_1 = [9]
list_2 = list_1[:]  # tworzenie kopii ze wszystkimi elementami lub [start:end]
# list_2 = [list_1]
# tworzy się dwie niezależne listy i nazwy
list_2[0] = 13 #
print(list_2)
print(list_1)
"""
"""
# Tłumaczenie slicing
numbers = [10, 8, 6, 4, 2]
new_numbers = numbers[1:3] # wycinek jakieś cześci
print(numbers)
print(new_numbers)

# indeksowanie ujemne czyli od tyłu zaczynamy -1
#          -5  -4 -3 -2 -1
numbers = [10, 8, 6, 4, 2]
new_numbers = numbers[-4:-2] # wycinek jakieś cześci zawsze idziemy od lewej do prawej strony
print(numbers)
print(new_numbers)

#kopiowanie całości
new_numbers = numbers[:]
new_numbers = numbers[0:len(numbers)] # jako długość listy
print(new_numbers)
"""
"""
# usuwanie, czyli wycinki
numbers = [10, 8, 6, 4, 2]

del numbers[1:3] # czesc elemetów

print(numbers)

#
numbers = [10, 8, 6, 4, 2]

del numbers[:] # wszystkie elemetów

print(numbers)

#
numbers = [10, 8, 6, 4, 2]

del numbers # wszystkie elemetów

print(numbers) # nie ma takie już listy po usunięciu

"""
"""
#sprawdzanie czy jest element z zbiorze
numbers = [10, 8, 6, 4, 2]

print(5 in numbers) # wynik False bo nie ma w liście
print(7 not in numbers) # sprawdza negacje True bo nie ma w liscie

"""
"""
# list comprehension wprowadzanie danych za pomocą

numbers = []
for i in range(1,1001):
    numbers.append(i)

print(numbers)

# alternatywnie za pomocą wyrażeń listowych
numbers = [i for i in range(1,1001)] # jednolinijkowy zapis
print(numbers)

# alternatywnie za pomocą wyrażeń listowych
numbers = [99 for i in range(1,1001)] # jednolinijkowy zapis jedna liczba taka sama
print(numbers)

# alternatywnie za pomocą wyrażeń listowych
numbers = [i**2 for i in range(1,101)] # jednolinijkowy zapis lażdy element podniesiony do kwadratu
print(numbers)

# instukcja warunkowa
numbers = [i**2 for i in range(1,101) if i %2 ==0] # interesują nas liczbyb parzyste
print(numbers)
"""
"""
# dowiedzeić się ile liczb w przedziale 1-300 które dzielą się przez 3 i 7
numbers = [i for i in range(1, 301) if i % 3 == 0 and i % 7 == 0]
print(numbers)
print("Liczba liczb w przedziale =", len(numbers)) # zliczaj liczby

#alternatywnie w jednej linii
print("Liczba liczb w przedziale =", len([i for i in range(1, 301) if i % 3 == 0 and i % 7 == 0]))
"""
"""
# listy w listach zagnieżdżanie

numbers = [1, 2, 3]
l2 = numbers # to jest przypisanie
l2 = [numbers, numbers] # to jest zagnieżdzenie listy w liście

print(numbers)
print(l2)
"""
#slicing
numbers = [1, 2, 3]

matrix = [numbers[:], numbers[:]] #kopiowanie

numbers[0]=99

matrix[0][0] = 99 # modyfikacja w obrębie macierzy

print(matrix)
