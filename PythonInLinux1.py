import sys

print("=== CREATE YOUR CHARACTER ===")
x = input("Nama : ")
y = int(input("Umur : "))
z = input("Class : ")

print("""======================== \n    CHARACTER INFO \n========================""")
a = x
b = y
c = z
print(f"Nama : {a}")
print(f"Umur : {b}")
print(f"Class : {c}")
print()
print(f"Selamat datang, {a}! \nPetualangan dimulai . . .")
print()
lvl = input("Apakah kamu ingin mendapatkan hadiah?(yes/no) : ")
print()
if "yes" in lvl:
    print("Anda mendapatkan hadiah! \n Level : 3 \n Gold : 150")
if "no" in lvl:
    print("GAME OVER!!!")
    sys.exit()
print()
print("Tahun pertama dimulai . . .")
print()
skip = input("Ketik Skip untuk time skip selama 5 tahun : ")
print()

if "skip" in skip:
    print("=== 5 TAHUN KEMUDIAN ===")
print()
if "skip" not in skip:
    print("GAME OVER!!!")
    sys.exit()
print("""======================== \n    CHARACTER INFO \n========================""")
u1 = b + 5
print(f"Nama : {a}")
print(f"Umur : {u1}")
print(f"Class : {c}")
print("Level : 8")
print("Gold : 1000")

print("=== STORY ===")
print()
story = input("Saat anda berjalan di tengah hutan, anda bertemu dengan sosok manusia gendut yang cinta dengan sawit, apakah anda ingin melawannya? (yes/no) : ")

if "yes" in story:
    print("ANDA BERHASIL MENGALAHKAN PRIA SAWITTT!!")
if "yes" not in story:
    print("GAME OVER!!")
    sys.exit()
