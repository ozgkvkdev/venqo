# 1. ürün bilgileri
urun1={
    "id":1,
    "ad": "Oversize Tişört",
    "marka":"VENQO",
    "kategori": "Tişört",
    "beden": "L",
    "renk":"Siyah",
    "fiyat": 499,
    "stok":10,
    "indirim":True,
    "favori":True,
}


# 2. ürün bilgileri
urun2={
    "id":2,
    "ad": "Kargo Pantolon",
    "marka":"VENQO",
    "kategori": "Pantolon",
    "beden": "M",
    "renk":"Haki",
    "fiyat": 899,
    "stok":20,
    "indirim":False,
    "favori":True
}

#3.ürün bilgileri 

urun3={
    "id":3,
    "ad": "Kapüşonlu Hoodie",
    "marka":"VENQO",
    "kategori": "Sweatshirt",
    "beden": "XL",
    "renk":"Gri",
    "fiyat": 1099,
    "stok":12,
    "indirim":True,
    "favori":True,
}



# 4. ürün bilgileri
urun4={
    "id":4,
    "ad": "Eşofman Altı",
    "marka":"VENQO",
    "kategori": "Alt Giyim",
    "beden": "L",
    "renk":"Lacivert",
    "fiyat": 699,
    "stok":18,
    "indirim":False,
    "favori":False,
}


# ürünler listesi oluşturuldu
urunler = [
    urun1,
    urun2,
    urun3,
    urun4
]   


# urun1 stoğu güncellendi
urun1["stok"]=7       

# urun2 fiyatı güncellendi
urun2["fiyat"]=799
urunler[0]["stok"] = urunler[0]["stok"] - 1      

print(urunler[0]["ad"])     # liste üzerinde işlem yapma
print(urunler[3]["stok"])

print(urunler[1]["ad"])
print(urunler[3]["fiyat"])



# ==========================================
# STOK KONTROL SİSTEMİ
# ==========================================


if urun1["stok"] == 0 :
    print("Ürün stokta yok")

elif urun1["stok"] >=1 and urun1["stok"] <=5 :
    print("Son Ürünler ! Acele edin")

elif urun1["stok"] > 5 :
    print("Ürün Stokta Mevcut")

else:
    print("Maalesef ürün mevcut değil")



# ==========================================
# İNDİRİM KONTROL SİSTEMİ
# ==========================================


if urun1["indirim"]:
    print(f" {urun1['ad']} ürünü indirimde!")
else:
    print(f"{urun1['ad']} ürününde indirim bulunmuyor.")



# ==========================================
# FAVORİ KONTROL SİSTEMİ
# ==========================================


if urun1["favori"]:
    print(f"{urun1['ad']} favorilerinizde bulunuyor.")
else:
    print(f"{urun1['ad']} favorilerinizde bulunmuyor.")


# --------------------------------------
# Ücretsiz Kargo Sistemi
#---------------------------------------

if urun1["fiyat"] >= 1000 :
    print(f'{urun1["ad"]} Bu ürün ücretsiz kargo kampanyasına dahildir.')
elif urun1["fiyat"] >=700 and urun1["fiyat"] <=999:
    print(f'{urun1["ad"]} Bu ürün ücretsiz kargo kampanyasına dahildir.')
else:
    print(f'{urun1["ad"]} Bu ürün ücretsiz kargo kampanyasına dahil değildir.')



# VIP Kampanya Sistemi
#----------------------#

if urun1["indirim"] == True and urun1 ["fiyat"] >= 1000 :
    print(f"{urun1['ad']} hem indirimde hem ücretsiz kargolu!")
elif urun1["indirim"] == True and urun1["fiyat"] <1000 :
    print(f"{urun1['ad']} Tişört indirimde.")
elif urun1["indirim"] == False and urun1["fiyat"] >= 1000 :
    print(f"{urun1['ad']} ürün ücretsiz kargo kampanyasına dahildir.")
else:
    print(f"{urun1['ad']} Normal satış devam ediyor.")


   