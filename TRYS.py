
numbers = [1, 2, 3, 4]
doubled_numbers = map(lambda x: x * 2, numbers)
print(list(doubled_numbers))  # [2, 4, 6, 8]
from itertools import islice

# Her elemanı iki ile çarpan bir fonksiyon tanımlayalım
def multiply_by_two(x):
    return x * 2

# Bir liste oluşturalım
numbers = [1, 2, 3, 4, 5]

# 'map' fonksiyonunu kullanarak her elemanı iki ile çarpalım
mapped_result = map(multiply_by_two, numbers)

# 'islice' fonksiyonu ile ilk 3 elemanı alalım
limited_result = islice(mapped_result, 3)

# Sonucu bir listeye dönüştürelim ve yazdıralım
print(list(limited_result))  # Çıktı: [2, 4, 6]

"""
def split_and_join(line):
    # Boşluklara göre böl
    words = line.split()
    # Listeyi '-' ile birleştir
    return "-".join(words)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


"""
