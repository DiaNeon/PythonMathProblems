sys_kullanıcı_adı = "Mustafa Gedik"
sys_passwd = 203182

kullanıcıadı = input("kullanıcı adını giriniz: ")
parola = int(input("Parola giriniz: "))

if sys_kullanıcı_adı == kullanıcıadı and parola == sys_passwd:
    print("Giriş Başarılı")
elif sys_kullanıcı_adı != kullanıcıadı and sys_passwd == parola:
    print("Kullanıcı adı hatalı")
elif sys_passwd != parola and sys_kullanıcı_adı == kullanıcıadı:
    print("Parola Hatalı")
elif sys_passwd != parola and sys_kullanıcı_adı != kullanıcıadı:
    print("Kullancı adı parola hatalı!")
elif sys_passwd == parola and sys_kullanıcı_adı == kullanıcıadı:
    print("Giriş Başarılı")
else:
    print("Hatalı Giriş")