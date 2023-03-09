"""def sum_numbers(numbers):
    sum = 0
    for element in numbers:
        sum += element
    return sum  # instrukcja return zwraca sumę


print(sum_numbers([1,2,3])) # printowanie wyników

# alternatywnie rozpisanie na czynniki pierwsze

numbers =[1,2,3]
result =sum_numbers(numbers)
print(result)

# sum_numbers(99) # wynik błąd bo element nie jest iterowalny nie jest to lista czy krotka
# aby się nie wykrzaczył to trzeba by było wprowadzić wyjątek exception
"""

"""
# zasięg zmiennych

def scope_test():
    x = 123 # tworzy zmienną lokalną i przypisuje wartość i ma zasięg fukcji

scope_test()
print(x) # x nie jest zdefiniowane bo nie ma jej globalnie, nie zadziała
"""
"""
# zadziała jeśli będzie zdefiniowana globalnie

def scope_test():
    print("w środku funkcji: " + str(x))

x =99
scope_test()
print()

# nazwa możę być nadpisywana chwilowo przez lokalną
# żadna zmienna nie nadpisuje innej zmiennej
def scope_test():
    x =123
    print("w środku funkcji: " + str(x))

x =99
scope_test()
print("na zewnątrz funkcji: " + str(x))
print()

# chcemy mieć wpływ na zmienną globalną i chcemy ją zmienić nadpisać
print("nadpisanie zmiennej globalnej")
def scope_test():
    global x
    x =123
    print("w środku funkcji: " + str(x))

x =99
scope_test()
print("na zewnątrz funkcji: " + str(x))
print()

"""

# funkcja zmieniająca wartości
"""
def change_value(n): # zrobi się kopia 7 
    print("przed zmianą: ", n)
    n +=1
    print("po zmianie: ", n)

val = 7 # nie będzie zmiany 7
change_value(val)
print(val)

# zmiana nastąpi po wprowadzeniu global do funkcji def

"""
"""
# operarcje na liście

def change_value(n): # n =val podstawienie
    print("przed zmianą: ", n)
    n = [0,0] # dla n podstawiamy [0,0] wytwarza nowy obiekt za pomącą przypisania, nie wytwarzaliśmy nowej listy
    print("po zmianie: ", n)

val = [1,2]
change_value(val)
print(val)
"""
"""print()
# operarcje na liście

def change_value(n): # n =val podstawienie
    print("przed zmianą: ", n)
    n[0] =999 # zmiana na liście zmień element o indekście 0 to jest ta sama lista na które wskazuje val [999,2]
    print("po zmianie: ", n)

val = [1,2]
change_value(val)
print(val)

"""
"""
# program do rekurencji

def recursion(number):
    if number == 20:
        return
    print(number)
    number+=1 # powtórne wywołanie funkcji aż do 20 i zapętlanie nastąpi
    recursion(number)

recursion(10)
recursion(20)
"""
"""
# przekazywanie wielu argumentów przez krotki
def my_fun(*args): # *args krotka, **args słownik - przekazywanie
    for el in args:
        print(el)
        
print(my_fun(1,2,3))


def my_fun(*args):  # *args krotka, **args słownik - przekazywanie
    for el in args:
        print(el)


print(my_fun(1, 2, 3))

"""