# 1 1 2 3 5 8 13 21 34...

def fib(n):  # n - numer elementu ciągu
    if n < 1:  # sprawdzenie żeby nie było zera
        return None
    if n < 3:
        return 1

    return fib(n-1) + fib(n-2) # to dostaniemy element np. 3

for n in range(1,10):
    print(n, "->", fib(n))


"""
def recursion(number):
    if number == 20:
        return
    print(number)
    number+=1 # powtórne wywołanie funkcji aż do 20 i zapętlanie nastąpi
    recursion(number)
"""