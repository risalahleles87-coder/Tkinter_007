import tkinter as tk

top = tk.Tk()
top.title("Prediksi Prodi")

# 1 label judul
L1 = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
L1.pack(pady=10)

# 10 input nilai mata pelajaran
mapel = ["Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
         "Biologi", "Ekonomi", "Sejarah", "Geografi", "Informatika"]
entries = []
for m in mapel:
    f = tk.Frame(top)
    f.pack(padx=20, pady=2)
    tk.Label(f, text=m + ":", width=18, anchor="w").pack(side=tk.LEFT)
    e = tk.Entry(f, bd=3, width=10)
    e.pack(side=tk.LEFT)
    entries.append(e)

