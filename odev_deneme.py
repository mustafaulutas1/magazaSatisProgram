class Magaza:
    def __init__(self, magaza_adi, satici_adi, satici_cinsi):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.__satis_tutari = 0
        
    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi
        
    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi
        
    def set_satici_cinsi(self, satici_cinsi):
        self.__satici_cinsi = satici_cinsi
        
    def get_magaza_adi(self):
        return self.__magaza_adi
        
    def get_satici_adi(self):
        return self.__satici_adi
        
    def get_satici_cinsi(self):
        return self.__satici_cinsi
        
    def satis_yap(self, satis_tutari):
        self.__satis_tutari += satis_tutari
        
    def magaza_satis_tutari(self):
        return self.__satis_tutari
     
def main():
    magazalar = {}
    
    while True:
        magaza_adi = input("Mağaza adi(Çikis icin enter): ")
        if magaza_adi == "":
            break
            
        satici_adi = input("Satici adi: ")
        satici_cinsi = input("Satici cinsi (tv, bilgisayar, beyaz eşya, diğer): ")
        satis_tutari = float(input("Satiş tutari: "))
        
        if magaza_adi not in magazalar:
            magazalar[magaza_adi] = []
        
        magazalar[magaza_adi].append(Magaza(magaza_adi, satici_adi, satici_cinsi))
        magazalar[magaza_adi][-1].satis_yap(satis_tutari)
        
    for magaza_adi in magazalar:
        print(magaza_adi)
        toplam_magaza_satis_tutari = 0
        
        for magaza in magazalar[magaza_adi]:
            toplam_satici_satis_tutari = magaza.magaza_satis_tutari()
            toplam_magaza_satis_tutari += toplam_satici_satis_tutari
            
            print(f"\t{magaza.get_satici_adi()} ({magaza.get_satici_cinsi()}): {toplam_satici_satis_tutari:.2f}")
            
        print(f"{magaza_adi} Magazasi Toplam Satis: {toplam_magaza_satis_tutari:.2f}")
        
        saticilar = {}
        for magaza in magazalar[magaza_adi]:
            if magaza.get_satici_adi() not in saticilar:
                saticilar[magaza.get_satici_adi()] = 0
            saticilar[magaza.get_satici_adi()] += magaza.magaza_satis_tutari()
        
        for satici in saticilar:
            print(f"\t{satici} Toplam Satis: {saticilar[satici]:.2f}")
            print("***********************************")
main()