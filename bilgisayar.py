def bilgisayar_topla(marka, *ozellikler):
    print(f"Aşağıdaki özelliklerle {marka} bilgisayar oluşturuldu")
    for ozellik in ozellikler:
        print(ozellik)

def bilgisayar_sil(marka):
    print(f"{marka} bilgisayar silindi")