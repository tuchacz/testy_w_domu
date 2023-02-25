# Napisz skrypt symulujący grę losową:
# • użytkownik obstawia 6 liczb z 49,
# • program losuje 6 liczb z 49,
# • użytkownik dostaje informacje o ilości trafień.

"""import random

numbers = []
number_choice = []
numbers = [i for i in range(1, 49)]
random_numbers = random.sample(numbers, 6)
for i in range(6):
    i = int(input("podaj liczbę: "))
    number_choice.append(i)
print(number_choice)
print(random_numbers)
counter = 0
for i in range(6):
    if random_numbers[i] == number_choice[i]:
        counter += 1
print(counter)

# print("ilość trafień wynosi ", len(random_numbers))
"""
import random

# na zajęciach

user_numbers = []
random_numbers = []
hit_total = 0
#pobranie liczb
for i in range(6):
    user_numbers.append(int(input("Podaj " + str(i+1) + " liczbę od 1 do 49: ")))
#losowanie liczb

random_numbers=random.sample(range(1,50),6) # losuj od 1 do 50 6 powtórzeń

#sprawdzenie czy użytkownik trafił
for number in user_numbers: #
    if number in random_numbers: # czy number jest w zbiorze random_numbers
        hit_total+=1

user_numbers.sort()
random_numbers.sort()

print(random_numbers)
print(user_numbers)
print("Trafiono:", hit_total, " liczb")