import os
dosya_list=[]
with open("passwords.txt","r",encoding="utf-8") as dosya:
    passwords=dosya.readlines()
for password in passwords:
    dosya_list.append(password.replace("\n",""))
def crack(sifre):
    for password in dosya_list:
        if(sifre==password):
            break
        
    return(password)
sifre=input("Lütfen Şifrenizi Giriniz : ")
password2=crack(sifre)
os.system('cls')
sorgu=input("Lütfen Şifreyi Görmek İçin Sorgu Şifresini Giriniz: ")
sorgu.lower()
while True:
    if(sorgu=="hello"):
        print("Şifreniz: {}".format(password2))
        break
    else:
        print("Girdiğiniz Şifre Yanlış... Lütfen Tekrar Deneyiniz: ")