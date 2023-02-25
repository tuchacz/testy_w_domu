"""Napisz program, który wylosuje kilka serii liczb całkowitych i wyświetli je
na ekranie, przy czym:
• program zapyta użytkownika o zakres minimum oraz maksimum,
• będzie losował odpowiednie liczby z zakresu podanego przez użytkownika,
• będzie losował liczbę liczb do wylosowania z zakresu podanego przez użytkownika,
• będzie losował liczbę serii liczb do wylosowania z zakresu podanego przez
użytkownika,
• wyświetli wylosowane serie liczb."""

import random

numbers = []

numbers_number = int(input("Podaj liczbę liczb do wylosowania: "))
serie_number = int(input("Podaj liczbę serii powtórzeń: "))
bottom_range = int(input("Podaj dolny zakres: "))
upper_range = int(input("Podaj górny zakres: "))
j = 0
while True:
    j +=1
    for i in range(numbers_number):
        number = random.randint(bottom_range,upper_range)
        numbers.append(number)
    if j == serie_number:
        print("Wychodzimy z programu i wyświetlamy wyniki")
        break
print(numbers)
