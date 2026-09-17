#tugas no 4
tujuan = input("masukkan tujuan (pantai/pegunungan/kota): ").lower()
waktu = input("masukkan waktu(pagi/malam): ").lower()
tipe = input("masukkan tipe pengunjung (anak/dewasa): ").lower()

if tujuan not in ["pantai", "pegunungan", "kota"]:
    print("Error: Tujuan tidak valid!")
    exit()

if waktu not in ["pagi", "malam"]:
    print("Error: Waktu tidak valid!")
    exit()

if tipe not in ["anak", "dewasa"]:
    print("Error: Tipe pengunjung tidak valid!")
    exit()

match tujuan:

    case "pantai":
        if waktu == "pagi":
            print("paket rekomendasi: paket A")
        elif waktu == "malam" and tipe == "dewasa":
            print("paket rekomendasi: paket B")
        else:
            print("tidak ada paket yang cocok")

    case "pegunungan":
        if waktu == "pagi" and tipe == "dewasa":
            print("paket rekomendasi: paket B") 
        elif waktu == "malam" and tipe == "dewasa":
            print("paket rekomendasi: paket C")
        else:
            print("tidak ada paket yang cocok")

    case "kota":
        if waktu == "malam":
            print("paket rekomendasi: paket C")
        else:
            print("tidak ada paket yang cocok")

    case _:
        print("tujuan wisata tidak valid")