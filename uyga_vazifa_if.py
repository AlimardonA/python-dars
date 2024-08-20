#######if10
# a = float(input("A sonni kiriting: "))
# b = float(input("B sonni kiriting: "))
# if a> b:
#     a, b = b, a
# print(f"a soni: {a}")
# print(f"b soni: {b}")
#######if11
# a = float(input("a sonni kiriting: "))
# b = float(input("b sonni kiriting: "))
# if a > b:
#     a, b = a, a
# elif a == b:
#     a,b = 0, 0
# else:
#     a, b = b,b
# print(f"a soni: {a}")
# print(f"b soni: {b}")

#######if12
# a = float(input("a sonni kiriting: "))
# b = float(input("b sonni kiriting: "))
# c = float(input("c sonni kiriting: "))
# if b >= a and c >= a:
#     kichik = a
# elif  a >= b and c >= b :
#     kichik = b
# else:
#     kichik = c
# print (f"Eng kich son:{c}")

#######if13
# a = float(input("a sonni kiriting: "))
# b = float(input("b sonni kiriting: "))
# c = float(input("c sonni kiriting: "))
# if b >= a and c >= a and b >= c:
#     ortacha = c
# elif  a >= b and c >= b and c >= a:
#     ortacha = a
# else:
#     ortacha = b
# print (f"ortacha son:{ortacha}")

#######if14
# a = float(input("a sonni kiriting: "))
# b = float(input("b sonni kiriting: "))
# c = float(input("c sonni kiriting: "))

# Eng kichik sonni topish
# if a <= b and a <= c:
#     kichik = a
# elif b <= a and b <= c:
#     kichik = b
# else:
#     kichik = c

# # Eng katta sonni topish
# if a >= b and a >= c:
#     katta = a
# elif b >= a and b >= c:
#     katta = b
# else:
#     katta = c
# print(f"Eng kichik son: {kichik}, Eng katta son: {katta}")

#######if15
# a = float(input("a sonni kiriting: "))
# b = float(input("b sonni kiriting: "))
# c = float(input("c sonni kiriting: "))

# if a+b >= b+c and a+b>=a+c:
#     d=a+b
# elif a+c>=a+b and a+c>=b+c:
#     d=a+c
# else:
#     d=b+c
# print(d) 

#######if16
# a = float(input("a sonni kiriting: "))
# b = float(input("b sonni kiriting: "))
# c = float(input("c sonni kiriting: "))
# if a<=b and b<=c:
#     a*=2
#     b*=2
#     c*=2
# else:
#     a*=-1
#     b*=-1
#     c*=-1
# print(a,b,c)


# ######if17
# a = float(input("a sonni kiriting: "))
# b = float(input("b sonni kiriting: "))
# c = float(input("c sonni kiriting: "))
# if a<=b and b<=c:
#     a*=2
#     b*=2
#     c*=2
# elif a>=b and b>=c:
#     a*=2
#     b*=2
#     c*=2
# else:
#     a*=-1
#     b*=-1
#     c*=-1
# print(a,b,c)
# ######if18
# a = float(input("a sonni kiriting: "))
# b = float(input("b sonni kiriting: "))
# c = float(input("c sonni kiriting: "))
# if a == b :
#     tartib = 3
# elif a == c:
#     tartib = 2
# else:
#     tartib = 1 
# print(tartib)
# ######if19
# a = float(input("a sonni kiriting: "))
# b = float(input("b sonni kiriting: "))
# c = float(input("c sonni kiriting: "))
# d = float(input("d sonni kiriting: "))
# if a == b and a == c:
#     tartib = 4
# elif a == c and c==d:
#     tartib = 2
# elif a==b and a==d:
#     tartib = 3
# else:
#     tartib = 1 
# print(tartib)

# ######if20

# a = float(input("a sonni kiriting: "))
# b = float(input("b sonni kiriting: "))
# c = float(input("c sonni kiriting: "))
# masofa_b = abs(b - a)
# masofa_c = abs(c - a)
# if masofa_b < masofa_c:
#     eng_yaqin_nuqta = b
#     masofa = masofa_b
# else:
#     eng_yaqin_nuqta = c
#     masofa = masofa_c
# print(f"a nuqtasiga eng yaqin nuqta: {eng_yaqin_nuqta}")
# print(f"Masofa: {masofa}")

# ######if24
# import math
# x = float(input("x sonni kiriting: "))
# if x>0 :
#   f=2*math.sin(x)
# elif x<=0:
#     f=x-6
# print(f)
######if25
# x = float(input("x sonni kiriting: "))
# if x < -2 and x > 2:
#     f = 2 * x
# else:
#     f = -3 * x
# print(f)
######if29
# x = float(input("x sonni kiriting: "))
# if x>0 and x%2!=0:
#     print(x, "musbat toq son")
# elif x>0 and x%2==0:
#     print(x, "musbat juft son")
# elif x<0 and x%2 ==0 :
#     print(x, "juft manfiy")
# elif x<0 and x%2 !=0 :
#     print(x, "toq manfiy")
# else:
#    print("0 ga teng")

######if30
# for son in range(1, 1000):
#     if 10 <= son <= 99 and son % 2 != 0:
#         print(f"{son} ikki xonali toq son")
#     elif 100 <= son <= 999 and son % 2 == 0:
#         print(f"{son} uch xonali juft son")












