# 13010011040/BEYZA NUR ORUÇ

kursiyerList = []
alinanKurs = []
telNoList = []

dosya = open("13010011040.txt", 'w') # w moduyla dosya açıyoruz.

def kursiyerEkle():
    print("-" * 30)
    print("Kursiyer Ekleme İşlemleri")
    print("-" * 30)
    dosya =open("13010011040.txt",'a')# a modu vererek her bir kaydın bir alt satıra geçmesini sağlıyoruz.
    adSoyad = input("Lütfen kursiyer ad-soyad bilgisini giriniz:")
    kursAd = input("Lütfen alınacak kurs bilgisini giriniz:")
    telNo = int(input("Lütfen kursiyer telefon numarası bilgisini giriniz:"))
    dosya.write(adSoyad +" "+ kursAd +" "+ str(telNo) + "\n") #dosyaya yazdırıp bir alt satıra geçme
    dosya.close()
    kursiyerList.append(adSoyad)
    alinanKurs.append(kursAd)
    telNoList.append(telNo)
    print("Kayıt başarılı bir şekilde eklendi.")

    devam()
def kursiyerSil():
    print("-" * 30)
    print("Kursiyer Silme İşlemleri")
    print("-" * 30)
    adSoyad = input("Lütfen silmek istediğiniz Ad Soyad bilgisini giriniz:")
    if adSoyad in kursiyerList:
        while True:
            silinecekId = kursiyerList.index(adSoyad)
            karar = input("Kaydı silmek istediğinize emin misiniz?(E/H)")

            if karar == 'E':
                kursiyerList.pop(silinecekId)
                alinanKurs.pop(silinecekId)
                telNoList.pop(silinecekId)
                print("Kayıt silme başarılı bir şekilde tamamlandı.")
                dosya = open("13010011040.txt",'w')
                i = 0
                while i < len(kursiyerList):
                    dosya.write(kursiyerList[i] + " ")
                    dosya.write(alinanKurs[i] +" ")
                    dosya.write(telNoList[i] +"\n")
                    i = i+1
                dosya.close()
                break
            elif karar == 'H':
                print("Kayıt silme işlemi gerçekleşmedi.")
                break
            else:
                print("Lütfen doğru bir seçim yapınız..")
    else:
        print("Kayıt Bulunamadı..!")

    devam()
def kursiyerArama():
    print("-" * 30)
    print("Kursiyer Arama İşlemleri")
    print("-" * 30)
    adSoyad = input("Aranacak Ad Soyad bilgisini giriniz:")


    with open('13010011040.txt','r') as aramadosyasi:
        for satir in aramadosyasi:
            if adSoyad in satir:
                print(satir)
            else:
                print("Kayıt Bulunamadı..!")

    devam()
def kursiyerListele():
    print("-" * 30)
    print("Kursiyer Listesi:")
    print("-" * 30)
    print(f"{'Ad Soyad':10} {'Alınan Kurs':10} {'Telefon Numarası':10}")

    for kursiyerId in range(len(kursiyerList)):
        print(f"{kursiyerList[kursiyerId]:10} {alinanKurs[kursiyerId]:10} {telNoList[kursiyerId]:10}")

    devam()
def kursiyerGuncelle():

    print("-" * 30)
    print("Kursiyer Güncelleme İşlemleri")
    print("-" * 30)
    adSoyad = input("Güncelleme yapmak istediğiniz Ad Soyad bilgisini giriniz:")
    if adSoyad in kursiyerList:
        guncellenenId = kursiyerList.index(adSoyad)
        print(f"{'Ad Soyad':10} {'Alınan Kurs':10} {'Telefon Numarası':10}")
        print(f"{kursiyerList[guncellenenId]:10} {alinanKurs[guncellenenId]:10} {telNoList[guncellenenId]:10}")
        print("Kayıt arama işlemi başarılı bir şekilde tamamlandı.")
    else:
        print("Kayıt Bulunamadı..!")
    yeniadSoyad = input("Lütfen yeni kursiyer ad-soyad bilgisini giriniz:")
    yenikursAd = input("Lütfen yeni alınacak kurs bilgisini giriniz:")
    yenitelNo = int(input("Lütfen yeni kursiyer telefon numarası bilgisini giriniz:"))
    kursiyerList[guncellenenId] = yeniadSoyad
    alinanKurs[guncellenenId] = yenikursAd
    telNoList[guncellenenId] = yenitelNo
    open('13010011040.txt','w').close()
    dosya = open("13010011040.txt", 'w')
    i = 0
    while i < len(kursiyerList):
        dosya.write(kursiyerList[i] + " ")
        dosya.write(alinanKurs[i] + " ")
        dosya.write(telNoList[i] + "\n")
        i = i + 1
    dosya.close()
    print("Kayıt güncelleme işlemi başarılı bir şekilde tamamlandı.")

    devam()


def ucretHesapla():
    print("-" * 30)
    print("Ücret Hesaplama İşlemleri")
    print("-" * 30)
    kursSaat = int(input("Lütfen kursun toplam kaç saat olduğu bilgisini giriniz:"))
    saatlikUcret = int(input("Lütfen kursun saatlik ücretini giriniz:"))

    def saatHesapla(kursSaat):

        return kursSaat

    def saatUcret(saatlikUcret):

        return saatlikUcret

    print(saatHesapla(kursSaat)*saatUcret(saatlikUcret))

    devam()

def devam():
    islem =input("Yeni bir işlem yapmak ister misiniz?")
    if islem == 'E':
        menu()
    elif islem == 'H':
        return 0
    else:
        print("Lütfen doğru bir seçim yapınız..!")


def menu():
    islemListesi = (kursiyerEkle, kursiyerSil, kursiyerArama, kursiyerListele, kursiyerGuncelle, ucretHesapla)
    # OLuşturulan tuple sayesinde pratik olarak fonksiyonlara erişim sağlanıyor.
    print("*** YABANCI DİL KURSLARIMIZA HOŞGELDİNİZ ***")
    print("Mevcut Kurslarımız:\n*Almanca*\n*Fransızca*\n*İngilizce*\n*İspanyolca*")
    while True:
        print("*" * 30)
        print("1-Kursiyer Ekle:")
        print("2-Kursiyer Sil:")
        print("3-Kursiyer Arama:")
        print("4-Kursiyer Listele:")
        print("5-Kursiyer Güncelle:")
        print("6-Ücret Hesapla:")
        print("0-Çıkış:")
        print("*" * 30)
        secim = int(input("Lütfen bir işlem seçiniz(0-6):"))

        if secim <= 6 and secim >= 1:
            islemListesi[secim - 1]()
            print("-" * 30)
        elif secim == 0:
            print("Çıkış yapılıyor..")
            break
        else:
            print("Lütfen 0 ile 6 arası bir seçim yapınız..!")

menu()


