import sys

hesap_Bilgileri = {
    1234: {
        "Ad":"Hasan",
        "Soyad":"Yılmaz",
        "Bakiye":2500,
        "Sifre":1234
    },
    5678: {
        "Ad":"Hüseyin",
        "Soyad":"Çakmak",
        "Bakiye":2000,
        "Sifre":5678
    },
    9123: {
        "Ad":"Salih",
        "Soyad":"Korkmaz",
        "Bakiye":5000,
        "Sifre":9123
    }
}
def menu():
    yonlendir = girdi_Alici(menu)
    if(yonlendir == 1):
        paraCekme()
    elif(yonlendir == 2):
        bakiyeSorgula()
    elif(yonlendir == 3):
        paraYatirma()
    elif(yonlendir == 0):
        print("İyi Günler, Görüşmek Üzere!")
        sys.exit()

def sifreSorgula():
    sifre = int(input("Lütfen hesabınızın 4 haneli şifresini giriniz: "))
    while(sifre<1000 or sifre>9999):
        print("Hatalı giriş!")
        sifre = int(input("Lütfen 4 haneli şifrenizi tekrar giriniz: "))
    return sifre

def paraCekme():
    sifre = sifreSorgula()
    cekim_Miktari = int(input("Ne kadar para çekmek istiyorsunuz? "))
    if(hesap_Bilgileri[sifre]["Bakiye"] < cekim_Miktari):
        print("Yetersiz Bakiye!")
        print("Ek hesabı kullanmak ister misiniz?")
        ek_Hesap = girdi_Alici(paraCekme)
        if(ek_Hesap == 1):
            ek_Hesap_Kullan()
        elif(ek_Hesap == 0):
            print("Para çekim miktarını güncellemek için 1'i,")
            guncelleme = int(input("Menüye dönmek için 0'ı tuşlayınız: "))
            while(guncelleme<0 or guncelleme>1):
                print("Hatalı Giriş Yaptınız!")
                print("Para çekim miktarını güncellemek için 1'i,")
                guncelleme = int(input("Menüye dönmek için 0'ı tuşlayınız: "))
            
        

        cekim_Miktari = int(input("Ne kadar para çekmek istiyorsunuz? "))

def bakiyeSorgula():
    hesap_Sorgula()
    sifre = sifreSorgula()
    print(hesap_Bilgileri[sifre]["Bakiye"])

def paraYatirma():
    print()

def ek_Hesap_Kullan():
    print("Ek hesap")

def hesap_Sorgula():
    ad = input("Adınızı giriniz: ")
    soyad = input("Soyadınızı giriniz:")
    sifre = sifreSorgula()
    for i in hesap_Bilgileri:
        if(hesap_Bilgileri[i]["Ad"]["Soyad"]["Sifre"] == hesap_Bilgileri[i][ad][soyad][sifre]):
            return sifre
    print("Hatalı giriş")

def girdi_Alici(fonk):
    if(fonk == menu):
        print("Para çekme için 1'i,")
        print("Bakiye Sorgulama için 2'yi,")
        print("Para yatırma için 3'ü,")
        yonlendir = int(input("Çıkış yapmak için 0'ı tuşlayınız:"))
        while(yonlendir<0 or yonlendir>3):
            print("")
            print("                             Hatalı Giriş!")
            print("Para çekme için 1'i,")
            print("Bakiye Sorgulama için 2'yi,")
            print("Para yatırma için 3'ü,")
            yonlendir = int(input("Çıkış yapmak için 0'ı tuşlayınız:"))
        return yonlendir
    
    if (fonk == paraCekme):
        ek_Hesap = int(input("Evet için 1'i, Hayır için 0'ı tuşlayınız: "))
        while(ek_Hesap<0 or ek_Hesap>1):
            print("Hatalı Giriş Yaptınız!")
            ek_Hesap = int(input("Lütfen evet için 1'i, Hayır için 0'ı tuşlayınız: "))
        return ek_Hesap

    # while(guncelleme<0 or guncelleme>1):
    #     print("Hatalı Giriş Yaptınız!")
    #     print("Para çekim miktarını güncellemek için 1'i,")
    #     guncelleme = int(input("Menüye dönmek için 0'ı tuşlayınız: "))

menu()