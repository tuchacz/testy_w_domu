# generator liczb od 1 do 99
import random

def generate_numbers(total_numbers):
    numbers = []
    for i in range(total_numbers):
        numbers.append(random.randint(1,99))
    return numbers # zwróć listę z liczbami

print(generate_numbers(10))
print(generate_numbers(100))
print(generate_numbers(2323))
