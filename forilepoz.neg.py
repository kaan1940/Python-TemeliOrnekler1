#########for ile pozitif negatif sayi tespiti#######
pozitifsayiadedi = 0
negatifsayiadedi = 0
sifirsayiadedi = 0
for i in range(5):
    sayi = int(input())
    if sayi > 0:
        print("sayiniz pozitif")
        pozitifsayiadedi += 1
    elif sayi < 0:
        print("sayiniz negatif")
        negatifsayiadedi += 1
    else:
        print("sayiniz sifira esittir")
        sifirsayiadedi += 1
print("pozitifsayiadedi: " + str(pozitifsayiadedi))
print("negatifsayiadedi: " + str(negatifsayiadedi))       
print("sifirsayi adedi: " + str(sifirsayiadedi))