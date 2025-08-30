def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')

    ogenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if 90 <= ortalama <= 100: harf="AA"
    elif 80 <= ortalama < 90: harf="BA"
    elif 75 <= ortalama < 80: harf="BB"
    elif 70 <= ortalama < 75: harf="CB"
    elif 65 <= ortalama < 70: harf="CC"
    elif 60 <= ortalama < 65: harf="DC"
    elif 50 <= ortalama < 60: harf="DD"
    elif 40 <= ortalama < 50: harf="FD"
    else: harf="FF"

    return f"{ogenciAdi} : {harf} - ({ortalama})\n"


def not_gir():
    ad = input("Öğrenci Adı:")
    soyad = input("Öğrenci Soyadı:")
    not1 = input("Not 1:")
    not2 = input("Not 2:")
    not3 = input("Not 3:")

    with open("sinav_notlari.txt", "a", encoding="utf-8") as file:
        file.write(ad + " "+ soyad + ":"+ not1 + ","+ not2 + ","+ not3 + "\n")


def not_oku():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))


def not_kayit():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        liste = []

        for satir in liste:
            liste.append(not_hesapla(satir))

        with open("sonuclar.txt", "w", encoding="utf-8") as file2:
            file2.writelines(liste)


while True:
    islem = int(input("1-Not Gir\n2-Notları Oku\n3-Notları Kayıt Et\n4-Çıkış\nSeçim: "))
    if islem == 1:
        not_gir()
    elif islem == 2:
        not_oku()
    elif islem == 3:
        not_kayit()
    else:
        break