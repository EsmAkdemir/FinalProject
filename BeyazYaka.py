from Calisan import Calisan
class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas,yeni_maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas)
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi
    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):# Zam hesaplama yöntemi
        try:
            if self.get_tecrube() >= 2 and self.get_tecrube() <= 4 and self.get_maas() < 15000:
                # Eğer çalışanın tecrübesi 2 ile 4 yıl arasında ve maaşı 15000 TL'den düşükse
                # Zam miktarı, maaşın tecrübeye bölümünden kalanıyla 5 çarpılır ve teşvik primi eklenir
                zam_miktari = (self.get_maas() % self.get_tecrube()) * 5 + float(self.get_tesvik_primi())
                # Yeni maaş hesaplanır ve ayarlanır
                self.set_yeni_maas(self.get_maas() + zam_miktari)
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                # Eğer çalışanın tecrübesi 4 yıldan fazla ve maaşı 25000 TL'den düşükse
                # Zam miktarı, maaşın tecrübeye bölümünden kalanıyla 4 çarpılır ve teşvik primi eklenir
                zam_miktari = (self.get_maas() % self.get_tecrube()) * 4 + float(self.get_tesvik_primi())
                # Yeni maaş hesaplanır ve ayarlanır
                self.set_yeni_maas(self.get_maas() + zam_miktari)
            else:
                # Diğer durumlarda sadece teşvik primi maaşa eklenir
                zam_miktari = float(self.get_tesvik_primi())
                # Yeni maaş hesaplanır ve ayarlanır
                self.set_yeni_maas(self.get_maas() + zam_miktari)

        # Hata durumunda gerekli işlemler yapılır
        except ZeroDivisionError as e:
            print("Hata: Sıfıra bölme hatası - Tecrübe değeri sıfır olamaz.")

    def __str__(self):
        # Zam hakki() yöntemi çağırılarak zam hesaplaması yapılır
        self.zam_hakki()
        # Üst sınıfın __str__() yöntemi çağırılır. Calisan bilgileri ve teşvik bilgisi birleştirilerek döndürülür
        return f"{super().__str__()}, Teşvik Prim: {self.get_tesvik_primi()}"

