#Tapsiriq 4
#4.ATM den 4 emeliyyat yerine yetire bileceyimiz oyun duzeldin
#balans = 5000
#1) Balansa baxmaq
#2) Balans artirmaq
#3) Pul chixartmaq
#4) Chixish

names=["Tuqay","Cavid","Ehmed","Vaqif","Huseyn"]
passwords=["Tuqay123","Cavid123","Ehmed123","Vaqif123","Huseyn123"]
balance=[1000,4232,183,923,422]

def atm_func(name,index):
    print(f"{name} siz hansi ne etmek isdeyirsiz:")
    print("Balans baxmaq,balans artirmaq")
    print("Pul cixartmaq yoxsa Accountdan cixmaq (hansi operatoru etmek isdiyrsizse ekranda gosterilen formada yazin)")
    operation=str(input(":"))
    if operation.lower()=="balans artirmaq":
        num=int(input("Ne qeder balans artirmaq isdeyirsiniz?:"))
        balance[index]=balance[index]+num
        print(f"Balansiniz {balance[index]}")
    elif operation.lower()=="balans baxmaq":
        print(f"Sizin balansiniz {balance[index]} qederdir")
    elif operation.lower()=="pul cixartmaq":
        num1=int(input("Ne qeder Pul cixartmaq isdeyirsiniz?:"))
        balance[index]=balance[index]-num1
        print(f"Artiq balansinizda {balance[index]} pul vardir")


print("ATM-e xos gelmisiniz, sehmet olmasa daxil olun, eger yoxdursa yarat yazin")

name1=str(input("Istifadeci adinizi daxil edin veya yaradin:"))
if name1=="yarat":
    newname=str(input("Istifadeci adinizi daxil edin:"))
    newpassword=str(input("Passwordunuzu daxil edin:"))
    names.append(newname)
    passwords.append(newpassword)
    balance.append(0)
    index1=len(names)-1
    print(f"Xos gelmisiniz {newname}")
    atm_func(newname,index1)
elif name1 in names:
    password=str(input(f"Xos gelmisiniz {name1},Zehmet olmasa passwordunuzu daxil edin:"))
    index1=names.index(name1)
    if password == passwords[index1]:
        atm_func(name1,index1)
    else:
        print("Parol sehvdir")
else:
    print("Invalid bele bir istifadeci adi yoxdur")