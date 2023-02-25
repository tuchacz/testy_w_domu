# Napisz program obliczającej wskaźnik BMI (Body Mass Index), w tym celu:
# • zapytaj użytkownika o wzrost i wagę,
# • stwórz funkcję obliczającą wskaźnik BMI na podstawie podanych przez użytkownika danych,
# • stwórz funkcję wyznaczającą odpowiednią kategorię (niedowaga, waga prawidłowa, nadwaga,
# otyłość) na podstawie wskaźnika BMI,
# • zaprezentuj wyniki korzystając z wcześniej przygotowanych funkcji.

def calculate_bmi(weight_in_kg, hight_in_m):
    return weight_in_kg / hight_in_m ** 2


# sprawdzenie kategorii
def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "niedowaga"
    elif bmi < 25:
        return "waga prawidłowa"
    elif bmi < 30:
        return "nadwaga"
    else:
        return "otyłość"


print("Obliczanie wskaźnika BMI!")
weight_in_kg = float(input("Podaj wagę w kilogramach: "))
hight_in_cm = float(input("Podaj swój wzrost w cm: "))

bmi = calculate_bmi(weight_in_kg, hight_in_cm * 0.01)
category = determine_bmi_category(bmi)

print("Wskaźnik BMI wynosi: ", bmi)
print("Kategoria: ", category)


# BMI = weight / (height ** 2)
