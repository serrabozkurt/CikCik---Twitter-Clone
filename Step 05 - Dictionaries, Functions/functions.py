def yas(dogum_yili):
    return 2018 - dogum_yili

print(yas(1990))

print("merhaba")
yas(1995)


yil3 = 1881
hesap = yas(yil3)

print(hesap)

print(hesap)


def kdv_dahil(fiyat, kdv_orani=0.18, kur=1, para_birimi="₺"):
    return fiyat + fiyat * kdv_orani
    # return komutundan sonraki hiçbir kod çalıştırılmaz!
    print(fiyat, para_birimi)

print(kdv_dahil(100, 0.08, 5.7))
print(kdv_dahil(83, kur=5.7))


def urun_aciklama(**sozluk):
    for ozellik in sozluk:
        print(ozellik, ":", sozluk[ozellik])

urun_aciklama(ram="16 GB", disk="1 TB")
urun_aciklama(beden="L")
urun_aciklama(tus_sayisi=120, tus_dizilimi="Türkçe Q")

ozellik = {
    "silindir": 4,
    "motor_hacmi": 2000
}

urun_aciklama(**ozellik, uretim_yili=2018)

fiyat_bilgisi = {
    "kdv_orani": 0.08,
    "kur": 3,
    "fiyat": 20
}

print(kdv_dahil(**fiyat_bilgisi))
