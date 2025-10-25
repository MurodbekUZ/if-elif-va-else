# Masala 1: Baho tizimi
# ball = int(input("Ballni kiriting:"))
# if ball < 0 or ball > 100:
#     print("Xato: Ball 0 dan 100 gacha bo‘lishi kerak.")
# else:
#     if ball >= 90:
#         print("A")
#     elif  ball >= 80:
#         print("B")
#     elif ball >= 70:
#         print("C")
#     elif ball >= 60:
#         print("D")
#     else:
#         print("F")

# Masala 2: Yosh va daromad bo‘yicha soliq
# yosh = int(input("Yoshingizni kiriting:"))
# daromad = float(input("Daromadni kiriting:"))
# if  yosh < 0 or yosh > 120 or daromad < 0:
#     print("Xato: Yosh 0-120 oralig‘ida, daromad musbat bo‘lishi kerak.")
# else:
#     if yosh < 18:
#         print("Soliq: 0%")
#     elif yosh <= 60:
#         if daromad > 5000:
#             print("Soliq: 20%")
#         else:
#             print("Soliq: 10%")
#     else:
#         print("Soliq: 5%")

# Masala 3: Kun va vaqt bo‘yicha ish rejimi
# kun = int(input("Hafta kunini kiriting (1-7): "))
# soat = float(input("Soatni kiriting (0-23): "))
# if kun < 1 or kun > 7 or soat < 0 or soat > 23:
#     print("Xato: Kun 1-7, soat 0-23 oralig‘ida bo‘lishi kerak.")
# else:
#     if kun == 6 or kun == 7:
#         print("Dam olish kuni")
#     else:
#         if 9 <= soat <= 17:
#             print("Ish vaqti")
#         else:
#             print("Ish vaqtidan tashqari")

# Masala 4: Iqlim sharoitlari
# harorat = float(input("Haroratni kiriting (C):"))
# yomgir = input("yomg‘ir holatini (True/False) kiriting")
# if harorat < -50 or harorat > 60:
#     print("Xato: Harorat –50°C dan 60°C gacha bo‘lishi kerak.")
# else:
#     if harorat < 0:
#         print("Qor yog‘ishi mumkin")
#     elif harorat <= 20:
#         if yomgir == "True":
#             print("Yomg‘irli va sovuq")
#         else:
#             print("Sovuq, lekin quruq")
#     else:
#         print("Issiq")

# Masala 5: Transport tanlash
# masofa = float(input("Masofani kiriting (km):"))
# vaqt = float(input("Vaqt kiriting (soat):"))
# if masofa < 0 or vaqt < 0:
#     print("Xato: Masofa va vaqt manfiy bo‘lmasligi kerak.")
# else:
#     if masofa < 5:
#         print("Piyoda boring")
#     elif  masofa <= 50:
#         if  vaqt > 1:
#             print("Avtobus")
#         else:
#             print("Velosiped")
#     else:
#         print("Samolyot")

# Masala 6: Bank krediti
# yosh = int(input("Yoshingizni kiriting:"))
# daromad = float(input("Daromadini kiriting:"))
# kredit_summa = float(input("Kredit summa kiriting:"))
# if  yosh < 18 or yosh > 100 or daromad < 0 or kredit_summa <= 0:
#     print("Xato: Yosh 18-100 oralig'ida, daromad va kredit summasi musbat bo'lishi kerak.")
# else:
#     if  yosh < 21:
#         print("Kredit berilmaydi")
#     elif  yosh <= 60:
#         if  daromad > kredit_summa * 0.2:
#             print("Kredit tasdiqlandi")
#         else:
#             print("Kredit rad etildi")
#     else:
#         print("Kredit faqat maxsus shartlarda")

# Masala 7: Restoran menyusi
# ovqat = input("Ovqat turini kiriting. Ovqat turi faqat (go'sht, baliq, vegetarian) shular bo'lsin.")
# narx = float(input("Narxni kiriting:"))
# if  narx <= 0:
#     print("Xato: Narx musbat bo'lishi kerak.")
# else:
#     if  ovqat == "go'sht":
#         if  narx > 50:
#             print("Premium go'shtli taom")
#         else:
#             print("Oddiy go'shtli taom")
#     elif ovqat == "baliq":
#         print("Baliqli taom")
#     elif  ovqat == "vegetarian":
#         if  narx > 30:
#             print("Premium vegetarian")
#         else:
#             print("Oddiy vegetarian")
#     else:
#         print("Xato: Noto'g'ri ovqat turi.")

# Masala 8: Talaba stipendiyasi
# baho = float(input("Bahoni kiriting:"))
# daromad = float(input("Daromadni kiriting:"))
# if  baho < 0 or baho > 5.0 or daromad < 0:
#     print("Xato: Baho 0-5.0 oralig'ida, daromad musbat bo'lishi kerak.")
# else:
#     if baho < 3.0:
#         print("Stipendiya yo'q")
#     elif baho < 4.0:
#         if daromad < 1000:
#             print("Oddiy stipendiya")
#         else:
#             print("Stipendiya yo'q")
#     else:
#         if daromad < 2000:
#             print("Yuqori stipendiya")
#         else:
#             print("Stipendiya yo'q")

# Masala 9: Telefon tarifi
# daqiqalar = int(input("Daqiqani kiriting:"))
# internet = float(input("Internetni kiriting:"))
# if daqiqalar < 0 or internet < 0:
#     print("Xato: Daqiqalar va internet manfiy bo'lmasligi kerak.")
# else:
#     if daqiqalar < 100:
#         print("Mini tarif")
#     elif daqiqalar <= 500:
#         if internet > 5:
#             print("Standart tarif")
#         else:
#             print("Ekonom tarif")
#     else:
#         print("Premium tarif")

# Masala 10: Ob-havo bo'yicha maslahat
# harorat = float (input("Haroratni kiriting:"))
# shamol = float (input("Shamol kiriting:"))
# if harorat < -50 or harorat > 50 or shamol < 0:
#     print("Xato: Harorat –50°C dan 50°C gacha, shamol manfiy emas.")
# else:
#     if harorat > 50 or shamol > 50:
#         print("Uyda qoling")
#     elif harorat <= 25:
#         if shamol < 5:
#             print("Sayr qiling")
#         else:
#             print("Ehtiyot bo'ling")
#     else:
#         print("Suv iching")

# Masala 12: Yil fasli
# oy = int(input("Oy raqamini kiriting:"))
# harorat = float(input("Haroratni kiriting:"))
# if oy < 1 or oy > 12 or harorat < -50 or harorat > 50:
#     print("Xato: Oy 1-12, harorat –50°C dan 50°C gacha bo'lishi kerak.")
# else:
#     if  oy == 12 or oy == 1 or oy == 2:
#         print("Qish")
#     elif 3 <= oy <= 5:
#         if  harorat > 15:
#             print("Iliq bahor")
#         else:
#             print("Sovuq bahor")
#     elif 6 <= oy <= 8:
#         print("Yoz")
#     else:
#         print("Kuz")

# Masala 13: Chegirma tizimi
summa = float(input("Xarid summasini kiriting:"))
doimiy_mijoz = input("Doimiy mijoz ekanlikingizni kiriting (True va False):")
if summa <= 0:
    print("Xato: Summa musbat bo'lishi kerak.")
else:
    if summa < 100:
        print("Chegirma 0 ")
    elif summa <= 500:
        if doimiy_mijoz == "True":
            print("Chegirma 10")
        else:
            print("chegirma = 5")
    else:
        print("Chegirma 15")



































