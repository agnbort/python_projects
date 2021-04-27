# zadanie_1

firstRow = 1
lastRow = 31

currentRow = firstRow

while currentRow <= lastRow:
    print('Row number', currentRow)
    currentRow += 1


# zadanie_2

liczbaPierwsza = 1
liczbaOstatnia = 13

counter = 1

for i in range(1, 14):
    print('kwadrat z liczby', i, 'to' ,i ** 2)
    print('sześcian z liczby', i, 'to' ,i ** 3)
    counter += 1

# zadanie_3

x = 0

while x in range(0, 17):
    print('Dwa do potęgi', x, 'to', x ** 2)
    x += 1


# zadanie_4

gwiazdka = 1

while gwiazdka in range(1, 11):
    print(gwiazdka * '*')
    gwiazdka += 1