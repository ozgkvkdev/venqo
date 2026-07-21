
# VENQO ÜRÜN LİSTESİ


urunler = [
    {
        "id": 1,
        "ad": "Oversize Tişört",
        "marka": "VENQO",
        "kategori": "Tişört",
        "beden": "L",
        "renk": "Siyah",
        "fiyat": 499,
        "stok": 10,
        "indirim": True,
        "favori": True
    },
    {
        "id": 2,
        "ad": "Kargo Pantolon",
        "marka": "VENQO",
        "kategori": "Pantolon",
        "beden": "M",
        "renk": "Haki",
        "fiyat": 799,
        "stok": 20,
        "indirim": False,
        "favori": True
    },
    {
        "id": 3,
        "ad": "Kapüşonlu Hoodie",
        "marka": "VENQO",
        "kategori": "Sweatshirt",
        "beden": "XL",
        "renk": "Gri",
        "fiyat": 1099,
        "stok": 12,
        "indirim": True,
        "favori": True
    }
]


# TÜM ÜRÜN ADLARINI LİSTELE


print("\n--- Ürün Adları ---")

for urun in urunler:
    print(urun["ad"])



# ÜRÜN DETAYLARINI GÖSTER


print("\n--- Ürün Detayları ---")

for urun in urunler:
    print("----------------------------")
    print(f"Ürün Adı : {urun['ad']}")
    print(f"Kategori : {urun['kategori']}")
    print(f"Fiyat    : {urun['fiyat']} TL")
    print(f"Favori   : {urun['favori']}")



# İNDİRİM DURUMU


print("\n--- İndirim Durumu ---")

for urun in urunler:
    if urun["indirim"]:
        print(f"{urun['ad']} ürününde indirim var.")
    else:
        print(f"{urun['ad']} ürününde indirim yok.")



# STOK DURUMU


print("\n--- Stok Durumu ---")

for urun in urunler:
    if urun["stok"] <= 5:
        print(f"{urun['ad']} - Son {urun['stok']} ürün kaldı.")
    else:
        print(f"{urun['ad']} - Stok: {urun['stok']}")



# EN PAHALI ÜRÜN


en_pahali = urunler[0]

for urun in urunler:
    if urun["fiyat"] > en_pahali["fiyat"]:
        en_pahali = urun

print("\n--- En Pahalı Ürün ---")
print(en_pahali["ad"])
print(en_pahali["fiyat"])



# EN UCUZ ÜRÜN


en_ucuz = urunler[0]

for urun in urunler:
    if urun["fiyat"] < en_ucuz["fiyat"]:
        en_ucuz = urun

print("\n--- En Ucuz Ürün ---")
print(en_ucuz["ad"])
print(en_ucuz["fiyat"])



# İNDİRİMDEKİ ÜRÜN SAYISI


indirim_sayisi = 0

for urun in urunler:
    if urun["indirim"]:
        indirim_sayisi += 1

print(f"\nİndirimdeki ürün sayısı: {indirim_sayisi}")



# TOPLAM ÜRÜN FİYATI


toplam_fiyat = 0

for urun in urunler:
    toplam_fiyat += urun["fiyat"]

print(f"\nToplam ürün fiyatı: {toplam_fiyat} TL")


# STOKU 10'DAN FAZLA OLAN ÜRÜNLER

stok_sayisi = 0

for urun in urunler:
    if urun["stok"] > 10:
        stok_sayisi += 1

print(f"\nStoku 10'dan fazla olan ürün sayısı: {stok_sayisi}")



# MARKAYA GÖRE ÜRÜN LİSTELEME

marka = input("\nMarka giriniz: ")

for urun in urunler:
    if marka == urun["marka"]:
        print(urun["ad"])



# ÜRÜN ARAMA


urun_adi = input("\nÜrün adını giriniz: ")

bulundu = False

for urun in urunler:
    if urun_adi == urun["ad"]:
        bulundu = True
        print("\nÜrün bulundu.")
        print(f"Ürün Adı : {urun['ad']}")
        print(f"Kategori : {urun['kategori']}")
        print(f"Fiyat    : {urun['fiyat']} TL")
        print(f"Stok     : {urun['stok']}")

if not bulundu:
    print("Aradığınız ürün bulunamadı.")



# MİNİMUM FİYATA GÖRE FİLTRELEME


min_fiyat = int(input("\nMinimum fiyat giriniz: "))

for urun in urunler:
    if urun["fiyat"] >= min_fiyat:
        print(f"{urun['ad']} - {urun['fiyat']} TL")
