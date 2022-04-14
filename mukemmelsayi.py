#########girilen sayi mukemmel sayi midir?########
carpantoplami = 0
sayi = int(input())
for i in range(1, (int(sayi / 2)+1)):
    if sayi % i == 0:
        carpantoplami += i
        print(carpantoplami)
if sayi == carpantoplami :
    print("sayiniz mukemmel sayi")
else:
    print("sayiniz mukemmel sayi degildir")