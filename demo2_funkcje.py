# funkcje
"""
name = input("Jak masz na imię: ")
print(("Witaj " + name + "!") * 100)

"""
"""
# przekazywanie parametrów pozycyjnych
def introduce(first_name, last_name):
    print("Cześć jestem", first_name, last_name)

introduce("Jan", "Kowalski")

introduce("Kowalski", "Jan") # w takiej kolejności w jakiej wprowadziliśmy w takiej dostaniemy
introduce(first_name="Jan", last_name="Kowalski")
# miksowanie parametrów, najpierw pozycyjne
# introduce(last_name="Kowalski", "Jan") # nie uruchomi się

print("raz", "dwa", "trzy", sep=" - ")
"""

"""
def introduce(first_name="Jan", last_name="Kowalski"):
    print("Cześć jestem", first_name, last_name)

introduce("Marcin","Nowak")
introduce(last_name="Nowak")

#def introduce(first_name="Jan", last_name): # nie zadziała bo domyślny następuje po okrteślonnym

"""
"""
# return
def introduce(first_name="Jan", last_name="Kowalski"):
    print("Cześć jestem", first_name, last_name)
    return None

print(introduce())

def introduce(first_name="Jan", last_name="Kowalski"):
    print("Cześć jestem", first_name, last_name)
    return 12

print(introduce())

"""

def my_fun():
    #to do
    pass

my_fun()
print(my_fun())

if my_fun() == None:
    print("Funkcja narazie nic nie zwraca")


