######case1
# x = float(input("x sonni kiriting: "))
# match x:
#     case 1:
#         print("Dushanba")
#     case 2:
#         print("Seshanba")
#     case 3:
#         print("Chorshanba")
#     case 4:
#         print ("Payshnba")
#     case 5:
#         print ("Juma")
#     case 6:
#         print("Shanba")
#     case 7:
#         print("Yakshanba")
#     case _:
#         print("Notugri raqam")
######case2
# x = float(input("x sonni kiriting: "))
# match x:
#     case 1:
#         print("yomon")
#     case 2:
#         print("qoniqarsiz")
#     case 3:
#         print("qoniqarli")
#     case 4:
#         print ("yaxshi")
#     case 5:
#         print ("Alo")
#     case _:
#         print("Notugri raqm kiritildi")

######case3
# x = float(input("x sonni kiriting: "))
# match x:
#     case 1:
#         print("1-oy,qish")
#     case 2:
#         print("2-oy,qish")
#     case 3:
#         print("3-oy,bahor")
#     case 4:
#         print("4-oy,bahor")
#     case 5: 
#         print("5-oy, bahor")
#     case 6:
#         print("6-oy, yoz")
#     case 7:
#         print("7-oy,yoz")
#     case 8:
#         print("8-oy,yoz")
#     case 9:
#         print("9-oy,kuz")
#     case 10:
#         print("10-oy,kuz")
#     case 11:
#         print("11-oy,kuz")
#     case 12:
#         print("12-oy,qish")
#     case _:
#         print("Notugri raqam kiritildi:")

######case4
# x = float(input("x sonni kiriting: "))
# match x:
#     case 1:
#         print("Yanvar 31 kun mavjud")
#     case 2:
#         print("fevral 28 kun mavjud")
#     case 3:
#         print("mart 31 kun mavjud")
#     case 4:
#         print("may 31 kun mavjud")

######case5
# a = float(input("a sonni kiriting:\n >>> "))
# b = float(input("b sonni kiriting:\n >>> "))
# x = int(input("Amalni kiriting(1-qoshish),(2-ayirish),(3-bolish),(4-kopaytrish):\n>>>"))
# match x:
#     case 1:
#         print(a+b)
#     case 2:
#         print(a-b)
#     case 3:
#         print(a/b)
#     case 4:
#         print(a*b)
#     case _:
#         print("Notugri raqam")
######case6
# a = float(input("Kesma uzunligini kiriting:\n >>> "))
# x = int(input("Amalni kiriting(1-detsimetr),(2-kilometr),(3-metr),(4-millimetr)(5-santimetr):\n>>>"))
# match x:
#     case 1:
#         print(a/10, "metr")
#     case 2:
#         print(a*1000, "metr")
#     case 3:
#         print(a,"metr")
#     case 4:
#         print(a/1000, "metr")
#     case 5 :
#         print(a/100, "metr")

#     case _:
#         print("Notugri raqam")

######case7
# a = float(input("ogirlikni  kiriting:\n >>> "))
# x = int(input("Amalni kiriting(1-kliogramm),(2-milligramm),(3-tonna),(4-sentnet):\n>>>"))
# match x:
#     case 1:
#         print(a, "kilogramm")
#     case 2:
#         print(a/1000, "kilogramm")
#     case 3:
#         print(a*1000,"kilogramm")
#     case 4:
#         print(a*100, "kilogramm")

#     case _:
#         print("Notugri raqam")

######case10

# yonalish = input("Yo'nalishni kiriting ('s'-shimol, 'j'-janub, 'q'-sharq, 'g'-g'arb):\n>>> ")
# komanda = int(input("Komandani kiriting (0-harakatni davom ettir, 1-chapga buril, 2-o'ngga buril):\n>>> "))
# match yonalish, komanda:
#     case ('s', 0):
#         print("Shimol tomonga harakat davom ettirilmoqda")
#     case ('s', 1):
#         print("Shimol tomonga chapga burildi")
#     case ('s', 2):
#         print("Shimol tomonga o'ngga burildi")
#     case ('j', 0):
#         print("Janub tomonga harakat davom ettirilmoqda")
#     case ('j', 1):
#         print("Janub tomonga chapga burildi")
#     case ('j', 2):
#         print("Janub tomonga o'ngga burildi")
#     case ('q', 0):
#         print("Sharq tomonga harakat davom ettirilmoqda")
#     case ('q', 1):
#         print("Sharq tomonga chapga burildi")
#     case ('q', 2):
#         print("Sharq tomonga o'ngga burildi")
#     case ('g', 0):
#         print("G'arb tomonga harakat davom ettirilmoqda")
#     case ('g', 1):
#         print("G'arb tomonga chapga burildi")
#     case ('g', 2):
#         print("G'arb tomonga o'ngga burildi")
#     case _:
#         print("Noto'g'ri raqam yoki yo'nalish kiritildi")

######case11
# yonalish = input("Yo'nalishni kiriting ('s'-shimol, 'j'-janub, 'q'-sharq, 'g'-g'arb):\n>>> ")
# komanda = int(input("Komandani kiriting (0-o'ngga buril, 1-chapga buril, 2-180'gradusga buril ):\n>>> "))
# match yonalish, komanda:
#     case ('s', 0):
#         print("Shimol tomonga o'ngga burildi")
#     case ('s', 1):
#         print("Shimol tomonga chapga burildi")
#     case ('s', 2):
#         print("Shimol tomonga 180'gradusga burildi")
#     case ('j', 0):
#         print("Janub tomonga tomonga o'ngga burildia")
#     case ('j', 1):
#         print("Janub tomonga chapga burildi")
#     case ('j', 2):
#         print("Janub tomonga 180'gradusga burildi")
#     case ('q', 0):
#         print("Sharq tomonga o'ngga burildi")
#     case ('q', 1):
#         print("Sharq tomonga chapga burildi")
#     case ('q', 2):
#         print("Sharq tomonga 180'gradusga burildi")
#     case ('g', 0):
#         print("G'arb tomongao'ngga burildi")
#     case ('g', 1):
#         print("G'arb tomonga chapga burildi")
#     case ('g', 2):
#         print("G'arb tomonga 180'gradusga burild")
#     case _:
#         print("Noto'g'ri raqam yoki yo'nalish kiritildi")

######case12


