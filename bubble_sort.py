# # sortowanie bąbelkowe program
#
# numbers = [4, 5, 2, 1] # nie posortowane
# numbers = [4, 2, 1, 5] # pierwsza iteracja
# numbers = [2, 1, 4, 5] # 2 iteracja
# numbers = [1, 2, 4, 5]# trzecia iteracja

numbers = [4, 5, 2, 1]
swapped = True  # czy była zamiana

while swapped:  # pętla się wykonuje dopóki będzie True
    swapped = False  # jeżeli będzie false to zakończy pętlę
    for i in range(len(numbers) - 1):  # przejść tyle ile jest elementów w liście minus 1
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True  # zamieniliśmy i dlatego jesszcze raz potrzebuyjemy wywołać pętlę while

print(numbers)

# większa lista
numbers = [4, 5, 2, 1, 5, 8, 10, 123, 50, -3, 4.6]
swapped = True  # czy była zamiana

while swapped:  # pętla się wykonuje dopóki będzie True
    swapped = False  # jeżeli będzie false to zakończy pętlę
    for i in range(len(numbers) - 1):  # przejść tyle ile jest elementów w liście minus 1
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True  # zamieniliśmy i dlatego jesszcze raz potrzebuyjemy wywołać pętlę while

print(numbers)

# alternatywnie za pomocą sort
numbers.sort()
print(numbers)

#reverse sort
numbers.sort(reverse=True)
print(numbers)
