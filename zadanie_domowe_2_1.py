"""Napisz program sumujący pobrane liczby od użytkownika wg wytycznych:
• program powinien pobierać od użytkownika liczby całkowite,
• niepodanie liczby powinno zakończyć wprowadzanie danych,
• program powinien podać sumę liczb parzystych oraz sumę liczb nieparzystych."""

numbers = int(input("Podaj liczbę elementów zbioru: "))
lista = []
for i in range(numbers):
    i=float(input("Podaj liczbę a zapiszę ją do listy: "))
    if i % 1 == 0:
        print("to jest liczba całkowita")
        lista.append(i)
    elif i % 1 != 0:
        print("to nie jest liczba całkowita")
        break
print(lista)

counterp = 0
countern = 0
for number in lista:
    if number % 2 == 0:
        print(number)
        counterp +=number
    elif number % 2 == 1:
        print(number)
        countern +=number
print("suma liczb parzystych: ", counterp, "suma liczb nieparzystych: ", countern)

