import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

try:
 # İnsan sınıfı için nesneler oluşturulması ve bilgilerin yazdırılması
 insan1 = Insan("12345678901", "Deniz", "Yildirim", 30, "Kadin", "Turk")
 insan2 = Insan("87654321098", "Alin", "Demir", 25, "Kadin", "Turk")

 print("\n")
 print("Insan sinifi ")
 print(insan1)
 print(insan2)

 # İşsiz sınıfı için nesneler oluşturulması ve bilgilerin yazdırılması
 issiz1 = Issiz("23456789012", "Eda", "Kara", 35, "Erkek", "Turk", { "mavi yaka": 5, "beyaz yaka": 4, "yönetici": 0 })
 issiz2 = Issiz("98765432109", "Beyza", "Beyaz", 28, "Kadin", "Turk", {"mavi yaka": 0, "beyaz yaka": 4, "yönetici": 3 })
 issiz3 = Issiz("45678901234", "Mehmet", "Yetim", 40, "Erkek", "Turk", { "mavi yaka": 7, "beyaz yaka": 4, "yönetici": 0})

 print("\nIssiz sinifi ")
 print(issiz1)
 print(issiz2)
 print(issiz3)

 # Çalışan sınıfı için nesneler oluşturulması ve bilgilerin yazdırılması
 calisan1 = Calisan("34567890123", "Levent", "Kilic", 32, "Erkek", "Alman", "Bilisim", 26, 12000,26520)
 calisan2 = Calisan("54321098765", "Esma", "Akdemir", 25, "Kadin", "Turk", "Pazarlama", 12, 8000,16320)
 calisan3 = Calisan("67890123456", "Zeki", "Kose", 45, "Erkek", "Yunan", "Finans", 62, 18000,41400)

 print("\nCalisan sinifi ")
 print(calisan1)
 print(calisan2)
 print(calisan3)

 # Mavi Yaka sınıfı için nesneler oluşturulması ve bilgilerin yazdırılması
 mavi_yaka1 = MaviYaka("78901234567", "Serdar", "Yasarbas", 28, "Erkek", "Turk", "Bilisim", 26, 12000,14960, 2)
 mavi_yaka2 = MaviYaka("80765432109", "Ayse", "Sagir", 20, "Kadın", "Turk", "Pazarlama", 12, 8000,9013.3, 1)
 mavi_yaka3 = MaviYaka("50678901234", "Volkan", "Sutcuoglu", 30, "Erkek", "Fransiz", "Finans", 60, 18000,23400, 3)

 print("\nMaviYaka sinifi ")
 print(mavi_yaka1)
 print(mavi_yaka2)
 print(mavi_yaka3)

 # Beyaz Yaka sınıfı için nesneler oluşturulması ve bilgilerin yazdırılması
 beyaz_yaka1 = BeyazYaka("20345678901", "Selim", "Kuscu", 41, "Erkek", "Azeri", "Bilisim", 26, 12000, 15556, 3500)
 beyaz_yaka2 = BeyazYaka("70065432109", "Selin", "Akdeniz", 23, "Kadin", "Turk", "Pazarlama", 12, 8000, 10532, 2500)
 beyaz_yaka3 = BeyazYaka("40567890123", "Fatih", "Kara", 37, "Erkek", "Kazak", "Finans", 62, 18000, 23080, 5000)

 print("\nBeyazYaka sinifi ")
 print(beyaz_yaka1)
 print(beyaz_yaka2)
 print(beyaz_yaka3)
 print("\n-----------------------------------------------------------------------------------------------------------------------------")

# DataFrame oluşturma

 data = {
    "nesne": ["Calisan", "Calisan", "Calisan", "Mavi_Yaka", "Mavi_Yaka", "Mavi_Yaka", "Beyaz_Yaka", "Beyaz_Yaka", "Beyaz_Yaka"],
    "tc_no": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), mavi_yaka1.get_tc_no(), mavi_yaka2.get_tc_no(), mavi_yaka3.get_tc_no(), beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no(), beyaz_yaka3.get_tc_no()],
    "ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), mavi_yaka1.get_ad(), mavi_yaka2.get_ad(), mavi_yaka3.get_ad(), beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()],
    "soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), mavi_yaka1.get_soyad(), mavi_yaka2.get_soyad(), mavi_yaka3.get_soyad(), beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad(), beyaz_yaka3.get_soyad()],
    "yas": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), mavi_yaka1.get_yas(), mavi_yaka2.get_yas(), mavi_yaka3.get_yas(), beyaz_yaka1.get_yas(), beyaz_yaka2.get_yas(), beyaz_yaka3.get_yas()],
    "cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), mavi_yaka1.get_cinsiyet(), mavi_yaka2.get_cinsiyet(), mavi_yaka3.get_cinsiyet(), beyaz_yaka1.get_cinsiyet(), beyaz_yaka2.get_cinsiyet(), beyaz_yaka3.get_cinsiyet()],
    "uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), mavi_yaka1.get_uyruk(), mavi_yaka2.get_uyruk(), mavi_yaka3.get_uyruk(), beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk(), beyaz_yaka3.get_uyruk()],
    "sektor": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), mavi_yaka1.get_sektor(), mavi_yaka2.get_sektor(), mavi_yaka3.get_sektor(), beyaz_yaka1.get_sektor(), beyaz_yaka2.get_sektor(), beyaz_yaka3.get_sektor()],
    "tecrube": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), mavi_yaka1.get_tecrube(), mavi_yaka2.get_tecrube(), mavi_yaka3.get_tecrube(), beyaz_yaka1.get_tecrube(), beyaz_yaka2.get_tecrube(), beyaz_yaka3.get_tecrube()],
    "maas": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), mavi_yaka1.get_maas(), mavi_yaka2.get_maas(), mavi_yaka3.get_maas(), beyaz_yaka1.get_maas(), beyaz_yaka2.get_maas(), beyaz_yaka3.get_maas()],
    "yipranma_payi": [0, 0, 0, mavi_yaka1.get_yipranma_payi(), mavi_yaka2.get_yipranma_payi(), mavi_yaka3.get_yipranma_payi(), 0, 0, 0],
    "tesvik_primi": [0, 0, 0, 0, 0, 0, beyaz_yaka1.get_tesvik_primi(), beyaz_yaka2.get_tesvik_primi(), beyaz_yaka3.get_tesvik_primi()],
    "yeni_maas": [calisan1.get_yeni_maas(), calisan2.get_yeni_maas(), calisan3.get_yeni_maas(), mavi_yaka1.get_yeni_maas(), mavi_yaka2.get_yeni_maas(), mavi_yaka3.get_yeni_maas(), beyaz_yaka1.get_yeni_maas(), beyaz_yaka2.get_yeni_maas(), beyaz_yaka3.get_yeni_maas()]
 }
 # Pandas ayarlarını değiştirme

 pd.set_option('display.max_columns', None)
 pd.set_option('display.expand_frame_repr', False)
 df = pd.DataFrame(data)
 df["tecrube"] = df["tecrube"] // 12
 print("\nDataFrame:")
 print(df)
 print("\n-----------------------------------------------------------------------------------------------------------------------------\n")

 # a) Boş değerleri 0 ile doldurma
 df.fillna(0, inplace=True)

 # b) Gruplandırma ve ortalama hesaplama
 print("Gruplara göre tecrube ve yeni maas ortalamalari..\n")
 gruplanmis_df = df.groupby("nesne").agg({"tecrube": "mean", "yeni_maas": "mean"})
 print(gruplanmis_df)
 print("\n-----------------------------------------------------------------------------------------------------------------------------\n")

 # c) Maaşı 15000TL üzerinde olanların sayısı
 maas_15000_ustu = df[df["maas"] > 15000].shape[0]
 print("Maaşı 15000 TL üzerinde olanların toplam sayısı:", maas_15000_ustu)
 print("\n-----------------------------------------------------------------------------------------------------------------------------\n")

 # d) Yeni maaşa göre küçükten büyüğe sıralama
 print("Yeni maaslari kucukten buyuge siralama..\n")
 siralama_df = df.sort_values("yeni_maas")
 print(siralama_df)
 print("\n-----------------------------------------------------------------------------------------------------------------------------\n")

 # e) Tecrübesi 3 yildan fazla olan Beyaz yakalılar
 print("Tecrubesi 3 yildan fazla olan beyaz yakalilar..\n")
 tecrube_3ten_fazla = df[(df["nesne"] == "Beyaz_Yaka") & (df["tecrube"] > 3)]
 print(tecrube_3ten_fazla)
 print("\n-----------------------------------------------------------------------------------------------------------------------------\n")

 # f) Yeni maaşı 10000 TL üzerinde olanlar için 2-5 satır arası TC ve yeni maaş sütunlarını seçme
 print("Maasi 10000 TL den fazla olanlarin tc ve yeni maas bilgisi..\n")
 yeni_maas_10000_ustu = df[df["yeni_maas"] > 10000].iloc[2:5, [1, -1]]
 print(yeni_maas_10000_ustu)
 print("\n-----------------------------------------------------------------------------------------------------------------------------\n")

 # g) Ad, soyad, sektor ve yeni maaş içeren yeni DataFrame oluşturma
 print("Yeni dataframe olusturma..\n")
 yeni_df = df[["ad", "soyad", "sektor", "yeni_maas"]]
 print(yeni_df)
except Exception as e:
 print(f"hata:{str(e)}")