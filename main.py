#Tapsriq 1 (1. Maximum 4 rəqəmli ədəd daxil edilir. Ədədin neçə rəqəmdən ibarət olduğunu hesablayan program yazın.)
reqem=input("Reqemi daxil et:")
if len(reqem)==4:
    print("Edediniz 4 reqem den ibaretdir")
elif len(reqem)==3:
    print("Edediniz 3 reqem den ibaretdir")
elif len(reqem)==2:
    print("Edediniz 2 reqem den ibaretdir")
elif len(reqem)==1:
    print("Edediniz 1 reqem den ibaretdir")
else:
    print("Edediniz 0 reqem den ibaretdir")

#Tapsiriq 2 (2.İstifadəçi ədəd daxil edir. Onun 3-ə, 5-ə, 7-ə bölünüb bölünməməsini (qalıqsız) yoxlayın.(Her 3 bolme yoxlanmali))
num=int(input("Ededi daxil et:"))

if num%3==0:
    print("Edediniz 3 qaliqsiz bolunur")
else:
    print(f"Edediniz 3 e qaliqla bolunur qaliqiniz {num%3}")

if num%5==0:
    print("Edediniz 5 qaliqsiz bolunur")
else:
    print(f"Edediniz 5 e qaliqla bolunur qaliqiniz {num%5}")

if num%7==0:
    print("Edediniz 7 qaliqsiz bolunur")
else:
    print(f"Edediniz 7 e qaliqla bolunmur qaliqiniz {num%7}")

#Tapsiriq 3 (3.İstifadəçi iki ədəd daxil edir. ( X və Y ) Əgər X Y-ə qalıqsız bölünürsə ekrana Yes çıxır, əks halda No.)
x=int(input("X ededini daxil edin:"))
y=int(input("Y ededini daxil edin:"))

if x%y==0:
    print("Yes")
else:
    print("No")