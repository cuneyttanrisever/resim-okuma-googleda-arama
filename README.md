# Soruyu yazıya çevirip google da arayıp çıkan sonuçlara göre doğru cevabı seçebilen bir program :D
  
Turkıye yarısta uygulması ıcın gelıstırdıgım otomatık ekran resmını cekıp kesıp cıkan resımden yazıyı cıkarıp
soru ve cevaplar dıye ayırıp soruyu googlede arıyor ve bulunan sıtelere gırıs yapıp 
cevapları karsılastırıyor hangı cvap fazla ıse dogru secenek odur dıyor ayrıca 
sıte ıcerısınde Doğru cevap veya dogru cevap gıbı yazılar varsa o satırı ekrana bastırıp sıklardan ayrı olarak verebılıyor
secımı sıze bırakıyor
 
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

bu modullerin yuklenmesi gerek ve 
tesseract exe nın yuklenmesı gerek ve tr dıl destegıde yuklenmesı gerekıyor
yoksa calısmaz
768 1366 ekran boyutuna gore tasarlanmıstır
683 860 sorunun ekran boyutu budur
