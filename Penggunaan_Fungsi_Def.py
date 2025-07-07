def garis ():
    print ("=================================")

def main_menu():
    print ("Selamat Datang Di Menu Penilaian")
    nama = str(input("Silakan Masukan Nama Anda : "))
    matkul = str(input("Silakan Masukan Mata Kuliah : "))
    return nama , matkul

def fuction(nama, matkul):
    nilai = float(input("Masukan Nilai ujian: "))
    print("___________________________________________________________________")
    if nilai >= 80:
        print (f"Selamat!!! {nama}, Anda Lulus '{matkul}' dengan predikat A")
    elif nilai >= 70:
        print (f"Selamat!!! {nama}, Anda Lulus '{matkul}' dengan predikat B")
    elif nilai >= 60:
        print (f"Selamat!!! {nama}, Anda Lulus '{matkul}' dengan predikat C")
    else:
        print (f"Maaf {nama}, kamu harus mengulang '{matkul}', silakan hubungi dosen terkait")
    print("___________________________________________________________________")
    print("Terimakasih telah mengikuti ujian")

garis()
nama, matkul = main_menu()
garis()
fuction(nama, matkul)
