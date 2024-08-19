# dostlar = ['Ali','Vali','Gani','Alish','Sherzod']
# n = 0
# for i in dostlar:
#     n+=1
#     print(f"Salom {i} qandayslar ") # harbir dostga xabar yollash
#     print (f"{n} marta takrorlandi") # tskil n marta takrorlanganligi

#######################################################################
# sonlar = list(range(11,100,2))
# for i in sonlar:
#     print(i)
#     print (i**3)
#####################################################################
# kinolar = []
# print("5 ta eng yaxshi kinolaringizni kiriting")
# for i in range(1,6):
#     kinolar.append(input(f"{i}- kinoni kiriting:\n"))
# print(kinolar)

####################################################################
# a = int(input("Bugun nechta odam bilan suhbat qurdingiz?\n"))
# suhbat = []
# for i in range(a):
#     suhbat.append(input(f"{i+1} -suhbatdoshingizni ismini kiriting"))
# suhbat = [suhbat.upper for ism in suhbat]
# print(suhbat.upper())
################################################################
a = int(input("Bugun nechta odam bilan suhbat qurdingiz?\n"))
suhbat = []
for i in range(a):
    suhbat.append(input(f"{i+1} -suhbatdoshingizni ismini kiriting"))
# Ro'yxatdagi barcha ismlarni katta harfga o'zgartirish
suhbat = [ism.upper() for ism in suhbat]
print(suhbat)


