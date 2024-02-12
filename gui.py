import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self):
        self.dosya_adi = "kitaplar.txt"
        self.dosya = open(self.dosya_adi, "a+")

    def __del__(self):
        self.dosya.close()

    def kitaplari_listele(self):
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        if not kitaplar:
            messagebox.showinfo("Bilgi", "Kitap bulunamadı.")
            return
        kitaplar_listesi = ""
        for kitap in kitaplar:
            kitap_bilgisi = kitap.strip().split(',')
            kitaplar_listesi += f"Başlık: {kitap_bilgisi[0]}, Yazar: {kitap_bilgisi[1]}, Yayın Yılı: {kitap_bilgisi[2]}, Sayfa Sayısı: {kitap_bilgisi[3]}\n"
        return kitaplar_listesi

    def kitap_ekle(self, baslik, yazar, yayin_yili, sayfa_sayisi):
        kitap_bilgisi = f"{baslik},{yazar},{yayin_yili},{sayfa_sayisi}\n"
        self.dosya.write(kitap_bilgisi)
        messagebox.showinfo("Bilgi", "Kitap başarıyla eklendi.")

    def kitap_sil(self, baslik):
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
            messagebox.showinfo("Bilgi", "Kitap başarıyla silindi.")
        else:
            messagebox.showinfo("Bilgi", "Kitap bulunamadı.")

    def kitap_ara(self, arama_terimi):
        self.dosya.seek(0)
        kitaplar = self.dosya.readlines()
        bulunan_kitaplar = []
        for kitap in kitaplar:
            kitap_bilgisi = kitap.strip().split(',')
            if arama_terimi.lower() in [bilgi.lower() for bilgi in kitap_bilgisi]:
                bulunan_kitaplar.append(kitap_bilgisi)
        if bulunan_kitaplar:
            return bulunan_kitaplar
        else:
            messagebox.showinfo("Bilgi", "Arama sonucunda hiçbir kitap bulunamadı.")

def list_books():
    kitaplar = lib.kitaplari_listele()
    if kitaplar:
        listbox = tk.Listbox(root, width=256, bg='gray', fg='white')
        for kitap in kitaplar.split('\n'):
            listbox.insert(tk.END, kitap)
        listbox.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

def add_book():
    baslik = baslik_entry.get()
    yazar = yazar_entry.get()
    yayin_yili = yayin_yili_entry.get()
    sayfa_sayisi = sayfa_sayisi_entry.get()
    lib.kitap_ekle(baslik, yazar, yayin_yili, sayfa_sayisi)

def remove_book():
    baslik = baslik_entry.get()
    lib.kitap_sil(baslik)

def search_book():
    arama_terimi = arama_entry.get()
    bulunan_kitaplar = lib.kitap_ara(arama_terimi)
    if bulunan_kitaplar:
        search_window = tk.Toplevel(root)
        search_window.title("Kitap Arama Sonuçları")
        search_window.geometry("400x300")
        search_window.configure(bg='black')

        listbox = tk.Listbox(search_window, width=250, bg='gray', fg='white')
        for kitap in bulunan_kitaplar:
            kitap_bilgisi = f"Başlık: {kitap[0]}, Yazar: {kitap[1]}, Yayın Yılı: {kitap[2]}, Sayfa Sayısı: {kitap[3]}"
            listbox.insert(tk.END, kitap_bilgisi)
        listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    else:
        messagebox.showinfo("Bilgi", "Arama sonucunda hiçbir kitap bulunamadı.")

def close_app():
    answer = messagebox.askyesno("Uygulamadan Çık", "Uygulamadan çıkmak istediğinize emin misiniz?")
    if answer:
        messagebox.showinfo("Bilgi", "Oturum Sonlandırıldı. İyi Günler.")
        root.destroy()

lib = Library()

root = tk.Tk()
root.title("Kütüphane Yönetim Sistemi")
root.configure(bg='black')

# Grid yöntemiyle bileşenleri yerleştirme
baslik_label = tk.Label(root, text="Başlık:", bg='black', fg='white', activebackground='white', activeforeground='green')
baslik_label.grid(row=0, column=0, padx=5, pady=5)
baslik_entry = tk.Entry(root, bg='gray', fg='white')
baslik_entry.grid(row=0, column=1, padx=5, pady=5)

yazar_label = tk.Label(root, text="Yazar:", bg='black', fg='white', activebackground='white', activeforeground='green')
yazar_label.grid(row=1, column=0, padx=5, pady=5)
yazar_entry = tk.Entry(root, bg='white', fg='black')
yazar_entry.grid(row=1, column=1, padx=5, pady=5)

yayin_yili_label = tk.Label(root, text="Yayın Yılı:", bg='black', fg='white', activebackground='white', activeforeground='green')
yayin_yili_label.grid(row=2, column=0, padx=5, pady=5)
yayin_yili_entry = tk.Entry(root, bg='gray', fg='white')
yayin_yili_entry.grid(row=2, column=1, padx=5, pady=5)

sayfa_sayisi_label = tk.Label(root, text="Sayfa Sayısı:", bg='black', fg='white', activebackground='white', activeforeground='green')
sayfa_sayisi_label.grid(row=3, column=0, padx=5, pady=5)
sayfa_sayisi_entry = tk.Entry(root, bg='white', fg='black')
sayfa_sayisi_entry.grid(row=3, column=1, padx=5, pady=5)

arama_label = tk.Label(root, text="Arama:", bg='black', fg='white', activebackground='white', activeforeground='green')
arama_label.grid(row=4, column=0, padx=5, pady=5)
arama_entry = tk.Entry(root, bg='green', fg='white')
arama_entry.grid(row=4, column=1, padx=5, pady=5)

list_button = tk.Button(root, text="Kitapları Listele", command=list_books, bg='gray', fg='white', activebackground='white', activeforeground='green')
list_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

add_button = tk.Button(root, text="Kitap Ekle", command=add_book, bg='gray', fg='white', activebackground='white', activeforeground='green')
add_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

remove_button = tk.Button(root, text="Kitap Sil", command=remove_book, bg='gray', fg='white', activebackground='white', activeforeground='green')
remove_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

search_button = tk.Button(root, text="Kitap Ara", command=search_book, bg='gray', fg='white', activebackground='white', activeforeground='green')
search_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

quit_button = tk.Button(root, text="Çıkış", command=close_app, bg='gray', fg='white')
quit_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Otomatik boyutlandırma için ayarlar
for i in range(10):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
