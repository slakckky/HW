
yas = int(input("Yaşınızı girin: "))

kontrol1 = yas > 18 and yas < 65
kontrol2 = yas < 18 or yas > 65
kontrol3 = not (yas == 25)

print("18'den büyük ve 65'ten küçük mü?:", kontrol1)
print("18'den küçük veya 65'ten büyük mü?:", kontrol2)
print("Yaş 25 değil mi?:", kontrol3)

sayi = int(input("\nBir sayı girin: "))

cift_mi = sayi % 2 == 0
pozitif_mi = sayi > 0

print("Sayı çift mi?:", cift_mi)
print("Sayı pozitif mi?:", pozitif_mi)

yas = int(input("\nYaşınızı girin: "))
ehliyet = int(input("Ehliyetiniz var mı? (Evet=1/Hayır=0): "))


if yas > 18 and ehliyet == 1:
    print("Araba kullanabilirsiniz.")
else:
    print("Araba kullanamazsınız.")
