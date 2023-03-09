# ciąg fibonacciego
# 1 1 2 3 5 8 13 21 34...

def fib(n):  # n - numer elementu ciągu
    if n < 1:  # sprawdzenie żeby nie było zera
        return None
    if n < 3:
        return 1

    el1 = el2 = 1  # sytuacja startowa
    sum = 0
    for i in range(3, n + 1):  # pętla od elementu 3
        sum = el1 + el2
        el1, el2 = el2, sum # zmiana elementu
    return sum

print(fib(5))
print()

# funkcja wypisująca liczby z określonego zakresu zakresu
for n in range(1,101):
    print(n, "->", fib(n))