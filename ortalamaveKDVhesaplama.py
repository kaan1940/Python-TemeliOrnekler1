######ortalama ve KDV hesaplama#########
sayi1 = int(input())
sayi2 = int(input())
sayi3 = int(input())
oran = int(input())
ortalama = (sayi1 + sayi2 + sayi3) / 3
KDV = ortalama * oran / 100
tutar = ortalama + KDV 
print(ortalama)
print(KDV)
print(tutar)