string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

# wzór_1

for i in range(11):
    print(string_A)

# wzór_2

for i in range(4):
    print(string_A)
    print(string_B)
    if i == 3:
        print(string_A)

# wzór_3

for i in range(10):
    print(i * 'x')
    i += 1

# wzór_4

for i in range(10):
    if i % 2 != 0:
        print('o' * i)
    else:
        print('x' * i)