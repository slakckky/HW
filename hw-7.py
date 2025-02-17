
metin = input("Bir metin girin: ")
metin_buyuk = metin.upper()


metin_bosluksuz = metin_buyuk.strip()
metin_ayrik = metin_bosluksuz.replace("A", "E")

kelime_listesi = metin_ayrik.split()

print("İşlenmiş Metin:", metin_ayrik)
print("Kelime Listesi:", kelime_listesi)


ilkhal_metin = "Python programlama dili"


ters_metin = ilkhal_metin[::-1]
print("Ters Metin:", ters_metin)

degisen_metin = ilkhal_metin.replace("programlama", "kodlama")
print("Yeni Metin:", degisen_metin)
