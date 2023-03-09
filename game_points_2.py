# Napisz program zliczający punkty w grach (karcianych, planszowych itp.), realizujący:
# • definiowanie liczby oraz imion graczy,
# • definiowanie liczby punktów potrzebnych do wygranej,
# • pobieranie informacji o zdobytych punktach w każdej turze gry,
# • wyświetlanie informacji o zwycięzcy oraz zdobytych punktach poszczególnych graczy

def fetch_and_validate_int(standard_msg,error_msg="To nie jest liczba"): # validacja funkcji int
    while True:
        try:
            return int(input(standard_msg)) # nie trzeba break bo return załatwia
        except:
            print(error_msg)

def define_player(player_no):  # zdefiniuj jednego gracza
    player_points = []
    player_name = input("Podaj imię " + str(player_no) + " gracza: ")
    return {player_name: player_points}

def define_players():  # wielu  graczy
    players = {}
    players_total = fetch_and_validate_int("Podaj liczbę graczy (1,8): "))
    for i in range(players_total):  # pobieramy informację o każdym z graczy
        players.update(define_player(i + 1))
    return players

# definiowanie liczby punktów potrzebnych do wygranej
def define_win_points():
    return fetch_and_validate_int("Zdefiniuj liczbę punktów wygranej: ")


# pobieranie informacji o zdobytych punktach w każdej turze gry,

def is_winner(players, win_points):
    for player_name, player_points in players.items():
        suma = 0
        for p in player_points:
            sum +=p
        if sum >= win_points:
            return True
    return False


def count_points(players, win_points):
    counter = 1
    while True:  # będziemy się krecić dopóki nie uzyska się zwycięstwa
        print("\nTure ", counter)  # \n nowa linia
        for player_name in players.keys():
            player_points = fetch_and_validate_int("Podaj punkty dla gracza " + player_name + ": "))
            players[player_name].append(player_points)
            if is_winner(players,win_points):
                return player_name
        counter += 1

def show_results(players, winner):
    print("Wygrał gracz o imieniu", winner + ", brawo!\n")
    print("Szczególowa tabela wyników")
    for player, points in players.items():
        print(player, "->", points)


players = define_players() # definiuje wszystkich graczy
win_points = define_win_points() # konfiguracja punktów dla zwycięstwa
winner = count_points(players,win_points)
show_results(players,win_points)
#print(win_points) # zdefiniuje winnera
