print ("====Program Konversi Suhu===")

celcius = float(input("Masukkan Suhu dalam Celcius : "))

reamur = (4/5) *celcius
farenheit = (9/5) *celcius +32
kelvin = 273.15 + celcius

print (f"Suhu dalam Reamur = {reamur:2f}°R")
print (f"Suhu dalam Farenheit = {farenheit:2f}°F")
print (f"Suhu dalam Kelvin = {kelvin:2f}°K")

print ("Proses Selesai.")
