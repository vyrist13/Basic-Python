d={
    "nama":"Thoma Saputra",
    "umur":36,
    "tinggi":172,
    #key   #value
}
print(d["nama"])
print(d)
d["nama"]="Thoma"
print(d)

for x in d:
    print(d)


d=[]

for i in range(1):
    nama=input("Masukkan nama anda: ")
    umur=int(input("Masukkan umur anda: "))
    tinggi=float(input("Masukkan tinggi anda: "))
    data={
        "nama":nama,
        "umur":umur,
        "tinggi":tinggi
    }
    d.append(data)
for i in d:
    print("Nama Pelanggan: ",i["nama"])
    print("Umur Pelanggan: ",i["umur"])
    print("Tinggi Pelanggan: ",i["tinggi"])

    

