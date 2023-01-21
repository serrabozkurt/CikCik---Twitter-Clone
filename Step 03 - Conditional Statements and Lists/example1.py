saat = 3

if 4 <= saat < 7:
    print("İyi sabahlar")
elif 7 <= saat < 11:
    print("Günaydın")
elif 11 <= saat < 17:
    print("İyi günler")
elif 17 <= saat < 21:
    print("İyi akşamlar")
# elif saat >= 21 or saat < 4:
# elif not 4 <= saat < 21:
else:
    print("İyi geceler")

if saat >= 21 or saat < 4:
    print("İyi geceler")
elif saat < 7:
    print("İyi sabahlar")
elif saat < 11:
    print("Günaydın")
elif saat < 17:
    print("İyi günler")
elif saat < 21:
    print("İyi akşamlar")