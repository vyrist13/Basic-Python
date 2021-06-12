#Program untuk menghitung luas lingkaran

r=int(input("Masukkan jari-jari lingkaran:"))
pi=22/7
luas_lingkaran=pi*(r**2)
print(type(r))
print(type(pi))
print(type(luas_lingkaran))
print("Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2".format(r,luas_lingkaran))
