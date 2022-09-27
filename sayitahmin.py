"""
1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri
ile buldurmaya çalışın.
"random modülü" için  python random şeklinde arama yapın.
100 üzerinden puanlama yapın. Her soru 20 puan.
Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
üzerinden hesaplansın.
"""
import random
from traceback import print_tb
hak = int(input("Hak sayisi giriniz : "))
sayi2 = random.randint(0, 100)
print(sayi2)
puan = 100
sayac = 0
while hak > 0:
    hak -= 1
    sayac += 1
    sayi = int(input("Sayi giriniz : "))

    if sayi2 == sayi:
        print(f"Dogru tahmin {sayac}. defada bildiniz.\nOyunu kazandın")
        print(f'Toplam puan : { 100 - (20) * (sayac - 1) }')
        break
    elif sayi2 > sayi:
        print("sayiyi buyutun. ")
        puan -= 20
    elif sayi2 < sayi:
        print("sayiyi kucultun")
        puan -= 20
    if hak == 0:
        print(f"Oyunu kaybettin , Sayi {sayi2}")
