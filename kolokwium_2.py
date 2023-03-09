# Napisz skrypt pobierający od użytkownika dowolną liczbę słów. Brak podania słowa (naciśnięty sam enter) oznacza koniec wprowadzania słów. Wyświetl zgromadzone słowa. Przykład działania skryptu:
#
# Podaj słowo: kot <enter>
# Podaj słowo: chomik <enter>
# Podaj słowo: <enter>
#
# Podano słowa: [kot, chomik]


lista=[]
name = "dsfgsdfgsdfgd"

while name!="":
    name = input("Podaj słowo: ")
    lista.append(name)
else:
    print(lista)
