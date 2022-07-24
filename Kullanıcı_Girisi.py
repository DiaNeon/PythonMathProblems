print("""
*********************************************
Kullanıcı Girişi Programı
*********************************************
""")

sys_kullanıcı_adı = "murat"
sys_parola = "123asd"

giris_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı Adı Giriniz: ")
    passwd = int(input("Parola Giriniz: "))

    if sys_parola == passwd and sys_kullanıcı_adı == kullanıcı_adı:
        print("Giriş Başarılı")

    elif sys_parola != passwd or sys_kullanıcı_adı != kullanıcı_adı:
        print("Bilgiler Yanlış")
        giris_hakkı -= 1
    if giris_hakkı == 0:
        break
