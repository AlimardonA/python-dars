###############Listlar##################
# ismlar = ['Abror', 'Mahmud','Ilhom']
# print("Salom", ismlar[0],"bugun choyxona bormi?")
# print(ismlar[1], 'choyxonaga boramizmi?')

# sonlar = []
# sonlar.append(1)
# print(sonlar)

a = [ ]
s = 1
k= 0
while True:
    mahsulot = input(f" {s}-Masulotni kiriting:\n >>>")
    a.append(mahsulot)
    javob = input("Yana mahsulot qushasizmi?(ha/yo'q)\n>>>")
    if javob == "ha":
        s+=1
    else:
        break
for i in a:
    k+=1
    print(f"{k}.{i.title()}")







