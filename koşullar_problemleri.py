"""
boy = float(input("Boy: "))
kilo = int(input("Kilo: "))

bki = kilo/(boy*boy)

if bki < 18.5:
    print("Zayıf")
elif bki >= 18.5 and bki <= 25:
    print("Normal")
elif bki >= 25 and bki <= 30:
    print("Fazla kilolu")
elif bki > 30:
    print("Obez")
"""
"""
bir = int(input("sayı1: "))
iki = int(input("sayı2: "))
uc = int(input("sayı3: "))

if bir > iki and bir > uc:
    print("Bir büyüktür")
elif iki > uc and iki > bir:
    print("iki buyuktur")
elif uc > iki and uc > bir:
    print("3 Büyüktür")
"""
"""
vize1 = int(input("vize1: "))
vize2 = int(input("vize2: "))
final = int(input("Final: "))

hf = sonuc = int(vize1)*(3/10) + int(vize2)*(3/10) + int(final)*(4/10)
print(hf)
if hf >=90:
    print("AA")
if hf >=85 and hf < 90:
    print("BA")
if hf >=80 and hf < 85:
    print("BB")
if hf >=75 and hf < 80:
    print("CB")
if hf >=70 and hf < 75:
    print("CC")
if hf >=65 and hf < 70:
    print("DC")
if hf >=60 and hf < 65:
    print("DD")
if hf >=55 and hf < 60:
    print("FD")
if hf < 55:
    print("FF")
"""

soru = input("Üçgen mi Dörtgenmi mi tipini bulmak istiyosun: ")

if soru == "Dörtgen":
    kenar1 = int(input("1.Kenar: "))
    kenar2 = int(input("2.Kenar: "))
    kenar3 = int(input("3.Kenar: "))
    kenar4 = int(input("4.Kenar: "))

    if kenar1 == kenar2 and kenar1 == kenar3 and kenar1 == kenar4:
        print("Kare")


    kenarlar1 = kenar1 + kenar2
    kenarlar2 = kenar1 + kenar3
    kenarlar3 = kenar1 + kenar4
    kenarlar4 = kenar2 + kenar1
    kenarlar5 = kenar2 + kenar3
    kenarlar6 = kenar2 + kenar4
    kenarlar7 = kenar3 + kenar2
    kenarlar8 = kenar3 + kenar1
    kenarlar9 = kenar3 + kenar4
    kenarlar10 = kenar4 + kenar2
    kenarlar11 = kenar4 + kenar3
    kenarlar12 = kenar4 + kenar1

    if kenarlar1 != kenarlar2 or kenarlar1 != kenarlar3 or kenarlar1 != kenarlar4 or kenarlar1 != kenarlar5 or kenarlar1 != kenarlar6 or kenarlar1 != kenarlar7 or kenarlar1 != kenarlar8 or kenarlar1 != kenarlar9 or kenarlar1 != kenarlar10 or kenarlar1 != kenarlar11 or kenarlar1 != kenarlar12 :
        print("Dikdörtgen")
    elif kenarlar2 != kenarlar3 or kenarlar2 != kenarlar4 or kenarlar2 != kenarlar5 or kenarlar2 != kenarlar6 or kenarlar2 != kenarlar7 or kenarlar2 != kenarlar8 or kenarlar2 != kenarlar9 or kenarlar2 != kenarlar10 or kenarlar2 != kenarlar11 or kenarlar2 != kenarlar12 :
        print("Dikdörtgen")
    elif kenarlar3 != kenarlar2 or kenarlar3 != kenarlar4 or kenarlar3 != kenarlar5 or kenarlar3 != kenarlar6 or kenarlar3 != kenarlar7 or kenarlar3 != kenarlar8 or kenarlar3 != kenarlar9 or kenarlar3 != kenarlar10 or kenarlar3 != kenarlar11 or kenarlar3 != kenarlar12 :
        print("Dikdörtgen")
    elif kenarlar4 != kenarlar2 or kenarlar4 != kenarlar3 or kenarlar4 != kenarlar5 or kenarlar4 != kenarlar6 or kenarlar4 != kenarlar7 or kenarlar4 != kenarlar8 or kenarlar4 != kenarlar9 or kenarlar4 != kenarlar10 or kenarlar4 != kenarlar11 or kenarlar4 != kenarlar12 :
        print("Dikdörtgen")
    elif kenarlar5 != kenarlar2 or kenarlar5 != kenarlar3 or kenarlar5 != kenarlar4 or kenarlar4 != kenarlar6 or kenarlar5 != kenarlar7 or kenarlar5 != kenarlar8 or kenarlar5 != kenarlar9 or kenarlar5 != kenarlar10 or kenarlar5 != kenarlar11 or kenarlar5 != kenarlar12 :
        print("Dikdörtgen")
    elif kenarlar6 != kenarlar2 or kenarlar6 != kenarlar3 or kenarlar6 != kenarlar4 or kenarlar6 != kenarlar5 or kenarlar6 != kenarlar7 or kenarlar6 != kenarlar8 or kenarlar6 != kenarlar9 or kenarlar6 != kenarlar10 or kenarlar6 != kenarlar11 or kenarlar6 != kenarlar12 :
        print("Dikdörtgen")
    elif kenarlar7 != kenarlar2 or kenarlar7 != kenarlar3 or kenarlar7 != kenarlar4 or kenarlar7 != kenarlar5 or kenarlar7 != kenarlar6 or kenarlar7 != kenarlar8 or kenarlar7 != kenarlar9 or kenarlar7 != kenarlar10 or kenarlar7 != kenarlar11 or kenarlar7 != kenarlar12 :
        print("Dikdörtgen")
    elif kenarlar8 != kenarlar2 or kenarlar8 != kenarlar3 or kenarlar8 != kenarlar4 or kenarlar8 != kenarlar5 or kenarlar8 != kenarlar6 or kenarlar8 != kenarlar7 or kenarlar8 != kenarlar9 or kenarlar8 != kenarlar10 or kenarlar8 != kenarlar11 or kenarlar8 != kenarlar12 :
        print("Dikdörtgen")
    elif kenarlar9 != kenarlar2 or kenarlar9 != kenarlar3 or kenarlar9 != kenarlar4 or kenarlar9 != kenarlar5 or kenarlar9 != kenarlar6 or kenarlar9 != kenarlar7 or kenarlar9 != kenarlar8 or kenarlar9 != kenarlar10 or kenarlar9 != kenarlar11 or kenarlar9 != kenarlar12 :
        print("Dikdörtgen")
    elif kenarlar10 != kenarlar2 or kenarlar10 != kenarlar3 or kenarlar10 != kenarlar4 or kenarlar10 != kenarlar5 or kenarlar10 != kenarlar6 or kenarlar10 != kenarlar7 or kenarlar10 != kenarlar8 or kenarlar10 != kenarlar9 or kenarlar10 != kenarlar11 or kenarlar10 != kenarlar12 :
        print("Dikdörtgen")
    elif kenarlar11 != kenarlar2 or kenarlar11 != kenarlar3 or kenarlar11 != kenarlar4 or kenarlar11 != kenarlar5 or kenarlar11 != kenarlar6 or kenarlar11 != kenarlar7 or kenarlar11 != kenarlar8 or kenarlar11 != kenarlar9 or kenarlar11 != kenarlar10 or kenarlar11 != kenarlar12 :
        print("Dikdörtgen")
    elif kenarlar12 != kenarlar2 or kenarlar12 != kenarlar3 or kenarlar12 != kenarlar4 or kenarlar12 != kenarlar5 or kenarlar12 != kenarlar6 or kenarlar12 != kenarlar7 or kenarlar12 != kenarlar8 or kenarlar12 != kenarlar9 or kenarlar12 != kenarlar10 or kenarlar12 != kenarlar11:
        print("Dikdörtgen")
    else:
        print("DÖRTGEN")

elif soru == "Üçgen":
    kenar5 = int(input("1.Kenar: "))
    kenar6 = int(input("2.Kenar: "))
    kenar7 = int(input("3.Kenar: "))

    if kenar5 == kenar6 or  kenar5 == kenar7 or  kenar6 == kenar5 or  kenar6 == kenar7 or  kenar7 == kenar6 or  kenar7 == kenar5:
        print("İkizkenar Üçgen")
    elif kenar5 == kenar6 == kenar7:
        print("Eşkenar üçgen")
    elif kenar5 != kenar6 != kenar7:
        print("Sıradan üçgen")

    else:
        print("Üçgen Belirtmiyor")



