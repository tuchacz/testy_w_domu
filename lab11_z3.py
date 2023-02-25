# Napisz skrypt symulujący rozgrywkę gry w szachy, w tym celu:
# • stwórz wirtualną szachownicę,
# • na wirtualnej szachownicy rozmieść losowo 2. dowolne figury szachowe i 3. piony,
# • zaprezentuj użytkownikowi stan wirtualnej szachownicy

import random

BLANK_SQUARE = "--"
pieces = ["WP", "BP", "BP", "BT", "WQ"]  # elementy szachowe 3 piony i dwie figury
# wirtualna szachownica
chessboard = [[BLANK_SQUARE for i in range(8)] for i in range(8)]  # zapomocą jedengo wyrazenia

# losowanie elementów na szachownicy
counter = 0

while counter < 5:  # mamy 5 elementów
    row = random.randint(0, 7)
    column = random.randint(0, 7)
    if chessboard[row][column] == BLANK_SQUARE:
        chessboard[row][column] = pieces[counter]
        counter += 1

# wyświetl szachownicę
for row in range(len(chessboard)):
    if row == 0:
        print(" ", "A", "B", "C", "D", "E", "F", "G", "H", sep="  ")
    print(row + 1, end=" ")
    for column in range(len(chessboard[row])):
        print(chessboard[row][column], end=" ")  # pokaż moje pole  i daj odstępy
    print()  # jak skończysz to daj eneter
