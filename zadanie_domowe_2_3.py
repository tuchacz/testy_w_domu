"""Napisz program pobierający od użytkownika liczbę całkowitą i zwracający
liczbę jedynek w ciągu bitów reprezentujących tę liczbę."""

number=int(input("Podaj liczbę całkowitą: "))
print(bin(number))

counter = 0
for i in bin(number):
    if i in "1":
        counter +=1
print("W zapisie bitowym liczby " + str(number) + " znajduje się następująca ilośc jedynek: " + str(counter))

