def count_down(wishes = True):
    print("Trzy...")
    print("Dwa...")
    print("Jeden...")

    if not wishes:
        return

    print("Szczęśliwego nowego roku!")

count_down()
count_down(True) # test z True
count_down(wishes=True)
print()
count_down(wishes=False)
print(type(count_down(wishes=False)))
print()
count_down(False) #
