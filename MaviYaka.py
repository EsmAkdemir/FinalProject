from Calisan import Calisan
class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas)
        self.__yipranma_payi = yipranma_payi

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):# Zam hesaplama yöntemi
        try:
            if self.get_tecrube() >= 2 and self.get_tecrube() <= 4 and self.get_maas() < 15000:
                # Eğer çalışanın tecrübesi 2 ile 4 yıl arasında ve maaşı 15000 TL'den düşükse
                # Zam oranı, maaşın tecrübeye bölümünden kalanının yarısıyla yıpranma payının 10 katı arasındadır
                zam_orani = (self.get_maas() % self.get_tecrube()) / 2 + (self.get_yipranma_payi() * 10)
                # Zam miktarı, zam oranının maaşın yüzdesiyle çarpılarak hesaplanır
                self.set_yeni_maas(self.get_maas() + (zam_orani * self.get_maas() / 100))
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                # Eğer çalışanın tecrübesi 4 yıldan fazla ve maaşı 25000 TL'den düşükse
                # Zam oranı, maaşın tecrübeye bölümünden kalanının üçte biriyle yıpranma payının 10 katı arasındadır
                zam_orani = (self.get_maas() % self.get_tecrube()) / 3 + (self.get_yipranma_payi() * 10)
                # Zam miktarı, zam oranının maaşın yüzdesiyle çarpılarak hesaplanır
                self.set_yeni_maas(self.get_maas() + (zam_orani * self.get_maas() / 100))
            else:
                # Diğer durumlarda sadece yıpranma payının 10 katı zam yapılır
                zam_orani = (self.get_yipranma_payi() * 10)
                # Zam miktarı, zam oranının maaşın yüzdesiyle çarpılarak hesaplanır
                self.set_yeni_maas(self.get_maas() + (zam_orani * self.get_maas() / 100))

        # Hata durumunda gerekli işlemler yapılır
        except ZeroDivisionError as e:
            print("Hata: Sıfıra bölme hatası - Tecrübe değeri sıfır olamaz.")

    def __str__(self):
        # Zam hakki() yöntemi çağrılır
        self.zam_hakki()
        # Üst sınıfın __str__() yöntemi çağrılır. Çalışan bilgileri ve yıpranma payı bilgisi birleştirilerek döndürülür
        return f"{super().__str__()}, Yıpranma Payı: {self.get_yipranma_payi()}"
