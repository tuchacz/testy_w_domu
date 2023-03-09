# słownik
"""
phones = {"Tomek": 345516232,"Ada": 15121564, "Karol": 9999999, "Tomek": 0000000}

# jeżeli wpiszę jeszcze raz TOmka to z aktualizuje wartość przy nim

print(phones)

# alternatywny zapis

phones = {"Tomek": 345516232,
          "Ada": 15121564,
          "Karol": 9999999,
          "Tomek": 0000000}
print(phones)

"""

"""
animals_dict = {
    "kot": "cat",
    "pies": "dog",
    "chomik": "hamster"
}

print(animals_dict["kot"])
print(animals_dict.get("kot")) # jest bezpieczniej bo jeśli nie ma to będzie None
print(animals_dict.get("krowa")) # None
print(animals_dict.get("krowa", "Brak takiego słowa"))


words = ["kot", "lew", "chomik"]
for word in words:
    if word in animals_dict:
        print(word,"->", animals_dict[word])
    else:
        print("Nie znaleziono słowa", word, "w słowniku.")
"""

# słownik nie jest sekwenvcyjny nie można bezpośrednio iterować
# ale można iterować po kluczach
# iteracja
"""
animals_dict = {
    "kot": "cat",
    "pies": "dog",
    "chomik": "hamster"
}

for key in animals_dict.keys():
    print(key,"->", animals_dict[key])


for key in animals_dict:
    print(key,"->", animals_dict[key])


for val in animals_dict.values():
    print(val)

# metoda items
for item in animals_dict.items():
    print(item)

# metoda items
for pl, en in animals_dict.items():
    print(pl, "->", en)

# inny zapis
a, b = (1,2)
print(a)
print(b)
"""
# modyfikacja słownika

animals_dict = {
    "kot": "cat",
    "pies": "dog",
    "chomik": "hamster"
}

animals_dict["świnka"] ="pig"
print(animals_dict) # dodanie nowego

# metoda update
animals_dict.update({"kurczak": "chicken"})
animals_dict.update({"świnka": "piggy"})
print(animals_dict)

#kopia słownika
dict2=animals_dict.copy()
print(dict2)

# usuwanie elementów

del dict2["świnka"]
dict2.popitem() # usuwanie ostatniego elementu słownika

dict2.clear() # usunięcie wszystkich elementów

print(dict2)
