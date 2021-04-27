# Krok 1
beatles = []
print("Krok 1:", beatles)

# Krok 2
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Krok 2:", beatles)

# Krok 3
# dodać: Stu Sutcliffe, Pete Best
for i in range(2):
    beatles.append(input("Dodaj osobę: "))

print("Krok 3:", beatles)

# Krok 4

del beatles[3]
del beatles[3]

print("Krok 4:", beatles)

# Krok 5

beatles.insert(0, 'Ringo Starr')

print("Krok 5:", beatles)
