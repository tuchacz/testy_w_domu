"""# Korzystając z rekurencji wypisz na ekranie tabliczkę mnożenie do 100.

def recursion(el1, el2):
    if el1 > 10 or el2 > 10:
        return None
    print(result)
    el1 = el2 = 1
    result = 0
    for i in range(10)
        result = el1 * el2
    recursion(el1, el2)

print(recursion(1,2))


for n in range(1,10):
    print(n, "->", recursion(n))


el1 = el2 = 1  # sytuacja startowa
    sum = 0
    for i in range(3, n + 1):  # pętla od elementu 3
        sum = el1 + el2
        el1, el2 = el2, sum # zmiana elementu
    return sum


for element in number:
    result = element ** power
    results.append(result)
return results


def recursion(el1,el2):
    if el1 > 20 or el2 > 10:
        return
    result = 0
    for i in range(1,10)
        result = el1*el2 # powtórne wywołanie funkcji aż do 20 i zapętlanie nastąpi
    print(result)
    recursion(number)

recursion(10)
"""


# na zajęciach multiplication table

def show_operation(a, b):  # wywołanie funkcji w funkcji
    print(a, "x", b, "=", a * b)
    if a == 10 and b == 10:  # wyłapujemy sutyacje skrajną
        return
    elif a == 10:
        show_operation(1, b + 1)  #
    else:
        show_operation(a + 1, b)


show_operation(1, 1)
