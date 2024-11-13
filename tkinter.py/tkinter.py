import tkinter as tk

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    label_hasil.config(text="Prodi Pilihan: Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

# Label judul
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
label_judul.grid(row=0, column=0, columnspan=2, pady=10)

# Input nilai mata pelajaran
labels = []
entries = []
for i in range(10):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:")
    label.grid(row=i+1, column=0, sticky="w", padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i+1, column=1, padx=10, pady=5)
    labels.append(label)
    entries.append(entry)

# Tombol hasil prediksi
button_prediksi = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
button_prediksi.grid(row=11, column=0, columnspan=2, pady=10)

# Label luaran hasil prediksi
label_hasil = tk.Label(root, text="", font=("Arial", 12))
label_hasil.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()