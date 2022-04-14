######ic ice if kullanildi############
yas = int(input())
if yas < 40:
    surucubelgesi = input()
    universitebelgesi = input()
    if universitebelgesi == "E" and surucubelgesi == "E":
        print("ise alindiniz")
    else:
        print("ise alinmadiniz")
else:
    print("uzgunuz ise alinmadiniz")