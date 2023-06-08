from Insan import Insan
class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas):

        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)

        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas
        self.__yeni_maas = yeni_maas

    def get_sektor(self):
        return self.__sektor
    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube
    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas
    def set_maas(self, maas):
        self.__maas = maas

    def get_yeni_maas(self):
        return self.__yeni_maas
    def set_yeni_maas(self, yeni_maas):
        self.__yeni_maas = yeni_maas

    def zam_hakki(self):#zam hesaplama

        try:
            yeni_maas = 0
            # Tecrübe 2-4 aralığındaysa ve maaş 15000'den küçükse
            if self.__tecrube >= 2 and self.__tecrube <= 4 and self.__maas < 15000:
                #zam oranını hesaplar
                zam_orani = self.__maas % self.__tecrube
                # Yeni maaşı günceller
                self.__yeni_maas += (zam_orani * self.__maas / 100) + self.__maas
            # Tecrübe 4'ten büyükse ve maaş 25000'den küçükse
            elif self.__tecrube > 4 and self.__maas < 25000:
                # Zam oranını hesaplar
                zam_orani = (self.__maas % self.__tecrube) / 2
                # Yeni maaşı günceller
                self.__yeni_maas += (zam_orani * self.__maas / 100) + self.__maas
            else:
                # Diğer durumlarda zam oranını sıfıra eşitler
                zam_orani = 0
                # Yeni maaşı mevcut maaş değeriyle eşitler
                self.__yeni_maas = self.__maas

        # Hata durumunda gerekli işlemler yapılır
        except Exception as e:
            print("Hata oluştu:", str(e))

    def __str__(self):
        # Zam hakki() yöntemi çağrılır
        self.zam_hakki()
        # Üst sınıfın __str__() yöntemini çağırır. İnsan bilgileri ve calisan bilgilerini birleştirerek sonucu döndürür
        return f"{super().__str__()}, Tecrübe: {self.__tecrube}, Yeni Maaş: {self.__yeni_maas}"