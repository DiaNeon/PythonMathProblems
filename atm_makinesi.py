print("""
*********************************************
Atm Makinesi Hoşgeldiniz.

İşlemler:

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Programran çıkmak için "q" ya basınız
*********************************************
""")


bakiye = 1000

while True:
    işlem = input("İşlemi seçiniz: ")
    if (işlem=="q"):
        break
    elif (işlem=="1"):
        print("Bakiyeniz: ",bakiye)
    elif (işlem=="2"):
        miktar = int(input("miktar giriniz: "))
        bakiye += miktar
        print(bakiye)
    elif (işlem=="3"):
        miktar = int(input("miktar giriniz: "))
        if bakiye - miktar < 0:
            print("Böyle bir miktar çekemezsiniz!")
            continue
        bakiye -= miktar
        print(bakiye)
    else:
        print("geçersiz işlem")
