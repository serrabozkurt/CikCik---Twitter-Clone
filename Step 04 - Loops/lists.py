yemekler = ["Makarna", "Ekşili Köfte", "İskender", "Mantı", "Nohut", "Dolma",
            "Menemen", "Mantı", "Lazanya"]


print(yemekler)
print(yemekler[1])
print(yemekler[-1])

print(yemekler[3:5])

print(yemekler[:5])

print(yemekler[4:])

print(yemekler[-3:])

print(yemekler[:-2])

print(yemekler[-5:-3])


yoklama = ("Hasan", "Berkay", "Serra", "Betül", "Muhammet S.", "Muhammet",
          "Arslan", "Erkut", "Gözde", "Halil", "Emre")

print(yoklama)
print(yoklama[1])
print(yoklama[-2])
print(yoklama[1:3])

# Atama yaparak veri değiştirilemez
# yoklama[5] = "Muhammet Ş."
# print(yoklama)

print(yoklama.index("Hasan"))
print(yoklama.count("Arslan"))

# Boş tüp yok
ogretmen = ("Onur",)
print(ogretmen)

print(yemekler)
print(set(yemekler))

renkler = {"Mavi", "Kırmızı", "Yeşil", "Beyaz", "Yeşil"}
print(renkler)

print("Balık" in yemekler)
print("Menemen" in yemekler)
print("Salata" not in yemekler)
