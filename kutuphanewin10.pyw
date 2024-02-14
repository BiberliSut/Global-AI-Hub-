import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from datetime import datetime

class KutuphaneGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("Kütüphane Yönetim Portalı (Programlayan: Erdem Erçetin)")
        
        self.kutuphane = Kutuphane()

        self.create_widgets()

    def create_widgets(self):
        self.master.config(bg='#333333')
        
        self.menu_frame = ttk.Frame(self.master)
        self.menu_frame.pack(padx=10, pady=10)

        self.menu_label = ttk.Label(self.menu_frame, text="Tarih")
        self.menu_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.list_button = ttk.Button(self.menu_frame, text="Kitapları Listele", command=self.kitaplari_listele, takefocus=0)
        self.list_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        self.list_button.bind("<Enter>", lambda event: self.list_button.config(background="#0055ff", foreground="#ffffff"))
        self.list_button.bind("<Leave>", lambda event: self.list_button.config(background="#007fff", foreground="#ffffff"))

        self.add_button = ttk.Button(self.menu_frame, text="Kitap Ekle", command=self.kitap_ekle, takefocus=0)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        self.add_button.bind("<Enter>", lambda event: self.add_button.config(background="#0055ff", foreground="#ffffff"))
        self.add_button.bind("<Leave>", lambda event: self.add_button.config(background="#007fff", foreground="#ffffff"))

        self.delete_button = ttk.Button(self.menu_frame, text="Kitap Sil", command=self.kitap_sil, takefocus=0)
        self.delete_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        self.delete_button.bind("<Enter>", lambda event: self.delete_button.config(background="#0055ff", foreground="#ffffff"))
        self.delete_button.bind("<Leave>", lambda event: self.delete_button.config(background="#007fff", foreground="#ffffff"))

        self.update_button = ttk.Button(self.menu_frame, text="Kitap Bilgilerini Güncelle", command=self.kitap_guncelle, takefocus=0)
        self.update_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        self.update_button.bind("<Enter>", lambda event: self.update_button.config(background="#0055ff", foreground="#ffffff"))
        self.update_button.bind("<Leave>", lambda event: self.update_button.config(background="#007fff", foreground="#ffffff"))

        self.search_button = ttk.Button(self.menu_frame, text="Kitap Ara", command=self.kitap_ara, takefocus=0)
        self.search_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        self.search_button.bind("<Enter>", lambda event: self.search_button.config(background="#0055ff", foreground="#ffffff"))
        self.search_button.bind("<Leave>", lambda event: self.search_button.config(background="#007fff", foreground="#ffffff"))

        self.exit_button = ttk.Button(self.menu_frame, text="Çıkış", command=self.exit_app, takefocus=0)
        self.exit_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        self.exit_button.bind("<Enter>", lambda event: self.exit_button.config(background="#0055ff", foreground="#ffffff"))
        self.exit_button.bind("<Leave>", lambda event: self.exit_button.config(background="#007fff", foreground="#ffffff"))

        self.date_label = ttk.Label(self.menu_frame, text="", font=("Helvetica", 12), background='#333333', foreground='white')
        self.date_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        self.update_date_time()

        self.output_frame = ttk.Frame(self.master)
        self.output_frame.pack(padx=10, pady=10)

        self.tree = ttk.Treeview(self.output_frame, columns=('Başlık', 'Yazar', 'Yayın Yılı', 'Sayfa Sayısı'), show='headings')
        self.tree.heading('Başlık', text='Başlık')
        self.tree.heading('Yazar', text='Yazar')
        self.tree.heading('Yayın Yılı', text='Yayın Yılı')
        self.tree.heading('Sayfa Sayısı', text='Sayfa Sayısı')
        self.tree.pack(expand=True, fill="both", padx=5, pady=5)

        self.kitaplari_listele()

    def update_date_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%d-%m-%Y")
        self.date_label.config(text=f"{current_date}  {current_time}")
        self.date_label.after(1000, self.update_date_time)

    def kitaplari_listele(self):
        self.tree.delete(*self.tree.get_children())
        kitaplar = self.kutuphane.kitaplari_listele()
        for kitap in kitaplar:
            self.tree.insert('', 'end', values=kitap)

    def kitap_ekle(self):
        baslik = simpledialog.askstring("Kitap Ekle", "Kitabın başlığını girin:")
        yazar = simpledialog.askstring("Kitap Ekle", "Kitabın yazarını girin:")
        yayin_yili = simpledialog.askstring("Kitap Ekle", "Yayın yılını girin:")
        sayfa_sayisi = simpledialog.askstring("Kitap Ekle", "Sayfa sayısını girin:")
        self.kutuphane.kitap_ekle(baslik, yazar, yayin_yili, sayfa_sayisi)
        self.kitaplari_listele()

    def kitap_sil(self):
        baslik = simpledialog.askstring("Kitap Sil", "Silmek istediğiniz kitabın tam adını girin:")
        self.kutuphane.kitap_sil(baslik)
        self.kitaplari_listele()

    def kitap_guncelle(self):
        baslik = simpledialog.askstring("Kitap Güncelle", "Güncellemek istediğiniz kitabın başlığını girin:")
        self.kutuphane.kitap_guncelle(baslik)
        self.kitaplari_listele()

    def kitap_ara(self):
        sorgu = simpledialog.askstring("Kitap Ara", "Arama sorgusunu girin (başlık, yazar, yayın yılı veya sayfa sayısı):")
        self.tree.delete(*self.tree.get_children())
        kitaplar = self.kutuphane.kitap_ara(sorgu)
        for kitap in kitaplar:
            self.tree.insert('', 'end', values=kitap)

    def exit_app(self):
        answer = messagebox.askyesno("Uygulamadan Çık", "Oturumu sonlandırmak istediğinize emin misiniz?")
        if answer:
            self.kutuphane.dosya.close()
            self.master.destroy()
            messagebox.showinfo("Çıkış", "Oturumunuz sonlandırıldı. İyi günler!")


class Kutuphane:
    def __init__(self):
        self.dosya_adi = "kitaplar.txt"
        self.dosya = open(self.dosya_adi, "a+")

    def __del__(self):
        self.dosya.close()

    def kitaplari_listele(self):
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        kitaplar_listesi = []
        for kitap in kitaplar:
            kitap_bilgisi = kitap.strip().split(',')
            kitaplar_listesi.append((kitap_bilgisi[0], kitap_bilgisi[1], kitap_bilgisi[2], kitap_bilgisi[3]))
        return kitaplar_listesi

    def kitap_ekle(self, baslik, yazar, yayin_yili, sayfa_sayisi):
        kitap_bilgisi = f"{baslik},{yazar},{yayin_yili},{sayfa_sayisi}\n"
        self.dosya.write(kitap_bilgisi)

    def kitap_sil(self, baslik):
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        guncellenmis_kitaplar = []
        for kitap in kitaplar:
            kitap_bilgisi = kitap.strip().split(',')
            if kitap_bilgisi[0] != baslik:
                guncellenmis_kitaplar.append(kitap)
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(guncellenmis_kitaplar)
# Algoritma ve kodlama Erdem Erçetin'e olup , scrum ve proje kaynak tahkimi Cem Berk Çıracı tarafından analiz edilmiştir.
    # Akbank Global AI World sertifika programına dahil olup 3. kişiler tarafından aynı amaçla kullanılması kesinlikle yasaktır.
    def kitap_guncelle(self, baslik):
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        guncellenmis_kitaplar = []
        for kitap in kitaplar:
            kitap_bilgisi = kitap.strip().split(',')
            if kitap_bilgisi[0] == baslik:
                yazar = simpledialog.askstring("Kitap Güncelle", "Yeni yazarı girin (Değiştirmek istemiyorsanız için boş bırakın):")
                yayin_yili = simpledialog.askstring("Kitap Güncelle", "Yeni yayın yılını girin (Değiştirmek istemiyorsanız için boş bırakın):")
                sayfa_sayisi = simpledialog.askstring("Kitap Güncelle", "Yeni sayfa sayısını girin (Değiştirmek istemiyorsanız için boş bırakın):")
                if yazar:
                    kitap_bilgisi[1] = yazar
                if yayin_yili:
                    kitap_bilgisi[2] = yayin_yili
                if sayfa_sayisi:
                    kitap_bilgisi[3] = sayfa_sayisi
                guncellenmis_kitaplar.append(','.join(kitap_bilgisi) + '\n')
            else:
                guncellenmis_kitaplar.append(kitap)
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(guncellenmis_kitaplar)

    def kitap_ara(self, sorgu):
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        bulunan_kitaplar = []
        for kitap in kitaplar:
            kitap_bilgisi = kitap.strip().split(',')
            if any(sorgu in bilgi.lower() for bilgi in kitap_bilgisi):
                bulunan_kitaplar.append((kitap_bilgisi[0], kitap_bilgisi[1], kitap_bilgisi[2], kitap_bilgisi[3]))
        return bulunan_kitaplar

root = tk.Tk()
app = KutuphaneGUI(root)
root.mainloop()
