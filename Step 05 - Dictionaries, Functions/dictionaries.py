ceviri = {"mutlu": "happy", "üzgün": "sad", "heyecanlı": "excited"}

print(ceviri)

print(ceviri["mutlu"])

# olmayan anahtar kelime KeyError verir
# print(ceviri["öfkeli"])

print("mutlu" in ceviri)

print("öfkeli" in ceviri)

# aramayı sadece anahtar kelimelerde yapar
print("happy" in ceviri)

for kelime in ceviri:
    print(kelime, ":", ceviri[kelime])

print(ceviri.get("mutlu"))

# anahtar kelime sözlükte yoksa None değeri oluşur.
print(ceviri.get("öfkeli"))

print(ceviri.pop("üzgün"))

print(ceviri)

ceviri["yorgun"] = "tired"

print(ceviri)

print(ceviri.keys())

print(ceviri.values())

print("happy" in ceviri.values())

print(ceviri.items())

ceviri.update({"hasta": "ill"})
print(ceviri)

ceviri.update({"korkmuş": "terrified", "yorgun": "exhausted"})
print(ceviri)

print(ceviri.setdefault("sinirli", "angry"))
print(ceviri)
print(ceviri.setdefault("sinirli", "furious"))
