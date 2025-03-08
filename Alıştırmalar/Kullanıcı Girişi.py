print("***********************KULLANICI GIRISINE HOSGELDINIZ...******************************")


sys_kul_adi="mertaslantur"
sys_parola="ANkara61."
giris_hakki=3

while True:

    name=input("Kullanici adiniz:")
    password=input("Sifreniz:")

    if(sys_kul_adi != name and sys_parola == password):

        print("Kullanici adi hatali...")
        giris_hakki -= 1
        print("Giris hakki",giris_hakki)

    elif(sys_kul_adi == name and sys_parola != password):

        print("Sifre hatali...")
        giris_hakki -=1
        print("Giris hakki", giris_hakki)

    elif (sys_kul_adi != name and sys_parola != password):

        print("Kullanici adi ve Sifre hatali...")
        giris_hakki -= 1
        print("Giris hakki",giris_hakki)

    else:
        print("Basariyla giris yaptiniz...")
        break


    if (giris_hakki == 0):

        print("Giris hakkiniz bitti...")

        break
