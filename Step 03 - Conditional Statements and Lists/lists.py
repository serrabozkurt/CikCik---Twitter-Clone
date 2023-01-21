renkler = ["Kırmızı", "Siyah", "Yeşil", "Mor", "Mavi", "Beyaz",
           "Kahverengi", "Turuncu", "Gri", "Mavi", "Turuncu"]

print(renkler)
print(renkler[3])

renkler[0] = "Yeşil"

print(renkler)

renkler.append("Kırmızı")
print(renkler)

# listeyi boşaltır
# renkler.clear()
# print(renkler)

turuncular = renkler.count("Turuncu")
print(turuncular)
pembeler = renkler.count("Pembe")
print(pembeler)

# İndis hatası verir
# print(renkler[12])

indis = renkler.index("Kahverengi")
print(indis)

print(renkler)
mavi_indis1 = renkler.index("Mavi")
mavi_indis2 = renkler.index("Mavi", mavi_indis1+1)
print(mavi_indis1, mavi_indis2)

renkler.insert(7, "Sarı")
print(renkler)

renkler.pop(2)
print(renkler)

renkler.remove("Mavi")
print(renkler)

renkler.reverse()
print(renkler)

renkler.sort()
print(renkler)

print(renkler[-2])

print(renkler[1:4])