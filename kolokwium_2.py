# Napisz skrypt pobierający od użytkownika dowolną liczbę słów. Brak podania słowa (naciśnięty sam enter) oznacza koniec wprowadzania słów. Wyświetl zgromadzone słowa. Przykład działania skryptu:
#
# Podaj słowo: kot <enter>
# Podaj słowo: chomik <enter>
# Podaj słowo: <enter>
#
# Podano słowa: [kot, chomik]

a = int(input("Podaj ilośc słów: "))

lista=[]

for i in range(a):
    i = input("Podaj słowo: ")
    lista.append(i)
    if i == str():
        break
print(lista)
