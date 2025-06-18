member = input("apakah pelanggan adalah member? [Ya/Tidak]").strip().lower()
jumlah_belanja = float(input("Masukan Jumlah Belanja Rp: "))

if member == "ya":
    if jumlah_belanja >= 500000:
        diskon = 0.2
    elif jumlah_belanja >= 200000:
        diskon = 0.1
    else:
        diskon = 0.05

else:
    if jumlah_belanja >= 500000:
        diskon = 0.1
    elif jumlah_belanja >= 200000:
        diskon = 0.05
    else:
        diskon = 0

total_diskon = jumlah_belanja * diskon 
total_harga = jumlah_belanja-total_diskon

print ("Rp",total_diskon)
print ("Rp",total_harga)
