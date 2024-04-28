#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests , re , os
os.system("setterm -term linux -foreground red")
print("""
Pardus Topluluk İlbilge Ekibi
Author : Yusuf Umut Piynar
Date : 06/11/2016 3am 
Description : Python Web Crawler For İlbilge
VERSION : v0.001 
""")
os.system("setterm -term linux -foreground green")
ilk_url = input("Url Giriniz .. \n @>> ") #URL'yi aldık
r = requests.get(ilk_url) #Siteyi Çekdik
print("Http'den Dönen Kod : " + str(r.status_code)) #Bağlantı hakkında bilgi verelim 
if r.status_code == 404 :         
    print("404 Not Found :D :D ")
elif r.status_code == 200 :
    print("Bağlantı Başarılı !")
alt_linkler = re.findall('<a href="([^"]+)">', str(r.content)) #Bütün linkleri bulduk
print("Sitedeki linkler bulunuyor") 
dosya = open('alt_linkler.txt','w') #Dosyayı for döngüsünün dışında açmak önemli.
for urll in alt_linkler : #şimdi bu döngüde başında / olan linkleri buluyor ve onları ana site linkiyle
    if urll[0] == '/':    #eşliyor
        print("Varsa Alt Linkler Bulunuyor...")
        ilk_url + urll = yeni_t_url #Tamamlanmış link oluşturuldu
        dosya.write(yeni_t_url)
        print("Sitenin alt linkleri alt_linkler.txt'e kaydediliyor...")
dosya.close() #ve for döngüsünün dışında kapatmak :D
dosya2 = open('diger_linkler.txt','w')
for url in alt_linkler:#başında / bulunmayan linkleri çekiyor
    if url[0] != '/' :
        print("Sitedeki diğer linkler diger_linkler.txt'e kaydediliyor..")
        dosya2.write(url) #dosyaları for içinde yazıp
dosya2.close() #for dışında kapatıyoruz.
