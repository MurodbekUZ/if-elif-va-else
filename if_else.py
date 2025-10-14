# 1-masala 🛒 Onlayn xarid chegirmasi
# summa = int(input("Xarid summasini kiriting:"))
# if summa < 50000:
#     print("Chegirma yo'q")
# elif summa < 100000:
#     print("5% chegirma")
# elif summa < 200000:
#     print("10% chegirma")
# else:
#     print("15% chegirma")

# 2-masala 🚦 Yo‘l harakati chirog‘i maslahati
# rang = input("Svetofor rangini kiriting:")
# yol = input("Svetofor yolini kiriting, masalan: (bo'sh yoki band):")
# if rang == 'qizil':
#     print("To'xtang")
# elif rang == 'sariq':
#     print("Tayyorlaning")
# elif rang == 'yashil':
#     if yol == "bo'sh":
#         print("Yuring")
#     else:
#         print("Kuting")
# else:
#     print("Iltimos kuting")

# 3-masala 💊 Dori ichish vaqti
# soat = int(input("Hozirgi soatni butun son sifatida (0–23) kiriting:"))
# if soat in [6, 7, 8, 9, 10, 11]:
#     print("Ertalabgi dori")
# elif soat in [12, 13, 14, 15, 16, 17]:
#     print("Kunduzgi dori")
# elif soat in [18, 19, 20, 21, 22, 23]:
#     print("Kechki dori")
# elif soat in [0, 1, 2, 3, 4, 5,]:
#     print("Hozir dori ichish kerak emas")
# else:
#     print("Siz mavjud bolmagan vaqtni kiritingiz:")

# 4-masala 🌡️ Haroratga qarab kiyim tanlash
# harorat = int(input("Hozirgi haroratni kiriting:"))
# if harorat < 0:
#     print("Qalin palto, qo‘lqop kiying")
# elif 0 < harorat < 15:
#     print("Jaket kiying:")
# elif 15 < harorat < 25:
#     print("Futbolka yetarli:")
# elif harorat > 25:
#     print("Yengil kiyim, soyobon oling:")

# 5-masala 🎒 Maktab sumkasi og‘irligi
# sinf = int(input("O‘quvchining sinfini (butun son)da kiriting:"))
# sumka = float(input("Sumka og‘irligini (haqiqiy son)da kiriting:"))
# if sinf in [1, 2, 3, 4] or sumka > 2.0:
#     print("Og'ir kamaytiring!")
# elif sinf in [5, 6, 7, 8, 9] or sumka > 4.0:
#     print("Og'ir kamaytiring!")
# else:
#     print("Normal")

# 6-masala 🏥 Bemor navbatini belgilash
# yosh = int(input("Bemor yoshini (butun son)da kiriting!"))
# holat = input("Holatini (oddiy yoki og‘ir)likini kiriting!")
# if holat == "og'ir":
#     print("Zudlik bilan")
# elif 10 < yosh > 70:
#     print("1-soat ichida")
# else:
#     print("3-soat ichida")

# 7-masala 🚕 Taksi narxi (dam olish kuni)
# 7-masala
# kun = input("Kun nomini kiriting (masalan: Dushanba, Seshanba...): ").lower()
# masofa = float(input("Masofani kiriting (km): "))
#
# ish_kuni = ['dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma']
# dam_kuni = ['shanba', 'yakshanba']
#
# if kun in dam_kuni:
#     if masofa > 10:
#         print("Bugun dam olish kuni!")
#         print(f"Summa: {(3600 * masofa) * 0.9} Sizga masofa 10 kmdan oshganligi sababli 10% chegirma beriladi.")
#     else:
#         print("Bugun dam olish kuni!")
#         print(f"Summa: {3600 * masofa} so'm.")
# elif kun in ish_kuni:
#     if masofa > 10:
#         print("Bugun ish kuni!")
#         print(f"Summa: {(3000 * masofa) * 0.9} so'm. Sizga masofa 10 kmdan oshganligi sababli 10% chegirma beriladi.")
#     else:
#         print("Bugun ish kuni!")
#         print(f"Summa: {3000 * masofa} so'm.")
# else:
#     print("Qiymat xato kiritildi!")