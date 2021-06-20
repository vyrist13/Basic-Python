class animal:
    def __init__(self, kaki, gigi, makanan):
        self.kaki=kaki
        self.gigi=gigi
        self.makanan=makanan

tiger=animal(4,"Punya Taring","Daging")
kancil=animal(4,"Tidak Punya Taring","Tumbuhan")
print(tiger.kaki)
print(tiger.gigi)
print(kancil.kaki)
print(kancil.makanan)