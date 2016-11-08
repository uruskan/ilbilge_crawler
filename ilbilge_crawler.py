# -*- coding:utf-8 -*-
import requests , re
print("""
Pardus Topluluk İlbilge Ekibi
Author : ShockvaWe - Yusuf Umut Piynar
Date : 06/11/2016 Gece 3 
Caffein : 600mg
Description : Python Web Crawler For İlbilge
""")
try :
    def crawlla():
        url = input("Lütfen url giriniz Örnek Format : http://www.google.com \n @>> ")
        r = requests.get(url) 
        print("Http request/istek kodu geldi =>> " + str(r.status_code)) #sunucudan gelen http kodu
        kaynak_dosyasi = open("/home/eski/Masaüstü/python/html_kaynak.txt","w")
        html_içerik = str(r.content) #r.content ile sitedeki html içeriği çekiyoruz
        print("Evet sorun olmadığına göre , html içerik çekiliyor... \n")
        kaynak_dosyasi.write(html_içerik) #içeriği str'ye dönüştürüp text dosyasına kaydediyoruz
        kaynak_dosyasi.close() #dosyayı kapatak ki kaynak yemesin hem kapatmak lazım yani :D
        print("Html içerik html_kaynak.txt dosyasına kaydedildi !\n")
        sitedeki_linkler = re.findall('<a href="(.*?)">(.*?)</a>', str(r.content)) #htmlenin içindeki diğer linkleri buluyor
        for link in sitedeki_linkler : #siteden başka sitelere linklere atlamak için..
            if link[0] == '/' : #eğer html içinde 1 link "/" ile başlıyorsa onun başına bulunduğu sitenin urlsini koyarak sitede ilerlemeye çalışıyor örnek : ilbilge.tk + /arkaplan gibi
                yeni_url = url + link
                b = 1
                d = b+".txt"
                r_2 = requests.get(yeni_url)
                yeni_dosya = open('d' , 'w')
                yeni_dosya.write(r_2)
                yeni_dosya.close()
                b += 1
    crawlla() #ve fonksiyonumuzu çalıştırıyoruz :D
except : #eğer siteye bağlantıda sorun çıkarsa program çok garip hatalar veriyordu onun önüne geçmek için :D
    print("MUHTEMELEN Siteye bağlantida sorun yaşaniliyor...")
    
