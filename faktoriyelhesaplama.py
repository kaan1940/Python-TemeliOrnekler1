########## faktoriyel hesaplama#############
faktoriyel = 1
sayi = int(input())
for i in range(1, sayi + 1, 1):
    faktoriyel = faktoriyel * i
print(str(sayi) + "!" + " = " + str(faktoriyel))
