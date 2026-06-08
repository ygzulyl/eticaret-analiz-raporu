class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.km = 0

    def bilgileri_goster(self):
        uzun_format = f"{self.marka} {self.model} {self.yil} ({self.km} km)"
        return uzun_format
    
    def km_guncelle(self, km):
        if km >= self.km:
            self.km = km
        else:
            print("Hata: Kilometre geri alınamaz.")

    def km_ekle(self, km):
        if km > 0:
            self.km += km
        else:
            print("Hata: Eklenen kilometre pozitif olmalıdır.")

    def benzin_doldur(self, litre):
        print(f"{litre} litre benzin dolduruldu.")

class Batarya:
    def __init__(self, kapasite_kwh):
        self.kapasite_kwh = kapasite_kwh

    def bilgileri_goster(self):
        print(f"Batarya kapasitesi: {self.kapasite_kwh} kwh")

def mesafe_hesapla(self):
    if self.kapasite_kwh == 75:
        mesafe = 350
        print(f"Bu batarya ile tahmini menzil: {mesafe} kwh")
    elif self.kapasite_kwh == 100:
        mesafe = 500
        print(f"Bu batarya ile tahmini menzil: {mesafe} kwh")
    else:
        mesafe = "Bilinmeyen batarya kapasitesi"
        print(mesafe)

class ElektrikliAraba(Araba):
    def __init__(self, marka, model, yil, batarya_kapasitesi):
        super().__init__(marka, model, yil)
        self.batarya = Batarya(batarya_kapasitesi)

    def benzin_doldur(self, litre):
        print("Hata: Elektrikli araba benzin doldurmaz.")