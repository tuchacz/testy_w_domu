# Napisz skrypt pobierający od użytkownika serię liczb całkowitych, a
# następnie wyświetl je w kolejności malejącej pozbywając się wcześniej
# duplikatów.
"""
a = int(input("podaj ilośc liczb do listy: "))
number_choice = []

for i in range(a):
    i = int(input("podaj liczbę: "))
    number_choice.append(i)
print(number_choice)

equal = True  # czy była zamiana

while equal:  # pętla się wykonuje dopóki będzie True
    equal = False  # jeżeli będzie false to zakończy pętlę
    for i in range(len(number_choice) - 1):  # przejść tyle ile jest elementów w liście minus 1
        if number_choice in number_choice:
            del number_choice[i]
            equal = True

number_choice.sort(reverse=True)
print(number_choice)
"""

# na zajęciach
numbers = []
numbers_total = int(input("Podaj liczbę elementów zboru: "))

for i in range(numbers_total):
    number = int(input("Podaj " + str(i + 1) + " element zboru: "))
    numbers.append(number)  # numbers.append(int(input("Podaj " +str(i+1) + " element zboru: ")))

numbers.sort(reverse=True)

numbers_without_duplicates = []
for number in numbers:
    if number not in numbers_without_duplicates:
        numbers_without_duplicates.append((number))

print(numbers_without_duplicates)
