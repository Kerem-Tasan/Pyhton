
def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


# Örnek kullanım
nested_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat_list = flatten(nested_list)
print(flat_list)


def reverseList(lst2):
    rvrseList = []
    for item in lst2:
        if isinstance(item, list):
            # Alt listeyi ters çevir
            tempList = item[::-1]
            rvrseList.append(tempList)
        else:
            # Tekil elemanları doğrudan ekle
            rvrseList.append(item)

    # Tam listeyi ters çevir
    return rvrseList[::-1]

# Örnek kullanım:
ornekListe = [[1, 2, 3], [4, 5, 6], 7, [8, 9]]
sonuc = reverseList(ornekListe)
print(sonuc)





