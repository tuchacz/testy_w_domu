# Napisz wyszukiwarkę numerów telefonów:
# • zdefiniuj słownik par imię -> numer telefonu,
# • zapytaj użytkownika o imię,
# • wyświetl użytkownikowi numer telefonu lub informacje o jego braku.



phones = {"Tomek": 345516232,
          "Ada": 15121564,
          "Karol": 9999999,
          }
print(phones)

for name in phones
    name = input("Podaj imię: ")
    print(name,"->", phones[name])


# for key in phones[key]:
#     if name == i:
#         print(name,"->", phones[name])
#     else:
#         print(("Brak osoby lub numeru"))

# animals_dict.update({"kurczak": "chicken"})



# na zajęciach phone numbers


phones = {
    "Adam": 1212323,
    "Karol": 11111111,
    "Mariola": 156562532,
    "Iza": 211211
}

while True:
    name = input("Podaj imię: ")
    if name == "":
        break
    if name in phones:
        print("Telefon", phones[name])
    else:
        print("nie znaleziono telefonu dla imienia", name)

