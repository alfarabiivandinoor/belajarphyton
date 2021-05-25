# # Membuat segitiga siku dengan perataan kiri-bawah
# T = int(input("Masukan Angka : "))
# for i in range (1, T+1):
# 	print(i * "*")

# # Membuat segitiga siku dengan perataan kiri-atas
# T = int(input("Masukan Angka : "))
# for i in range (1, T+1):
# 	print((T-i+1) * "*")

# Membuat segitiga siku dengan perataan kanan-bawah
# T = int(input("Masukan Angka : "))
# for i in range (1, T+1):
# 	print(((T-i+1) * " ") + (i * "*"))

# # Membuat segitga siku dengan perataan kanan-atas
# T = int(input("Masukan Angka : "))
# for i in range (1, T+1):
# 	print((i * " ") + ((T-i+1) * "*")) 

# # Membuat piramida
# T = int(input("Masukan Angka : "))
# for i in range (1, T+1):
#     print ((T-i+1) * " " + ("*" * ((i*2)-1)))

# # Membuat piramida terbalik
# T = int(input("Masukan Angka : "))
# for i in range (1, T+1):
#     print ((i*" ") + (("*" * (((T-i+1) * 2)-1))))

# # Membuat piramida berisi
# T = int(input("Masukan Angka : "))
# for i in range (1, T+1):
#     # print ((T-i+1) * " " + ("*" * ((i*2)-1)))
#     if i == (((T/2)+1)-1/2):
#         print ((T-i+1) * " " + (int(T/2 - 1/2) * "*") + "o" + (int(T/2 - 1/2) * "*"))
#     elif i == T/2: 
#         print ((T-i+1) * " " + (int(T/2 - 1/2) * "*") + "o" + (int(T/2 - 1/2) * "*"))
#     else :
#         print ((T-i+1) * " " + ("*" * ((i*2)-1)))

# # Membuat skor kelulusan
# T = (int(input("Masukan Nilai : ")))
# if T >= 85:
#     print ("Nilai : A")
# elif T in range (75, 84):
#     print ("Nilai : B")
# elif T in range (65, 74):
#     print ("Nilai : C")
# elif T in range (55, 64):
#     print ("Nilai : D")
# elif T <= 54:
#     print ("GOBLOK")

# def pesanan(makanan, minuman, pesanan_lain):
#     makan = 0
#     minum = 0
#     if makanan == 'Nasi Uduk' :
#         makan += 1
#     if pesanan_lain == 'Nasi Padang' :
#         makan += 1
#     if minuman == 'Amer' :
#         minum += 1

#     return makan, minum

# makanan = input("masukin makanan : ")
# minuman = input("masukin minuman : ")
# pesanan_lain = input("Tambahan? : ")
# print("Total Pesanan", pesanan(makanan, minuman, pesanan_lain))

# # Soal HackerRank
# def is_leap(year):
#     leap = False
#     a = (year % 4)
#     b = (year % 100)
#     c = (year % 400)
    
#     if a == 0 :
#         leap = True
#         if b == 0 :
#             leap = False
#             if c == 0 :
#                 leap = True
#         elif c == 0 :
#             leap = True
#     return leap
# year = int(input("Masukan : "))
# print(is_leap(year))

# # Soal HackerRank #2
# def pengulangan(i) :
#     z = ""
#     for u in range(1, i+1) :
#         z += str(u)
        
#     return z
# n = int(input("Masukan Angka : "))
# print (pengulangan(n))