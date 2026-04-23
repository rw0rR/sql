import tkinter as tk
from tkinter import ttk
import sqlite3

# --- VERİTABANI BAĞLANTISI ---
conn = sqlite3.connect('sql.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS kullanıcılar")
cursor.execute("CREATE TABLE kullanıcılar (id TEXT PRIMARY KEY, durum TEXT)")

# 50 Bilgisayarı "Aktif" olarak ekleyelim
for i in range(1, 51):
    cursor.execute("INSERT INTO kullanıcılar VALUES (?, ?)", (f'h{i}', 'Aktif'))
conn.commit()

def arayuzu_tazele():
    """Veritabanındaki son duruma göre renkleri günceller."""
    cursor.execute("SELECT id, durum FROM kullanıcılar")
    for pc_id, durum in cursor.fetchall():
        renk = "green" if durum == "Aktif" else "red"
        if pc_id in pc_butonlari:
            pc_butonlari[pc_id].config(bg=renk)

def sql_calistir():
    """Senin yazdığın SQL komutunu çalıştırır."""
    komut = sql_giris.get()
    try:
        cursor.execute(komut)
        conn.commit()
        arayuzu_tazele()
        durum_etiketi.config(text="SQL Başarıyla Çalıştı!", fg="blue")
    except Exception as e:
        durum_etiketi.config(text=f"Hata: {e}", fg="red")

# --- PENCERE TASARIMI ---
root = tk.Tk()
root.title("SQL Admin Kontrol Merkezi")
root.geometry("700x600")

# Üst Kısım: 50 PC İkonu
frame_ust = tk.LabelFrame(root, text="Sistemdeki Bilgisayarlar (Yeşil=Aktif, Kırmızı=Atıldı)")
frame_ust.pack(pady=10, padx=10, fill="both")

pc_butonlari = {}
for i in range(1, 51):
    pid = f'h{i}'
    btn = tk.Label(frame_ust, text=pid, width=5, height=2, bg="green", fg="white", relief="raised")
    row = (i-1) // 10
    col = (i-1) % 10
    btn.grid(row=row, column=col, padx=3, pady=3)
    pc_butonlari[pid] = btn

# Alt Kısım: SQL Manuel Kontrol
frame_alt = tk.LabelFrame(root, text="Manuel SQL Komut Paneli")
frame_alt.pack(pady=20, padx=10, fill="x")

tk.Label(frame_alt, text="Komut Gir:").pack(side="left", padx=5)
sql_giris = tk.Entry(frame_alt, width=50)
sql_giris.pack(side="left", padx=5)
sql_giris.insert(0, "UPDATE kullanıcılar SET durum='Pasif' WHERE id='h56'")

btn_run = tk.Button(frame_alt, text="KOMUTU ÇALIŞTIR", command=sql_calistir, bg="orange")
btn_run.pack(side="left", padx=5)

durum_etiketi = tk.Label(root, text="Sistem Hazır", font=("Arial", 10, "italic"))
durum_etiketi.pack(pady=5)

root.mainloop()