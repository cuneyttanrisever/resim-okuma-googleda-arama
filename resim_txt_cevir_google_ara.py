#coding:utf-8
import cv2
import numpy as np
import re
import sys
import urllib
import os
import requests
import bs4
import time
import datetime
from PIL import Image , ImageGrab
print("Coder Cüneyt TANRISEVER")
print("Resimdeki soruyu yazıya çevirip googlede arama yapıp çıkan sonuca göre seçeneklerden doğru cevabı seçer")
baslangic= datetime.datetime.now()
def gecen(baslangic, bitis):
    sonuc = bitis - baslangic
    d= str(sonuc).split(":")
    dd= d[0]+":"+d[1]+":"+d[2][0:2]
    print "\n\n\nProgram islemi   %s' surede bitirmistir."%(dd)

resim = ImageGrab.grab()
adi="add.jpg"
resim.save(adi,'JPEG')


image=cv2.imread( "C:\\Python27\\add.jpg")    #döndürmek istediğim görüntünün bilgisayarımda ki konumunu belirtiyorum
height, width = image.shape[:2]
print height, width
start_row, start_col=int(height * .1), int(width * .37)      #kırpmak istediğiniz boyuta göre değerler verebilirsiniz
end_row, end_col=int(height * .89), int(width * .63) # burası pencereyı height pencereyı yukarıya dogru kucultuyor sayı arttıkca width ise pencereyı saga donru daraltıp genısletıyor
print end_row, end_col
cropped=image[start_row:end_row , start_col:end_col]
cv2.imwrite("DexmoD.jpg", cropped)
#burada tesseract calıstırılacak ve belirtilen yere dex.txt adında  dosya olusturacak
#komut os.system('tesseract DexmoD.jpg dex')
#dedıkten sonra txt cıkaracak ve asaggıdakı arama bolumu calısacak
komut="\"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe\""
#print komut
tesse=os.system(komut+" DexmoD.jpg dex -l tur")

ky=open("C:\Python27\dex.txt","r").readlines()
kyy= []
asik=0
bsik=0
csik=0
#print ky
soru=""
cevaplar=[]

for dexmod in ky[2:-6]:
	kk=dexmod.replace("\n"," ")
	soru+=kk
for i in ky[-6:-1]:
	dex=i.replace("\n","")
	
	if str("") != dex:
		cevaplar.append(dex)
#print cevaplar
sorudz=soru.replace(" ","+")
Dogrul=["Doğru Cevap","dogru cevap","Doğru Cevab"]

sorudzz=urllib.quote(sorudz)
#print cevaplar
url="https://www.google.com/search?ei=k3JQXP6EI4PRwALGmYX4Aw&q=%s&oq=%s&gs_l=psy-ab.3..35i39.33758.39851..40095...0.0..0.195.3637.0j21......0....1..gws-wiz.......0i8i13i30j0j0i203j0i22i30.bZ8Ly4qW3A8"%(sorudzz,sorudzz)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
rq=requests.session()
rq.headers.update(headers)
print "google aramasi basladi---- "
res=rq.get(url)
rm=res.content
print "google aramasi bitti "
soup = bs4.BeautifulSoup(rm,'html.parser')
dex= soup.find_all('a')
#print dex
for ia in dex:
    l=re.findall('href+',str(ia))
   # print l
say=0
at=[]
solmenu = soup.find_all("div",attrs={"class":"r"})
dos=open("denemee.txt","w")
for link in solmenu:
	dex= link.find_all('a', href=True)
	spp=str(dex).split("ping")
	dz=str(spp[0]).replace("[<a href=","")
	dzz=dz.replace("\"","")

	dk=at.append(str(dzz))
	
#print at[0:3]
	
try:
	for i in at:
		res=rq.get(i,timeout=1)
		rm=res.content
		#print res.url
		for ii in cevaplar:
			dex12= re.findall(ii,rm)
			#print dex12
			if [] != dex12:
				if ii == cevaplar[0]:
					asik+=1
				if ii == cevaplar[1]:
					bsik+=1
				if ii == cevaplar[2]:
					csik+=1
			else:
				pass
			#	print "bulunamedı ::::::::::::"
		for j in Dogrul:
			kelime=str(j)+".+"
			dex122= re.findall(kelime,rm)
			if [] != dex122:
				k=""
				k=str(dex122).replace("\n","")
				kk=str(k).replace("\r","")
				if [] !=  kk:
					print "Doğru Cevap = ",dex122
		
except requests.exceptions.ConnectionError:
    print "\n boyle bir site yok ve ya ban yedin diye baglanmadi"
    pass
except requests.exceptions.Timeout:
    print "\nzaman asimi olustu bu url atlandi"
    pass
except requests.exceptions.TooManyRedirects:
    print"\n 20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"
    pass
except IOError:
        	print "belirtilen dosya bulunamadi"

if asik>bsik:
	if asik>csik:
		print """"
		####################################
		#                                  #
		#                                  #
		#       CEVAP A  == %s #
		#                                  #
		#                                  #
		####################################""" %(cevaplar[0])
if bsik>asik:
	if bsik>csik:
		print """"
		####################################
		#                                  #
		#                                  #
		#       CEVAP B  == %s #
		#                                  #
		#                                  #
		####################################""" %(cevaplar[1])
if csik>asik:
	if csik>bsik:
		print """"
		####################################
		#                                  #
		#                                  #
		#       CEVAP C  == %s #
		#                                  #
		#                                  #
		####################################""" %(cevaplar[2])
#print asik
#print bsik
#print csik			
bitis= datetime.datetime.now()
gecen(baslangic,bitis)
