sudut = float(input("Besar sudut dalam derajat: "))

if sudut <= 0 or sudut >= 180:
    print("Masukan sudut tidak valid. Sudut harus di antara 0 dan 180 derajat.")
elif sudut < 90:
    print("Sudut lancip")
elif sudut == 90:
    print("Sudut siku-siku")
else:
    print("Sudut tumpul")