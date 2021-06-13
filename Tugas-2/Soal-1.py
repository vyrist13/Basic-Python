def greeting():
    print("Selamat datang!")
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

kontak={
    "Farhan":"08123456789",
    "Joko":"08987654321",
}
pilih_menu=0
greeting()
while pilih_menu !=3:
    pilih_menu=int(input("Pilih menu:"))
    if pilih_menu==1:
        print("---Daftar Kontak---")
        for x in kontak.keys():
            print("Nama:",x)
            print("No. Telepon:",kontak[x])
        print()
    elif pilih_menu==2:
        nama=input("Nama:")
        telp=input("No. Telepon:")
        kontak[nama]=telp
        print("---Kontak Berhasil Ditambahkan---")
    elif pilih_menu==3:
        print("---Program Selesai, Sampai Jumpa!---")
    else:
        print("---Menu Tidak Tersedia---")


    
