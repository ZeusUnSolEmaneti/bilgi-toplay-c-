from datetime import datetime
from colorama import Back,init,Fore
import requests
import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time

os.system("cls")
init(autoreset=True)

class ─░nformation(object):
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
            print(Fore.RED+"Merhaba Bilgi Toplama Arac─▒na Ho┼č Geldiniz Arac─▒m─▒z─▒ ┼×u Anda ├çal─▒┼č─▒r Olup Geli┼čtirilmeye Devam Edecektir...")
            print(Fore.LIGHTBLUE_EX+"""Arama Yapmak ─░stedi─činiz B├Âl├╝m:
                        [1] Github
                        [2] ─░nstagram 
                        [3] Facebook (Soon)
                        [4] ├ç─▒k─▒┼č
                """)
            secim=input(Fore.LIGHTBLUE_EX+"Se├žiniz : ")
            if secim == "1":
                self.github()
            if secim == "2":
                self.instagram()
            if secim == "3":
                self.facebook()
            if secim == "4":
                self.exit()
    def github(self):
        name=input(Fore.LIGHTBLUE_EX+"Ki┼činin Kullan─▒c─▒ Ad─▒ Nedir: ")
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
        print(Fore.RED+"---Ki┼činin Bilgileri---")
        print(f"""
        {Fore.LIGHTGREEN_EX} ─░sim : {__requests['name']}
        {Fore.LIGHTGREEN_EX} ┼×irket : {__requests['company']}
        {Fore.LIGHTGREEN_EX} Blog : {__requests['blog']}
        {Fore.LIGHTGREEN_EX} Email : {__requests['email']}
        {Fore.LIGHTGREEN_EX} Yer : {__requests['location']}
        {Fore.LIGHTGREEN_EX} Depo Say─▒s─▒ : {__requests['public_repos']}
        {Fore.LIGHTGREEN_EX} Takip├ži Say─▒s─▒ : {__requests['followers']}
        {Fore.LIGHTGREEN_EX} Takip Say─▒s─▒ : {__requests['following']}
        {Fore.LIGHTGREEN_EX} Biyografi : {str(__requests['bio']).strip()}
        {Fore.LIGHTGREEN_EX} Hesap Kurulma Tarihi : {(__requests['created_at'])}
        """)
    def instagram(self):
        name=input(Fore.LIGHTBLUE_EX+"Ki┼činin Kullan─▒c─▒ Ad─▒ Nedir: ")
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
        print(Fore.RED+"---Ki┼činin Bilgileri---")
        print(Fore.LIGHTGREEN_EX+"Takip├ži Say─▒s─▒ : ",veri[0])
        print(Fore.LIGHTGREEN_EX+"Takip Say─▒s─▒ : ",veri[2])
        print(Fore.LIGHTGREEN_EX+"G├Ânderi : ",veri[4])
    def facebook(self):
        print(Fore.RED+"Geli┼čtirmeye Devam Ediyoruz...")
    
    def exit(self):
        print(Fore.RED+"Tekrar G├Âr├╝┼čmek Dile─čiyle...")
        exit()

if __name__ == "__main__":
    clas=─░nformation()
    clas.banner()
