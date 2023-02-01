from datetime import datetime
from colorama import Back,init,Fore
import requests
import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time

os.system("cls")
init(autoreset=True)

class İnformation(object):
    def __init__(self):
        self.banner()

    def banner(self):
        print(Fore.RED+r"""                   
                (                           )
          ) )( (                           ( ) )( (
       ( ( ( )  ) )                     ( (   (  ) )(
      ) )     ,,\\\                     ///,,       ) (
   (  ((    (\\\\//                     \\////)      )
    ) )    (-(__//                       \\__)-)     (
   (((   ((-(__||                         ||__)-))    ) )
  ) )   ((-(-(_||           ```\__        ||_)-)-))   ((
  ((   ((-(-(/(/\\        ''; 9.- `      //\)\)-)-))    )
   )   (-(-(/(/(/\\      '';;;;-\~      //\)\)\)-)-)   (   )
(  (   ((-(-(/(/(/\======,:;:;:;:,======/\)\)\)-)-))   )
    )  '(((-(/(/(/(//////:%%%%%%%:\\\\\\)\)\)\)-)))`  ( (
   ((   '((-(/(/(/('uuuu:WWWWWWWWW:uuuu`)\)\)\)-))`    )
     ))  '((-(/(/(/('|||:wwwwwwwww:|||')\)\)\)-))`    ((
  (   ((   '((((/(/('uuu:WWWWWWWWW:uuu`)\)\))))`     ))
        ))   '':::UUUUUU:wwwwwwwww:UUUUUU:::``     ((   )
          ((      '''''''\uuuuuuuu/``````         ))
           ))            `JJJJJJJJJ`           ((
             ((            LLLLLLLLLLL         ))
               ))         ///|||||||\\\       ((
                 ))      (/(/(/(^)\)\)\)       ((
                  ((                           ))
                    ((                       ((
                      ( )( ))( ( ( ) )( ) (()   


                      {OWNER : 'Endi}   
                """)
        print(Fore.LIGHTGREEN_EX+"=== %10")
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX+"====== %30")
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX+"======== %50")
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX+"=========== %70")
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX+"================ %100")
        time.sleep(1)
        while True:
            print(Fore.RED+"Merhaba Bilgi Toplama Aracına Hoş Geldiniz Aracımızı Şu Anda Çalışır Olup Geliştirilmeye Devam Edecektir...")
            print(Fore.LIGHTBLUE_EX+"""Arama Yapmak İstediğiniz Bölüm:
                        [1] Github
                        [2] İnstagram 
                        [3] Facebook (Soon)
                        [4] Çıkış
                """)
            secim=input(Fore.LIGHTBLUE_EX+"Seçiniz : ")
            if secim == "1":
                self.github()
            if secim == "2":
                self.instagram()
            if secim == "3":
                self.facebook()
            if secim == "4":
                self.exit()
    def github(self):
        name=input(Fore.LIGHTBLUE_EX+"Kişinin Kullanıcı Adı Nedir: ")
        __url="https://api.github.com/users/"
        __requests= requests.get(url=__url + name).json()
        print(Fore.LIGHTGREEN_EX+"=== %10")
        time.sleep(0.5)
        print(Fore.LIGHTGREEN_EX+"====== %30")
        time.sleep(0.5)
        print(Fore.LIGHTGREEN_EX+"======== %50")
        time.sleep(0.5)
        print(Fore.LIGHTGREEN_EX+"=========== %70")
        time.sleep(0.5)
        print(Fore.LIGHTGREEN_EX+"================ %100")
        time.sleep(0.5)
        print(Fore.RED+"---Kişinin Bilgileri---")
        print(f"""
        {Fore.LIGHTGREEN_EX} İsim : {__requests['name']}
        {Fore.LIGHTGREEN_EX} Şirket : {__requests['company']}
        {Fore.LIGHTGREEN_EX} Blog : {__requests['blog']}
        {Fore.LIGHTGREEN_EX} Email : {__requests['email']}
        {Fore.LIGHTGREEN_EX} Yer : {__requests['location']}
        {Fore.LIGHTGREEN_EX} Depo Sayısı : {__requests['public_repos']}
        {Fore.LIGHTGREEN_EX} Takipçi Sayısı : {__requests['followers']}
        {Fore.LIGHTGREEN_EX} Takip Sayısı : {__requests['following']}
        {Fore.LIGHTGREEN_EX} Biyografi : {str(__requests['bio']).strip()}
        {Fore.LIGHTGREEN_EX} Hesap Kurulma Tarihi : {(__requests['created_at'])}
        """)
    def instagram(self):
        name=input(Fore.LIGHTBLUE_EX+"Kişinin Kullanıcı Adı Nedir: ")
        __url="https://www.instagram.com/"
        __request = Request(url=__url + name,headers={'User-Agent':'Mozilla/5.0'})
        htmlverisi = urlopen(__request).read()
        soup = BeautifulSoup(htmlverisi, "html.parser")
        veri = soup.find("meta", property="og:description").attrs['content']
        veri = veri.split("-")[0]
        veri = veri.split(" ")
        print(Fore.LIGHTGREEN_EX+"=== %10")
        time.sleep(0.5)
        print(Fore.LIGHTGREEN_EX+"====== %30")
        time.sleep(0.5)
        print(Fore.LIGHTGREEN_EX+"======== %50")
        time.sleep(0.5)
        print(Fore.LIGHTGREEN_EX+"=========== %70")
        time.sleep(0.5)
        print(Fore.LIGHTGREEN_EX+"================ %100")
        time.sleep(0.5)
        print(Fore.RED+"---Kişinin Bilgileri---")
        print(Fore.LIGHTGREEN_EX+"Takipçi Sayısı : ",veri[0])
        print(Fore.LIGHTGREEN_EX+"Takip Sayısı : ",veri[2])
        print(Fore.LIGHTGREEN_EX+"Gönderi : ",veri[4])
    def facebook(self):
        print(Fore.RED+"Geliştirmeye Devam Ediyoruz...")
    
    def exit(self):
        print(Fore.RED+"Tekrar Görüşmek Dileğiyle...")
        exit()

if __name__ == "__main__":
    clas=İnformation()
    clas.banner()
