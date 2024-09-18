import cv2
from zxingcpp import read_barcodes  # Zxing-cpp ile hem barkod hem Data Matrix okuyacağız
import tkinter as tk
from tkinter import simpledialog
import pyperclip
import os
import winsound
import subprocess  # Enlil işlemlerini başlatmak için

# Data Matrix ve barkod işlemlerini ayıracağız
memory_file = "codes_memory.txt"
codes_memory = {}

# Eğer dosya mevcutsa kod ve tanımları yükle, yoksa boş bir dictionary başlat
if os.path.exists(memory_file):
    with open(memory_file, 'r') as f:
        for line in f:
            code, description = line.strip().split(': ', 1)
            codes_memory[code] = description

# Sonuçları saklamak için liste
results = []
open_windows = {}
read_codes = set()  # Daha önce okunan Data Matrix kodlarını takip etmek için

# Tkinter arayüzü
root = tk.Tk()
root.withdraw()  # Tkinter arayüzü Data Matrix kodu tespit edilene kadar gizlenir

# Sonuçları clipboard'a kopyalama fonksiyonu
def copy_to_clipboard():
    clipboard_text = "\n".join([f"{desc}: {result}" for desc, result in results])
    pyperclip.copy(clipboard_text)
    copy_button.config(text="Kopyalandı")  # Tuş yazısını "Kopyalandı" olarak değiştir

# Sonuç ekleme fonksiyonu
def add_result(code, description, result):
    results.append((description, result))
    result_display.insert(tk.END, f"{description}: {result}\n")

# Data Matrix işlemleri
def handle_data_matrix(code):
    if code in read_codes:
        winsound.Beep(500, 500)  # Farklı ses çıkar
        read_codes.add(code)  # Yine de işlem yap
    else:
        winsound.Beep(1000, 200)  # Bip sesi çıkar
        read_codes.add(code)  # Yeni kodu takip listesine ekle

    if code not in open_windows:
        if code not in codes_memory:
            description = simpledialog.askstring("Yeni Kod", f"Yeni kod bulundu: {code}. Lütfen tanım girin:")
            if description:
                codes_memory[code] = description
                with open(memory_file, 'a') as f:
                    f.write(f"{code}: {description}\n")
        else:
            description = codes_memory[code]
            result_window = tk.Toplevel(root)
            result_window.title(description)
            result_window.attributes('-topmost', True)  # Pencereyi ön planda tut
            open_windows[code] = result_window

            description_label = tk.Label(result_window, text=description, font=("Helvetica", 24, "bold"))
            description_label.pack()

            pos_button = tk.Button(result_window, text="Pozitif", command=lambda: [add_result(code, description, "Pozitif"), result_window.destroy()])
            neg_button = tk.Button(result_window, text="Negatif", command=lambda: [add_result(code, description, "Negatif"), result_window.destroy()])
            pos_button.config(bg="orange")  # Pozitif butonu turuncu
            neg_button.config(bg="cyan")  # Negatif butonu cyan
            pos_button.pack()
            neg_button.pack()

            input_entry = tk.Entry(result_window, font=("Helvetica", 20))
            input_entry.pack()

            def submit_result():
                boya_result = input_entry.get()
                if boya_result:
                    add_result(code, description, boya_result)
                result_window.destroy()
                open_windows.pop(code, None)

            submit_button = tk.Button(result_window, text="Sonuç Gir", command=submit_result, bg="light blue")
            submit_button.pack()

# Barkod işlemleri
def handle_barcode(barcode_code):
    print(f"Barkod tespit edildi: {barcode_code}")
    if "/" in barcode_code:
        result_display.insert(tk.END, "Enlil işlemi başlatılıyor...\n")
        # Enlil işlemi başlatılıyor
        subprocess.Popen(['python', 'C:\\path_to_enlil\\enlil_ocr_process.pyw'])  # Enlil işlemini başlatır
    else:
        result_display.insert(tk.END, f"Barkod tespit edildi: {barcode_code}\n")

# Kamera döngüsü
def camera_loop():
    ret, frame = cap.read()
    if ret:
        decoded_objects = read_barcodes(frame)
        for obj in decoded_objects:
            if obj.format == "DataMatrix" or len(obj.text) > 20:  # Uzun şifreli görünen kodlar Data Matrix olabilir
                root.deiconify()  # Data Matrix kodu tespit edilince Tkinter arayüzünü aç
                handle_data_matrix(obj.text)
            else:
                handle_barcode(obj.text)

        cv2.imshow('Kamera', frame)
    root.after(100, camera_loop)

# "Kapat" tuşu
def close_session():
    root.withdraw()  # Arayüzü gizle, kamera çalışmaya devam etsin

# GUI elemanları
result_display = tk.Text(root, height=15, width=70)
result_display.pack()

copy_button = tk.Button(root, text="Kopyala", command=copy_to_clipboard, bg="yellow")
copy_button.pack(side=tk.LEFT, padx=10, pady=10)

close_button = tk.Button(root, text="Kapat", command=close_session, bg="red")
close_button.pack(side=tk.LEFT, padx=10, pady=10)

# Kamera başlatma ve GUI döngüsü
cap = cv2.VideoCapture(0)  # Kamera numarası 0, gerekirse 1 olarak değiştir
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

root.after(100, camera_loop)
root.mainloop()

cap.release()
cv2.destroyAllWindows()
