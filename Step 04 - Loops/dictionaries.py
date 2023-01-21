sozluk = {"mutlu": "happy", "üzgün": "sad", "heyecanlı": "excited"}
print(sozluk)

print(sozluk["mutlu"])

print("heyecanlı" in sozluk)
print("öfkeli" in sozluk)
print("happy" in sozluk)

for kelime in sozluk:
    print(kelime, " > ", sozluk[kelime])