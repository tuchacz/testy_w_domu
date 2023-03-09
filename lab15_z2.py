# Napisz program pobierający od użytkownika 3 liczby zmiennoprzecinkowe.
# Uwzględnij możliwość pomyłki użytkownika

numbers =[]
counter = 0
while True:
    if counter==3:
        break
    try:
        n = float(input("Podaj liczbę zmiennoprzecinkową: "))
        numbers.append(n)
        counter += 1
    except ValueError:
        print("To nie jest liczba zmiennoprzecinkowa, spróbuj ponownie:")
print(numbers)
