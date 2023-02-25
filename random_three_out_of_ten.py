"""# wylosuj 3 liczby

import random

random_numbers = []  # umieszczamy  liczby w liście random_numbers
counter = 3  # trzy wylosowane liczby
while counter:  # pętla będzie działąć aż do 3, jeżeli counter większe od zera, counter musi się wyzerować
    number = random.randint(1, 10)
    if number not in random_numbers:
        random_numbers.append(number)  # losuj od 1 do 10 włącznie
        counter -= 1  # counter = counter - 1 jeżeli counter dojdzie do zera to wyjdę z pętli

random_numbers.sort()
# nie mogą się powtarzać bo random tego nie sprawdza

print(random_numbers)
"""

# w funkjci random jest sample która nie wylosuje liczb takich samych

import random

numbers = [i for i in range(1,11)]
random_numbers = random.sample(numbers,3)
random_numbers.sort()

print(random_numbers)

