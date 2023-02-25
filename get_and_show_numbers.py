#
def get_number(number_no):
    print("Proszę podaj ", number_no, "liczbę: ", end=" ")
    return int(input())


a = get_number(1)
b = get_number(2)
c = get_number(3)

print("Pobrano liczby:", a, b, c)


# zaleta w jednym punkcie zmieniam i od razu się zmienia w całości

# alterantywny zapis
def get_number(number_no):
    return int(input("Proszę podaj " + str(number_no) + " liczbę: ", end=" "))


a = get_number(1)
b = get_number(2)
c = get_number(3)

print("Pobrano liczby:", a, b, c)


# zaleta w jednym punkcie zmieniam i od razu się zmienia w całości


# alterantywny zapis
def get_number(number_no):
    return int(input("Proszę podaj " + str(number_no) + " liczbę: ", end=" "))


print("Pobrano liczby:", get_number(1), get_number(2), get_number(3))

# zaleta w jednym punkcie zmieniam i od razu się zmienia w całości
