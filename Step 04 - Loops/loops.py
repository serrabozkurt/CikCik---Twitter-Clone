for tekrar in range(3):
    print("Merhaba")

print([1,2,3])
print(range(3))

for sayi in range(1, 11, 2):
    print(sayi)

print("Geri sayım başladı")
for sayi in range(10, 0, -1):
    print(sayi)

yemekler = ["Mantı", "Ekşi Köfte", "Menemen", "Lazanya", "Nohut"]
for yemek in yemekler:
    print(yemek)

print("Döngü ile ilgili sorular:")
sorular = ["Hiç veri olmadığında ne olacak?"]
# sorular = []
if len(sorular) > 0:
    for soru in sorular:
        print(soru)
else:
    print("Hiç soru yok :)")


for soru in sorular:
    print(soru)
else:
    if len(sorular) == 0:
        print("Hiç soru yok :)")

sayi = 3
while sayi < 5:
    print("Küçük")
    sayi += 0.5

print("Program bitti")