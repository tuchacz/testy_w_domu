# plansza do gry w szachy i warcabry: ilość pól 8x8

#     A B C D E F G H
#   1 # # # # # # # #
#   2 # # # # # # # #
#   3 # # # # # # # #
#   4 # # # # # # # #
#   5 # # # # # # # #
#   6 # # # # # # # #
#   7 # # # # # # # #
#   8 # # # # # # # #

# program do gry w szachy
# obrazowanie pola za pomocą dwóch kresek pierwsza kolor druga rodzaj

#chess_row = ["--", "--", "--", "--", "--", "--", "--", "--"] # szachowy wiersz

# chess_row = ["--" for i in range(8) ] # szachowy wiersz dla i podstaw mi "--"
# chessboard = [chess_row[:] for i in range(8)] # bo jest 8 wierszy, weź cały chess row i zrób kopie i podstawiaj aby nie było problemu nadpisania

#alternatywnie
WHITE_pown="WP"
BLACK_pown = "BP"

chessboard = [["--" for i in range(8)] for i in range(8)] # zapomocą jedengo wyrazenia

chessboard[0][0] = WHITE_pown
chessboard[3][5] = BLACK_pown # ustaw na miejscu jakiegos pionka 4 wiersz i 5 kolumna

for chess_row in chessboard:
    for chess_square in chess_row:
        print(chess_square, end=" ") # pokaż moje pole  i daj odstępy
    print() # jak skończysz to daj eneter



