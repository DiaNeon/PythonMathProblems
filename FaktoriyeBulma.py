print("""
************************************

Faktoriyel Bulma Programı

Çıkmak için q'ya basın.

************************************
""")


faktöriyel = int(input("Faktöriyel sayısını giriniz: "))

for i in range(2,faktöriyel+1):
    print("i: ",i)
    i *= i
    print("faktoriyel: ",i)