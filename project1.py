x = 7
hitungan = 1
print("=== TEBAK ANGKA ===")
print("Percobaan ke-1")
while True:
 if hitungan > 1:
    print(f"Percobaan ke-{hitungan}")

 y = int(input("Masukkan angka 1-10 : "))

 if y > x:
    print("Angka terlalu besar!\n")
 elif y < x:
    print("Angka terlalu kecil!\n")
 elif y == x:
    print("BENARR!!")
    break
 hitungan = hitungan + 1
