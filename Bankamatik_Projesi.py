import sys

hesap_Bilgileri = [
    {
        "ad":"Hasan Yılmaz",
        "hesapNo":12345,
        "bakiye":2500,
        "ekHesap":1500,
        "username":"hasanyilmaz",
        "password":"1234"
    },
    {
        "ad":"Eren Balkış",
        "hesapNo":98765,
        "bakiye":1600,
        "ekHesap":400,
        "username":"erenbalkis",
        "password":"9876"
    },
    {
        "ad":"Hüseyin Çakmak",
        "hesapNo":23456,
        "bakiye":2000,
        "ekHesap":500,
        "username":"huseyincakmak",
        "password":"5678"
    },
    {
        "ad":"Salih Korkmaz",
        "hesapNo":67891,
        "bakiye":5000,
        "ekHesap":2500,
        "username":"salihkorkmaz",
        "password":"9123"
    }
]

def menu (hesap):
    print()
    print(f"Merhaba {hesap["ad"]}")
    print("Bakiye Sorgulama için 1'i,")
    print("Para çekme için 2'yi,")
    print("Para yatırma için 3'ü,")
    islem = input("Çıkış yapmak için 0'ı tuşlayınız: ")

    if islem == "1":
        bakiyeSorgula(hesap)
    elif islem == "2":
        paraCekme(hesap)
    elif islem == "3":
        paraYatirma(hesap)
    elif islem == "0":
        print("\t\t İYİ GÜNLER GÖRÜŞMEK ÜZERE!")
        sys.exit()
    else:
        print("Yanlış giriş:")
    menu(hesap)

def bakiyeSorgula(hesap):
    print()
    print(f"Hesabınızda bulunan bakiye: {hesap["bakiye"]}")
    print(f"Hesabınızda bulunan ek hesap bakiyesi: {hesap["ekHesap"]}")

def paraCekme(hesap):
    print()
    cekim_Mitari = int(input("Çekmek istediğiniz para miktarını giriniz:"))

    if(hesap["bakiye"]>=cekim_Mitari):
        hesap["bakiye"] -= cekim_Mitari
        print("Paranızı almayı unutmayın!")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if toplam >= cekim_Mitari:
            print("Bakiye Yetersiz!")
            ekHesapIzni = input("Ek hesap kullanılsın mı?(e/h)")
            if ekHesapIzni == "e":
                kullanilacakMiktar = cekim_Mitari - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= kullanilacakMiktar
                print("Paranızı alabilirsiniz!")
            else:
                print("Üzgünüz Bakiyeniz Yetersiz!")
        else :
            print("Üzgünüz Bakiyeniz Yetersiz!")

def paraYatirma(hesap):
    print()
    yatirmaMiktari = int(input("Yatırmak istediğiniz para miktarını giriniz:"))
    if yatirmaMiktari > 0:
        hesap["bakiye"] += yatirmaMiktari
        print("Para hesabınıza eklendi.")
    else:
        print("\t\t HATALI GİRİŞ!")

def login():
    username = input("username: ")
    password = input("password: ")

    isLoggedIn = False

    for hesap in hesap_Bilgileri:
        if hesap["username"] == username and hesap["password"] == password:
            isLoggedIn = True
            menu(hesap)
            break

    if not(isLoggedIn):
        print("username ya da parola yanlış!")

login()