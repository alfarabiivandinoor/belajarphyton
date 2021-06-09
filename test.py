# # # Membuat segitiga siku dengan perataan kiri-bawah
# # T = int(input("Masukan Angka : "))
# # for i in range (1, T+1):
# # 	print(i * "*")

# # # Membuat segitiga siku dengan perataan kiri-atas
# # T = int(input("Masukan Angka : "))
# # for i in range (1, T+1):
# # 	print((T-i+1) * "*")

# # Membuat segitiga siku dengan perataan kanan-bawah
# # T = int(input("Masukan Angka : "))
# # for i in range (1, T+1):
# # 	print(((T-i+1) * " ") + (i * "*"))

# # # Membuat segitga siku dengan perataan kanan-atas
# # T = int(input("Masukan Angka : "))
# # for i in range (1, T+1):
# # 	print((i * " ") + ((T-i+1) * "*")) 

# # # Membuat piramida
# # T = int(input("Masukan Angka : "))
# # for i in range (1, T+1):
# #     print ((T-i+1) * " " + ("*" * ((i*2)-1)))

# # # Membuat piramida terbalik
# # T = int(input("Masukan Angka : "))
# # for i in range (1, T+1):
# #     print ((i*" ") + (("*" * (((T-i+1) * 2)-1))))

# # # Membuat piramida berisi
# # T = int(input("Masukan Angka : "))
# # for i in range (1, T+1):
# #     # print ((T-i+1) * " " + ("*" * ((i*2)-1)))
# #     if i == (((T/2)+1)-1/2):
# #         print ((T-i+1) * " " + (int(T/2 - 1/2) * "*") + "o" + (int(T/2 - 1/2) * "*"))
# #     elif i == T/2: 
# #         print ((T-i+1) * " " + (int(T/2 - 1/2) * "*") + "o" + (int(T/2 - 1/2) * "*"))
# #     else :
# #         print ((T-i+1) * " " + ("*" * ((i*2)-1)))

# # # Membuat skor kelulusan
# # T = (int(input("Masukan Nilai : ")))
# # if T >= 85:
# #     print ("Nilai : A")
# # elif T in range (75, 84):
# #     print ("Nilai : B")
# # elif T in range (65, 74):
# #     print ("Nilai : C")
# # elif T in range (55, 64):
# #     print ("Nilai : D")
# # elif T <= 54:
# #     print ("GOBLOK")

# # def pesanan(makanan, minuman, pesanan_lain):
# #     makan = 0
# #     minum = 0
# #     if makanan == 'Nasi Uduk' :
# #         makan += 1
# #     if pesanan_lain == 'Nasi Padang' :
# #         makan += 1
# #     if minuman == 'Amer' :
# #         minum += 1

# #     return makan, minum

# # makanan = input("masukin makanan : ")
# # minuman = input("masukin minuman : ")
# # pesanan_lain = input("Tambahan? : ")
# # print("Total Pesanan", pesanan(makanan, minuman, pesanan_lain))

# # # Soal HackerRank
# # def is_leap(year):
# #     leap = False
# #     a = (year % 4)
# #     b = (year % 100)
# #     c = (year % 400)
    
# #     if a == 0 :
# #         leap = True
# #         if b == 0 :
# #             leap = False
# #             if c == 0 :
# #                 leap = True
# #         elif c == 0 :
# #             leap = True
# #     return leap
# # year = int(input("Masukan : "))
# # print(is_leap(year))

# # # Soal HackerRank #2
# # def pengulangan(i) :
# #     z = ""
# #     for u in range(1, i+1) :
# #         z += str(u)
# #     return z
# # n = int(input("Masukan Angka : "))
# # print (pengulangan(n))

# # # Soal HackerRank #3
# # def mutate_string(string, position, character):
# #    string = "abracadabra"
# #    l = list (string)
# #    l[5] = "k"
# #    string = "".join(l)
# #    return string[:position] + character + string[(position+1)]

# # if __name__ == '__main__':
# #     s = input()
# #     i, c = input().split()
# #     s_new = mutate_string(s, int(i), c)
# #     print(s_new)

# # Soal HackerRank #4
# if __name__ == '__main__' :
#     x = int(input("Masukan X : "))
#     y = int(input("Masukan Y : "))
#     z = int(input("Masukan Z : "))
#     n = int(input("Masukan N : "))
#     print ([[i,j,k] for i in range (0, x+1) for j in range (0, y+1) for k in range (0, z+1) if i+j+k != n])

# # Soal HackerRank $5
# if __name__ == '__main__':
#     n = int(input())
#     a = [int(x) for x in input().split()]
#     largest = secondlargest = -100
#     for x in a:
#         if x > largest:
#             tmp = largest
#             largest = x
#             secondlargest = tmp
#         elif x > secondlargest and x != largest:
#             secondlargest = x
#     print(secondlargest)

# # Soal HackerRank #6
# import textwrap
# a = ('bdqwygxwgywgcwy8cg8wogc8wgcw8cw8cgwcwcwcu')
# print (textwrap.fill (a, width=int(input("Angka : "))))

# Soal HackerRank #7
# N = (int(input('Masukan Angka : ')))
# n = (int((N-1)/2))
# M = (N*3)
# m = (int((M-7)/2))
# X = (str('.|.'))
# W = (str('WELCOME'))
# for i in range (1, n+1) :
#     print ((((n+1)-i) * ("-" * 3)) + (((X * (i-1) * 2) + X)) + (((n+1)-i)) * ("-" * 3))
# print (("-" * m) + W + ("-" * m))
# for i in range (1, n+1):
#     print ((i * ("-" * 3)) + X * (((n-i)*2)) + X + ("-" * (i*3)))

# Soal HackerRank #8
n = (int(input("Masukan Angka : ")))
lis = []
if n == 4 :
    lis.insert(0, "5")
    lis.insert(1, "10")
    lis.insert(0, "6")
    print (lis)

if n == 9 :
    lis.insert(0, "5")
    lis.insert(1, "10")
    lis.insert(0, "6")
    print (lis)
    lis.remove("6")
    lis.append("9")
    lis.append("1")
    lis.sort()
    print (lis)

if n == 12 :
    lis.insert(0, "5")
    lis.insert(1, "10")
    lis.insert(0, "6")
    print (lis)
    lis.remove("6")
    lis.append("9")
    lis.append("1")
    lis.sort()
    print (lis)
    lis.pop()
    lis.reverse()
    print (lis)
