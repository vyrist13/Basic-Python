class person:
    def __init__(self,nama,umur,tinggi,hobby):
        self.nama=nama
        self.umur=umur
        self.tinggi=tinggi
        self.hobby=hobby
    def greet(self):
        print("Nama saya adalah",self.nama, "saat ini saya berumur".self.umur,"saat ini saya memiliki tinggi", self.tinggi,"hobby saya",self.hobby)

user=person("Thoma", 35, 172,"Membaca buku")
user.greet()