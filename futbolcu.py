def futbolcu_olustur(isim, *ozellikler):
    print(f"Aşağıdaki özelliklerle {isim} futbolcu oluşturuldu")
    for ozellik in ozellikler:
        print(ozellik)

def futbolcu_sil(isim):
    print(f"{isim} futbolcu silindi")