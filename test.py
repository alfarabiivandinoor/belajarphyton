# # Membuat segitiga dengan perataan kiri-bawah
# T = int(input("Masukan Angka : "))
# for i in range (1, T+1):
# 	print(i * "*")

# # Membuat segitiga dengan perataan kiri-atas
# T = int(input("Masukan Angka : "))
# for i in range (1, T+1):
# 	print((T-i+1) * "*")

# Membuat segitiga dengan perataan kanan-bawah
# T = int(input("Masukan Angka : "))
# for i in range (1, T+1):
# 	print(((T-i+1) * " ") + (i * "*"))

# # Membuat segitga dengan perataan kanan-atas
# T = int(input("Masukan Angka : "))
# for i in range (1, T+1):
# 	print((i * " ") + ((T-i+1) * "*"))

# Membuat piramida
T = int(input("Masukan Angka : "))
for i in range (1, T+1):
    print ((T-i+1) * " " + ("*" * ((i*2)-1)))