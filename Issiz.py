from Insan import Insan
class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube = tecrube

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def statu_bul(self):
        # Her bir statüye etkisi tanımlanmış bir etkiler sözlüğü oluşturuluyor
        etkiler = {
            "mavi yaka": 0.2,
            "beyaz yaka": 0.35,
            "yönetici": 0.45
        }
        # En yüksek etkiye sahip olan statünün başlangıçta değerleri atanıyor
        maks_etki = 0
        en_uygun_statu = ""

        # Tecrübe sözlüğündeki her bir statü ve yıl çifti üzerinde döngüye giriliyor
        for statu, yil in self.__tecrube.items():
            try:
                # Yıl değeri bir tam sayıya dönüştürülüyor
                yil = int(yil)
                # Etkiler sözlüğünde statü kontrol ediliyor
                if statu in etkiler:
                    # Statünün etkisi hesaplanıyor
                    etki = yil * etkiler[statu]

                    # Eğer hesaplanan etki, maksimum etkiden daha büyükse, yeni en uygun statü olarak atanıyor
                    if etki > maks_etki:
                        maks_etki = etki
                        en_uygun_statu = statu
                else:
                    # Geçersiz bir statü varsa hata mesajı döndürülüyor
                    return "Geçersiz bir statü bulunuyor. Lütfen kontrol ediniz."
            except ValueError:
                # Geçersiz bir yıl değeri varsa hata mesajı döndürülüyor
                return "Geçersiz bir yıl değeri bulunuyor. Lütfen kontrol ediniz."

        # En uygun statü sonucu döndürülüyor
        return en_uygun_statu

    def __str__(self):
        # En uygun statü bulunuyor
        en_uygun_statu = self.statu_bul()
        # İnsan bilgileri ve en uygun statü birleştirilerek sonuç döndürülüyor
        return f"{super().__str__()}, En Uygun Statü: {en_uygun_statu}"