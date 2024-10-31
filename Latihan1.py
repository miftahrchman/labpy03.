from random import random

# Meminta input dari pengguna untuk jumlah bilangan acak
n = int(input("Masukkan jumlah bilangan acak yang ingin ditampilkan: "))

# Inisialisasi variabel untuk menghitung jumlah bilangan yang telah ditampilkan
count = 0

# Menggunakan while untuk terus menghasilkan bilangan acak sampai mencapai n
while count < n:
    # Menghasilkan bilangan acak
    a = random()
    
    # Memeriksa apakah bilangan acak kurang dari 0.5
    if a < 0.5:
        count += 1  # Menambah hitungan bilangan yang ditampilkan
        print(f"Data ke : {count} => {a}")  # Menampilkan bilangan acak dengan format yang diinginkan

# Menampilkan tulisan "Selesai" setelah semua bilangan ditampilkan
print("Selesai")
