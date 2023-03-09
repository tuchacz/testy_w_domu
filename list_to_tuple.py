# Napisz funkcje zamieniającą 3 listy na 1 krotkę bez powtarzających się elementów.
# Przykład: [1, 2], [1, 1], [4, 4, 4] -> (1, 2, 4)
#

def merge_list_without_duplicates(source,target):
    for e in source: #mam dodać elementy do elementów
        if e not in target: # sprawdzamy czy element nie jest w liście docelowej
            target.append(e)


def transform_data(list1,list2,list3):
    result =[] # tworzę pustę listę
    merge_list_without_duplicates(list1, result)
    merge_list_without_duplicates(list2, result)
    merge_list_without_duplicates(list3, result)
    return tuple(result)


print(transform_data([1,2],[1,1],[4,4,4]))
print(transform_data([1,2,3],[1,2,3],[4,5,6]))
print(transform_data(["Ala", "ma"],["Ala", "ma","kota"],["mysz"]))


