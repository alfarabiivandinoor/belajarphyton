# Membuat segitiga dengan perataan kiri-bawah
T = int(input("Masukan Angka : "))
for i in range (1, T+1):
	print(((T-i+1) * " ") + (i * "*"))
