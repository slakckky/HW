
meyveler = ["elma", "armut", "çilek", "kiraz"]
meyve = input("Bir meyve ismi girin: ")

if meyve in meyveler:
    print(meyve, "listede var.")
else:
    print(meyve, "listede yok.")

parola = "PyThOn123"


karakter = input("Bir karakter girin: ")

if karakter not in parola:
    print("Parolada bu karakter yok.")
else:
    print("Parolada bu karakter var.")
