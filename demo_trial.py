def my_name():
    return "Marcin" # zwraca wartość ale nie drukuje

def show_my_name():
    print("Marcin") # zwraca wartość i drukuje
    return None

result = show_my_name()
print(result)