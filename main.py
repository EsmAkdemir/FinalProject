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
