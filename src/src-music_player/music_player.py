class MusicPlayer():
    def __init__(self, isim = "mp3", model = "yeni"):
        self.isim = isim
        self.model = model
        self.run = True
        self.kullanici_ismi = input('Kullanıcı İsminiz: ')
        self.kullanici_no = "1234567890"
        self.yas = 13
        self.tasarim = input("""
        
------------¨~ MÜZİK ÇARLAR (MP3) ~¨------------
|  #Yapabileceğiniz İşlemler:
|   1- Şarkı Ekleme
|   2- Şarkı Silme
|   3- Ses ayarları
|   4- Müzik çalar Bilgileri
|   5- Müzik çalar Listeniz
|   Q- ÇIKIŞ
|--> Yapmak istediğniz işlemi girin : 
""")
        self.liste = []
        self.ses_deger = 100
    def dongu(self):
        while self.run:
            print(self.tasarim)
            
            if self.tasarim == "1":
                self.sarki_ekle = input('|Eklemek istediğniz şarkıyı girin: ')
            
                self.liste.append(self.sarki_ekle)
            elif self.tasarim == "2":
                while self.run:    
                    self.sarki_silme = input('|Silmek istediğniz Sarkıyı girin: ')
                    if self.sarki_silme in self.liste:
                        self.liste.remove(self.sarki_silme)
                        break
                    else:
                        print('|Hatalı giriş ... :)')
                        continue
            elif self.tasarim == "3":
                while self.run:
                    self.ses = input('Sesi artırmak için "artır" ya azaltmak için "azalt" artır yazın. Çıkmak için de "çıkış" yazın.')
                    if self.ses == "artır":
                        self.ses_artirmadegeri = int(input('|Ne kadar artırılsın: '))
                        if self.ses_deger == 100 or self.ses_artirmadegeri >= 101 or self.ses + self.ses_artirmadegeri > 100:
                            print('|Ses artırlamıyor çünkü zaten yeteri kadar fazla')
                            break
                        elif self.ses_artirmadegeri < 0:
                            print('|Positif değer girin.')
                            break
                        else:
                            self.ses_deger = self.ses_deger + self.ses
                            print('|Ses değeriniz: {}'.format(self.ses_deger))
                            break
                    elif self.ses == "azalt":
                        self.ses_azaltmadegeri = int(input('|Ne kadar azaltılsın: '))
                        if self.ses_deger == 0 or self.ses_azaltmadegeri >= 101 or self.ses_azaltmadegeri - self.ses_deger < 0:
                            print('|Ses azalatılamıyor çünkü zanten çok kısık.')
                            continue
                        elif self.ses_azaltmadegeri < 0:
                            print('|Ses azaltmak için pozitif değer girin [çünkü pozitif olara düşürülüyor.]')
                            continue
                        else:
                            self.ses_deger = self.ses_deger - self.ses_azaltmadegeri
                            print('|Ses değeriniz: {}'.format(self.ses_deger))
                            continue
            elif self.tasarim == "4":
                print("\#MÜZİK ÇALAR BİLGİLERİ:\n-------------------------\n|İsim: {}\n|Yas: {}\n|Kullanıcı No: {}\n-------------------------".format(self.kullanici_ismi, self.yas, self.kullanici_no))
            elif self.tasarim == "5":
                print('Şarkılarınız:\n-----------------')
                for self.sarki in self.liste:
                    print("{} - {}".format(self.sayi, self.liste[self.sarki]))
                    self.sayi += 1
                continue
            elif self.tasarim.lower() == "q":
                print('Sistemden çıkılıyor\n.\n.\n.')
                run = False
            else:
                continue

music_calar = MusicPlayer('Yigit\'in Müzik çaları')