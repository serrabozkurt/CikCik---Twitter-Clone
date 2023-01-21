kilo = 80
erkek = True

if kilo > 80:
    print("Spor yapmaya ne dersin?")
elif kilo < 50:
    print("Biraz kilo alsan fena olmaz")
else:
    print("Gayet sağlıklısın")


if 50 < kilo <= 80:
    print("Gayet sağlıklısın")
else:
    print("Kilona dikkat etmelisin")


if erkek and kilo > 80:
    print("Spor yapmaya ne dersin?")
elif erkek and kilo < 50:
    print("Biraz kilo alsan fena olmaz")
elif not erkek and kilo > 70:
    print("Spor yapmaya ne dersin?")
elif not erkek and kilo < 40:
    print("Biraz kilo alsan fena olmaz")
else:
    print("Gayet sağlıklısın")