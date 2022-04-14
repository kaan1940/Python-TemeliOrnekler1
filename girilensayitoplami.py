######girilen sayi çif ise topla##############
toplam = 0
for i in range(7):
    sayi = int(input())
    if sayi %2 == 0:
        toplam += sayi
print("cift sayilarin toplami: " + str(toplam))