# Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną
# ilość razy, w poziomie lub w pionie.

"""
def show_char(char, poziom, pion):  # parametr how many czyli ile jest gwiazdek
    print((char * poziom) * pion)

show_char(char="#", poziom=10, pion=10)

"""


# na zajęciach

def print_char(character="*", rep=10, vert=False):  # czyli japierw robimy domyślnie horyzontalnie
    for i in range(rep):
        if vert:# sprawdzenie parametru
            print(character)
        else:
            print(character + " ", end="") # wypisuje hotyzontalnie
    if not vert:
        print()
    print()


print_char()
print_char("+", 5, True)
print_char("^", 7, False)
