sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))


toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
bolum = sayi1 / sayi2
tam_bolme = sayi1 // sayi2
mod = sayi1 % sayi2
us_alma = sayi1 ** sayi2

print("Toplam:", toplam)
print("Fark:", fark)
print("Çarpım:", carpim)
print("Bölüm:", bolum)
print("Tam Bölme:", tam_bolme)
print("Mod:", mod)
print("Üs Alma:", us_alma)


r = float(input("\n Dairenin yarıçapını girin: "))

pi = 3.14
alan = pi * (r ** 2)

print("Dairenin alanı:", alan)