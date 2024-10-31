# Inisialisasi variabel untuk menyimpan bilangan terbesar
max_number = None

print("Masukkan angka (masukkan 0 untuk berhenti):")

while True:
    # Mengambil input dari pengguna
    number = int(input("Masukkan bilangan: "))
    
    # Memeriksa apakah pengguna memasukkan 0
    if number == 0:
        break
    
    # Memperbarui bilangan terbesar jika diperlukan
    if max_number is None or number > max_number:
        max_number = number

# Menampilkan bilangan terbesar
if max_number is not None:
    print("Bilangan terbesar adalah:", max_number)
else:
    print("Tidak ada angka yang dimasukkan.")
