#Program untuk kelulusan

teori=int(input("Silakan masukkan nilai ujian teori anda: "))
praktek=int(input("Silakan masukkan nilai ujian praktek anda: "))

if teori >=70 and praktek >= 70:
    print("Selamat, anda lulus!")
elif teori >=70 and praktek <70:
    print("Anda harus mengulang ujian praktek")
elif teori <70 and praktek >=70:
    print("Anda harus mengulang ujian teori")
else:
    print("Anda harus mengulang ujian teori dan praktek")