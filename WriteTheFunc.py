def isLeap(year):
    leap = False
    if (year % 4 == 0):
        if (year % 100 != 0 or year % 400 == 0):
            leap = True
    return leap

year = int(input("Enter a year: "))
print(isLeap(year))


num1=90_100_000_000
print(num1)

x=2

print(f"x in değeri:{x}")
