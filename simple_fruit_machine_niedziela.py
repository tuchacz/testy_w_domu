# Napisz skrypt symulujący uproszczone działanie gry losowej "jednoręki bandyta",
# w tym celu:
# • za każdym "pociągnięciem" losuj 3 litery ze zbioru od A do E,
# • kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
# • wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
# • przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
# większą liczbę liter.


# na zajęciach program simple_fruit_machine
#
# print(ord("A"))  # reprezentacja litery jako cyfry
# print(chr("65"))  # przekształcenie w odrotną stronę

import random

FIRST_SYMBOL = "A"
LAST_SYMBOL = "H"
NUMBER_OF_LETTERS = 5

def draw_letter():
    return chr(random.randint(ord(FIRST_SYMBOL), ord(LAST_SYMBOL)))  # losuj z zakresu od 65 do 69 jako reprezentaw


# wylosuj cały rząd liter

def draw_row():
    return [draw_letter() for i in range(NUMBER_OF_LETTERS)]


# kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
def check(row):
    first_element = row[0]
    for element in row: # iteracja po liście
        if element != first_element:
            return False
    return True


# wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
counter = 1
while True:
    row = draw_row()
    print(row, counter)
    if check(row):
        break
    counter += 1

# przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
# większą liczbę liter

print(draw_letter())
print(draw_row())
# print(check(["A", "A", "A"]))
