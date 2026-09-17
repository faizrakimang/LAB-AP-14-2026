#tugas no 1
cabai = int(input("masukkan persentase cabai: "))

if cabai < 0:
    print("input tidak valid")
elif cabai <= 10:
    print("level aman")
elif cabai <= 40:
    print("level sedang")
elif cabai <= 70:
    print("level pedas")
else:
    print("level ekstrem")
