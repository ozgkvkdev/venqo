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


for urun in urunler :
  print(urun["ad"])


for urun in urunler:
    print("------------------------")
    print(f"Ürün Adı : {urun['ad']}")
    print(f"Kategori : {urun['kategori']}")
    print(f"Fiyat    : {urun['fiyat']} TL")
    print(f"Favori   : {urun['favori']}")

# indirim hesaplama

for urun in urunler:
   if urun["indirim"]:
    print(f"ürün adı :{urun['ad']} indirim mevcut")
   else:
     print(f"Ürün adı: {urun['ad']} indirim mevcut değil.")


# adet hesaplama  

for urun in urunler:
  if urun["stok"] <=5:
    print(f"{urun['ad']} - {urun['stok']} adet kaldı.")
  else:
   print(f"{urun['ad']} - {urun['stok']} adet kaldı.")


# en pahalı ürünü bulma

en_pahali=urunler[0]
for urun in urunler:
  if urun["fiyat"] > en_pahali["fiyat"]:
    en_pahali=urun

print(en_pahali["ad"])
print(en_pahali["fiyat"])

# en ucuz ürünü bulma

en_ucuz=urunler[0]

for urun in urunler:
  if urun["fiyat"] < en_ucuz["fiyat"]:
    en_ucuz=urun

print(en_ucuz["ad"])
print(en_ucuz["fiyat"])


# indirim hesaplama 

indirim_sayisi=0
for urun in urunler:
  if urun["indirim"]:
    indirim_sayisi+=1

print(f"İndirimdeki ürün sayısı: {indirim_sayisi}")


# ürünlerin toplam  fiyatını bulma

toplam_fiyat=0

for urun in urunler:
  toplam_fiyat+=urun["fiyat"]

print("ürünlerin toplam fiyatı :" , toplam_fiyat)


# Stok değeri 10'dan büyük olan ürünlerin sayısını bul.

stok_degeri=0

for urun in urunler:
  if urun["stok"] > 10:
    stok_degeri+=1

print(f"dan fazla bulunan ürün sayısı : {stok_degeri}")


#----------------------------------------------

marka = input("Lütfen Bir Marka Giriniz: ")

for urun in urunler:
    if marka == urun["marka"]:
        print(urun["ad"])


urun_adi = input("Lütfen bir ürün adı giriniz: ")

bulundu = False

for urun in urunler:
    if urun_adi == urun["ad"]:
        bulundu = True
        print(" Ürün bulundu")
        print(f"Ürün Adı : {urun['ad']}")
        print(f"Kategori : {urun['kategori']}")
        print(f"Fiyat    : {urun['fiyat']} TL")
        print(f"Stok     : {urun['stok']}")

if bulundu == False:
    print(" Aradığınız ürün bulunamadı.")


min_fiyat=int(input("lütfen bir fiyat giriniz :"))

for urun in urunler:
   if urun["fiyat"] == min_fiyat:
      print(f"Ürün: {urun['ad']} - {urun['fiyat']} TL")
  