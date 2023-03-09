var_1 = 1
var_2 = 2
print(var_1, var_2)

var_1, var_2 = var_2, var_1

print(var_1, var_2)

numbers = [4, 3, 5, 1, 7]

print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)