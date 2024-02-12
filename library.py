class Kutuphane:
    def __init__(self):
        self.dosya_adi = "kitaplar.txt"
        self.dosya = open(self.dosya_adi, "a+")

    def __del__(self):
        self.dosya.close()

    def kitaplari_listele(self):
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        if not kitaplar:
            print("Kitap bulunamadı. Üst menüye yönlendiriliyor...")
            return
        for kitap in kitaplar:
            kitap_bilgisi = kitap.strip().split(',')
            print(f"Başlık: {kitap_bilgisi[0]}, Yazar: {kitap_bilgisi[1]}, Yayın Yılı: {kitap_bilgisi[2]}, Sayfa Sayısı: {kitap_bilgisi[3]}")

    def kitap_ekle(self):
        baslik = input("Kitabın başlığını girin: ")
        yazar = input("Kitabın yazarını girin: ")
        yayin_yili = input("Yayın yılını girin: ")
        sayfa_sayisi = input("Sayfa sayısını girin: ")
        kitap_bilgisi = f"{baslik},{yazar},{yayin_yili},{sayfa_sayisi}\n"
        self.dosya.write(kitap_bilgisi)
        print("Kitabınız başarıyla eklendi.")

    def kitap_sil(self):
        baslik = input("Silmek istediğiniz kitabın tam adını girin: ")
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        guncellenmis_kitaplar = []
        bulundu = False
        for kitap in kitaplar:
            kitap_bilgisi = kitap.strip().split(',')
            if kitap_bilgisi[0] == baslik:
                bulundu = True
            else:
                guncellenmis_kitaplar.append(kitap)
        if bulundu:
            self.dosya.seek(0)
            self.dosya.truncate()
            self.dosya.writelines(guncellenmis_kitaplar)
            print("Kitap başarıyla silindi.")
        else:
            print("Kitap bulunamadı.Üst menüye yönlendiriliyor...")

    def kitap_guncelle(self):
        baslik = input("Güncellemek istediğiniz kitabın başlığını girin: ")
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        guncellenmis_kitaplar = []
        bulundu = False
        for kitap in kitaplar:
            kitap_bilgisi = kitap.strip().split(',')
            if kitap_bilgisi[0] == baslik:
                bulundu = True
                yazar = input("Yeni yazarı girin (Değiştirmek istemiyorsanız için boş bırakın): ")
                yayin_yili = input("Yeni yayın yılını girin (Değiştirmek istemiyorsanız için boş bırakın): ")
                sayfa_sayisi = input("Yeni sayfa sayısını girin (Değiştirmek istemiyorsanız için boş bırakın): ")
                if yazar:
                    kitap_bilgisi[1] = yazar
                if yayin_yili:
                    kitap_bilgisi[2] = yayin_yili
                if sayfa_sayisi:
                    kitap_bilgisi[3] = sayfa_sayisi
                guncellenmis_kitaplar.append(','.join(kitap_bilgisi) + '\n')
            else:
                guncellenmis_kitaplar.append(kitap)
        if bulundu:
            self.dosya.seek(0)
            self.dosya.truncate()
            self.dosya.writelines(guncellenmis_kitaplar)
            print("Kitabınız başarıyla güncellendi.")
        else:
            print("Kitap bulunamadı.Üst menüye yönlendiriliyor...")

    def kitap_ara(self):
        sorgu = input("Arama sorgusunu girin (başlık, yazar, yayın yılı veya sayfa sayısı): ").lower()
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        bulunan_kitaplar = []
        for kitap in kitaplar:
            kitap_bilgisi = kitap.strip().split(',')
            if any(sorgu in bilgi.lower() for bilgi in kitap_bilgisi):
                bulunan_kitaplar.append(kitap_bilgisi)
        if bulunan_kitaplar:
            print("Bulunan Kitaplar:")
            for kitap_bilgisi in bulunan_kitaplar:
                print(f"Başlık: {kitap_bilgisi[0]}, Yazar: {kitap_bilgisi[1]}, Yayın Yılı: {kitap_bilgisi[2]}, Sayfa Sayısı: {kitap_bilgisi[3]}")
        else:
            print("Arama sorgusuna uyan kitap bulunamadı.Üst menüye yönlendiriliyor...")


kutuphane = Kutuphane()
import time

while True:
    print("\n*** MENÜ ***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekleyin")
    print("3) Kitap Silin")
    print("4) Kitap Bilgilerini Güncelleyin")
    print("5) Kitap Ara")
    print("6) Çıkış")
    
    secim = input("Lütfen seçiminizi girin: ")
    
    if secim == '1':
        kutuphane.kitaplari_listele()
    elif secim == '2':
        kutuphane.kitap_ekle()
    elif secim == '3':
        kutuphane.kitap_sil()
    elif secim == '4':
        kutuphane.kitap_guncelle()
    elif secim == '5':
        kutuphane.kitap_ara()
    elif secim == '6':
        print("Veritabanı kapatılıyor...")
        time.sleep(2)
        print("Bizi tercih ettiğiniz için Teşekkürler. İyi günler.")
        break
    else:
        print("Geçersiz seçim. Lütfen 1 ile 6 arasında bir sayı girin.")
