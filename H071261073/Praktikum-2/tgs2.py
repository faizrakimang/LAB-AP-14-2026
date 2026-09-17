# tugas no 2
jarak = float(input("masukkan jarak pengiriman (km): "))
express = input("layanan express (ya/tidak) ").lower()

if jarak < 5:
    tarif = 10000
elif jarak <= 20:
    tarif = 20000
else:
    tarif = 35000


biaya_express = 15000 if express == "ya" else 0
total = tarif + biaya_express
print("total tarif pengiriman: Rp", total)

