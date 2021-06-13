def greeting():
    print("Selamat Datang!")
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
    print()
    pilih_menu=int(input("Pilih Menu (Angka 1-3): "))
    if pilih_menu==1:
        print()
        print("---Daftar Kontak---")
        for x in kontak.keys():
            print("Nama:",x,"\tNo. Telepon:",kontak[x])
    elif pilih_menu==2:
        print()
        print("---Pastikan Nama yang Akan Ditambahkan Berbeda dengan yang Sudah Ada di Kontak---")
        nama=input("Nama: ")
        telp=input("No. Telepon: ")
        kontak[nama]=telp
        print()
        print("---Kontak Berhasil Ditambahkan---")
        print("---Silakan Pilih Menu 1 Untuk Cek Kontak Tambahan---")
    elif pilih_menu==3:
        print("---Program Selesai, Sampai Jumpa!---")
        print()
    else:
        print("---Menu Tidak Tersedia. Silakan Pilih Angka 1 sampai 3---")


    
