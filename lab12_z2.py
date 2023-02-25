# Napisz skrypt obliczający obwód, pole powierzchni i długość przekątnej dla
# prostokątów o następujących długościach boków:
# • 4 i 5,
# • 2678 i 5678,
# • 344555 i 788998
"""
a = 4
b = 5
c = 2678
d = 5678
e = 344555
f = 788998

lista = [4, 5, 2678, 5678, 344555, 788998]

def obwod(first_number, second_number):
    return 2 * first_number + 2 * second_number
result = obwod(lista[0],lista[1])
print(result)

def pole(first_number, second_number):
    return first_number * second_number
result = pole(lista[0],lista[1])
print(result)

def przeciw(first_number, second_number):
    return (first_number**2 + second_number**2)**(0.5)
result = przeciw(lista[0],lista[1])
print(result)
"""


# na zajęciach
def perimeter(a, b):
    return 2 * a + 2 * b


def surface_area(a, b):
    return a * b


def diagonal_length(a, b):
    return (a ** 2 + b ** 2) ** (0.5)


def show_result(a, b):
    print("Prostokąt o bokach ", a, "i", b)
    print("Obwód: ", perimeter(a, b))
    print("Pole powierzchni: ", surface_area(a, b))
    print("Długość przekątnej: ", diagonal_length(a, b))
    print()

show_result(4,5)
show_result(2678,5678)
show_result(344555,788998)