# Modal awal
modal_awal = 100_000_000

# Inisialisasi list untuk menyimpan laba setiap bulan
laba_per_bulan = []

# Menghitung laba setiap bulan
for bulan in range(1, 9):
    if bulan == 1 or bulan == 2:
        laba_bulan = 0  # Belum mendapatkan laba pada bulan 1 dan 2
    elif bulan == 3:
        laba_bulan = modal_awal * 0.01  # Laba 1% pada bulan 3
    elif bulan == 4:
        laba_bulan = laba_per_bulan[2]  # Laba tetap sama dengan bulan 3
    elif bulan == 5:
        laba_bulan = laba_per_bulan[2] * 1.05  # Laba meningkat 5% dari bulan 3
    elif bulan == 6:
        laba_bulan = laba_per_bulan[4]  # Laba tetap sama dengan bulan 5
    elif bulan == 7:
        laba_bulan = laba_per_bulan[4]  # Laba tetap sama dengan bulan 5
    elif bulan == 8:
        laba_bulan = laba_per_bulan[4] * 0.03  # Laba menjadi 3% dari bulan 5

    laba_per_bulan.append(laba_bulan)

# Menghitung total laba
total_laba = sum(laba_per_bulan)

# Menampilkan hasil
for i in range(8):
    print(f"Laba bulan ke-{i + 1} sebesar: {laba_per_bulan[i]:,.2f}")

print(f"Total laba adalah: {total_laba:,.2f}")
