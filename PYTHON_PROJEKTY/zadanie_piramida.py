

blokow = int(input("Wprowadź liczbę bloków: "))

wysokosc = 0
bloki_w_pietrze = 1

while bloki_w_pietrze <= blokow:
    wysokosc = wysokosc + 1
    blokow = blokow - bloki_w_pietrze
    if blokow == 0:
        break
    bloki_w_pietrze = bloki_w_pietrze + 1


print("Wysokość piramidy wynosi:", wysokosc)

