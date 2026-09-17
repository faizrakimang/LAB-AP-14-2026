minuman = int(input("Pilih minuman (1/2/3): "))
match minuman:
	case 1:
		pesanan = "Kopi"
	case 2:
		pesanan = "Teh"
	case 3:
		pesanan = "Jus"
	case _:
		pesanan = "Menu tidak tersedia"

ukuran = input("Ukuran (besar/kecil): ").lower()

if ukuran == "besar":
	tambahan = 5000
else:
	tambahan = 0

print(f"Pesanan: {pesanan}")
print(f"Total tambahan: Rp{tambahan}")

