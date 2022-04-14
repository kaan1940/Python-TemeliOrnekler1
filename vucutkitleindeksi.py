#########VKI HESAPLAMA#########
boy = float(input())
kilo = int(input())
VKI = kilo / (boy * boy)
if VKI < 18.5:
    print("zayifsiniz")
elif 18.5 < VKI < 24.9:
    print("sagliklisiniz")
elif 25 < VKI < 29.9:
    print("1. derece obezite")
elif 30 < VKI < 34.9:
    print("2. derece obezitesiniz")