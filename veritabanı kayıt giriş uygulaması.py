import ast         #Json'daki veriyi sözlük olarak okumak için
import json         #Sözlüğü stringe çevirip tekrar json'a yazmak için
import time


f=open("data.json","r")                 #Json dosyasını okuma formatında açalım
sözlük=ast.literal_eval(f.read())         #Json dosyasını string şeklinde okuyup sözlüğe çevirir

soru=input("Giriş (g), kayıt (k) : ")
soru=soru.lower()
if soru=="k":
    que=input("Id belirleyin : ")           #sözlüğe eklenecek key ögesini oluşturur.
    que2=input("Şifre belirleyin : ")       #sözlüğe eklenecek value ögesini oluşturur.
    sözlük.setdefault(que,que2)             #sözlüğe ögeleri ekleyelim.
    metin=json.dumps(sözlük)                #güncellenmiş sözlüğü jsona yazabilmek için stringe dönüştürelim.
    f2=open("data.json","w")                #jsonu "w" formatında açalım ki üstüne yazmasın.
    f2.write(metin)                     #stringi jsona yazalım.
    f2.close()                          #dosyayı kapatmayı unutmuyoruz.
    print("Kayıt başarılı... ")
    time.sleep(2)
elif soru=="g":
    que3=input("Id'niz ne ? : ")
    if que3 in sözlük.keys():                 #eğer girilen id veritabanında varsa şifre ister.
        que4=input("Şifreniz ne ? :")
        if que4==sözlük[que3]:                 #id ile şifre uyuşuyorsa giriş sağlanır.
            print("Hoşgeldiniz. ")
            time.sleep(2)
            
        else:
            print("Şifre hatalı. ")            #id ile şifre uyuşmuyorsa giriş sağlanamaz.
            time.sleep(2)
    else:
        print("Böyle bir ID yok! ")
        time.sleep(2)