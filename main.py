"""
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b ** 2-4 *a *c

x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)

print("Birinci Kök: {} İkinci Kök: {}".format(x1,x2))
"""
#Problem1
"""
bir = int(input("1.sayı: "))
iki = int(input("2.sayı: "))
üç = int(input("3.sayı: "))

print("sayı bir : {} sayı iki : {} sayı üç: {} çarpım işlemi sonucu: {}".format(bir,iki,üç,bir*iki*üç))
"""
#Problem2
"""
boy = float(input("boy: "))
kilo = float(input("kilo: "))
Kitleİndeksi = kilo/boy

print("boy: {} kilo: {} Beden kitle İndeksi: {}".format(boy,kilo,Kitleİndeksi))
"""
#Problem3
"""
benzin = int(input("Aracın kilometrede yaktığı: "))
yol = int(input("Araç kaç km yol gitti: "))

tl = benzin/yol

print("benzin: {} yol: {} yakılan tutar: {}".format(benzin,yol,tl))
"""
#problem4
"""
ad = input("Kullanıcı Adı: ")
soyad = input("Soyad: ")
numara = input("Numara: ")

print("ad: {}\nsoyad: {}\nnumara: {}".format(ad,soyad,numara))
"""
#problem5
"""
sayı1 = int(input("sayı girin: "))
sayı2 = int(input("sayı girin: "))
print(sayı2,sayı1)
sayı2,sayı1 = sayı1,sayı2
print(sayı2,sayı1)
"""
#Problem6
a = int(input("a notası: "))
b = int(input("b notası: "))

hipotenüs = a **2 + b**2

print("A NOKTASI: {} B NOKTASI: {} HİPOTENÜS: {}".format(a,b,hipotenüs))