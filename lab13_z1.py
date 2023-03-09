# Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.


"""
def potega(number,power):
    results = []
    for element in number:
        result=element**power
        results.append(result)
    return results

print(potega([2,4,5],2))

"""


# na zajęciach

def pow(numbers, exponent):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** exponent
    return numbers


print(pow([1, 2, 3], 2))

print()

# alternatywa
def pow2(numbers, exponent):
    result = []
    for n in numbers:
        result.append(n ** exponent)
    return result

print(pow2([1, 2, 3], 2))

print()
# alternatywa za pomocą wyrażenia listowego

def pow3(numbers,exponent):
    return [x**exponent for x in numbers]

print(pow3([1, 2, 3], 2))

