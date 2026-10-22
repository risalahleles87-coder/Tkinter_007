import tkinter as tk

top = tk.Tk()
top.title("Prediksi Prodi")

# 1 label judul
L1 = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
L1.pack(pady=10)

# 10 input nilai mata pelajaran
mapel = ["Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
         "Biologi", "Ekonomi", "Sejarah", "Geografi", "Informatika"]
