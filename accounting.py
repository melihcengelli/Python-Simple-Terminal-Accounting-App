global kalem
global silgi
global defter
global dosya
kalem=0
silgi=0
defter=0
dosya=0
kasaHesabi=0 #nakit odemeler tutuluyor.
bankaHesabi=0 #banka odemeleri tutuluyor.
alinanCekler=0 #cek karsiligi odemeler tutuluyor.
alacakSenetHesabi=0 #senet karsiligi odemeler tutuluyor.
alicilarHesabi=0 #veresiye satislar tutuluyor.
digerStoklar=0 #bitcoin ile satislar tutuluyor.
bitcoinCuzdani=0 #satis karsiligi alinan bitcoinlerin tutuldugu hesap.
yurticiSatislar=0 #satislarin tutuldugu hesap.
hesKDV=0 #satis karsiligi odenen kdvnin tutuldugu hesap.
ticariMallar=0 #alinan ticari mallarin tutuldugu hesap.
indKDV=0 #alis karsligi odenen kdvlerin tutuldugu hesap.
verilenCekler=0 #verilen ceklerin tutuldugu hesap.
borcSenetleri=0 #verile senetlerin tutuldugu hesap.
saticilarHesabi=0 #veresiye alinan mallarin tutuldugu hesap.

veresiye=0
while True:
    try:
       sermaye=float(input("Isletme acilisida isletme icin sermaye belirtiniz, sermaye nakit olarak kasaya aktarılacakir.\nBaslangic sermayenizi giriniz :"))
       if sermaye>=0:
           kasaHesabi+=sermaye
       else:
           print ("Hatali giris yaptiniz")
           continue
       break
    except(ValueError):
        print ("************   Hatali giris yaptiniz.   *****************")
        continue
        
while True:
    giris=str(input("-----------------------------------------------------------------------------------------------------------------------------------\nHosgeldiniz, Asagidaki secenekleri kullanarak menulere erisebilirsiniz...\n\nSatış yapmak için : satis \nAlim yapmak icin : alis\nRapor almak icin : rapor\nProgrami kapatmak icin : kapat\nHesaplara para yatirmak icin : para yatir\nPara cekmek icin : para cek\n\nGiris yapabilirsiniz...:"))
    def satis():
        while True:
            global kalem
            global silgi
            global defter
            global dosya
            global kasaHesabi
            global hesKDV
            global yurticiSatislar
            global alinanCekler
            global bankaHesabi
            global alacakSenetHesabi
            global alicilarHesabi
            global digerStoklar
            global bitcoinCuzdani
            global indKDV
            #SATILAN URUNUN NE OLDUGU SORULUYOR
            while True:
                urunTipi=str(input("-----------------------------------------------------------------------------------------------------------------------------------\nHangi urunu satiyorsunuz?: \n\nStoklardaki urunler :  kalem / silgi / defter / dosya\n\nGiris yapabilirsiniz...:"))
                stoklar=["kalem","silgi","defter","dosya"]
                if urunTipi not in stoklar:
                    print("\n****    Lutfen belirtilen kriterlerde giris yapiniz. Iyi günler dileriz.   ****")
                    continue
                else:
                    pass
                    break
            #ODEME YONTEMI SORULUYOR
            while True:
                odemeTipi=str(input("-----------------------------------------------------------------------------------------------------------------------------------\nHangi odeme yontemiyle odeniyor?: \n\nOdeme yontemlerimiz :  nakit / banka / cek / senet / veresiye / bitcoin\n\nGiris yapabilirsiniz...:"))
                odemeTipleri=["nakit","banka","cek","senet","veresiye","bitcoin"]
                if odemeTipi not in odemeTipleri:
                    print("\n****    Lutfen belirtilen kriterlerde giris yapiniz. Iyi günler dileriz.   ****")
                    continue
                else:
                    pass
                while True:
                    if odemeTipi=="bitcoin":
                        try:
                            anlikBTCdegeri=float(input("BTC alırken anlık BTC/TRY degerini giriniz. : "))
                            break
                        except(ValueError):
                            print ("Hatali giris yaptiniz.")
                            continue
                    else:
                        break
                break
                    
            #KAC ADET URUN SATILDIGI SORULUYOR.
            while True:
                try:
                    adetBilgisi=float(input("-----------------------------------------------------------------------------------------------------------------------------------\nKac adet urun satiyorsunuz?...:"))
                    if adetBilgisi>=0:
                        pass
                    else:
                        print ("Hatali Giris Yapildi. - Deger giremezsiniz.")
                        continue
                except(ValueError):
                    print("Hatali giris yaptiniz.")
                    continue
                break
            else:
                print ("****  Lutfen sayi giriniz. Iyi gunler dileriz.  ****")
                continue
            #URUNUN SATIS FIYATI SORULUYOR.
            while True:
                try:
                    fiyatBilgisi=float(input("-----------------------------------------------------------------------------------------------------------------------------------\nUrunun satis fiyatini giriniz...:"))
                    if fiyatBilgisi>=0:
                        break
                    else:
                        print ("Hatali giris yapildi. - Deger giremezsiniz.")
                        continue
                except(ValueError):
                    print("Hatali giris yaptiniz.")
                    continue
            #MUHASEBE KAYDI
            kdvDahilDeger=fiyatBilgisi*adetBilgisi
            kdvHaricDeger=(kdvDahilDeger/1.18)
            kdvTutari=kdvDahilDeger-kdvHaricDeger
            
            if odemeTipi=="nakit":
                if urunTipi=="kalem":
                    if kalem<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        kasaHesabi+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="silgi":
                    if silgi<adetBilgisi: 
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        kasaHesabi+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="defter":
                    if defter<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        kasaHesabi+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="dosya":
                    if dosya<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        kasaHesabi+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                        
                
                print ("-----------------------------------------------------------------------------------------------------------------------------------\n### Muhasebe Kaydi Asagidaki Gibidir. ###\nBorc Degeri\n100 Kasa    ",kdvDahilDeger,"TL","\n                    Alacak Degeri","\n                    600 Yurtici Satislar    ",kdvHaricDeger,"TL","\n                    391 Hesaplanan KDV",kdvTutari,"TL")
                print ("Muhasebe kaydi gerceklestirilmistir.")
            
            elif odemeTipi=="banka":
                if urunTipi=="kalem":
                    if kalem<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        bankaHesabi+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="silgi":
                    if silgi<adetBilgisi: 
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        bankaHesabi+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="defter":
                    if defter<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        bankaHesabi+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="dosya":
                    if dosya<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        bankaHesabi+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                
                print ("-----------------------------------------------------------------------------------------------------------------------------------\n### Muhasebe Kaydi Asagidaki Gibidir. ###\nBorc Degeri\n102 Bankalar    ",kdvDahilDeger,"TL","\n                    Alacak Degeri","\n                    600 Yurtici Satislar    ",kdvHaricDeger,"TL","\n                    391 Hesaplanan KDV",kdvTutari,"TL")
                print ("Muhasebe kaydi gerceklestirilmistir.")
            
            elif odemeTipi=="cek":
                if urunTipi=="kalem":
                    if kalem<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        alinanCekler+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="silgi":
                    if silgi<adetBilgisi: 
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        alinanCekler+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="defter":
                    if defter<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        alinanCekler+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="dosya":
                    if dosya<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        alinanCekler+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                
                print ("-----------------------------------------------------------------------------------------------------------------------------------\n### Muhasebe Kaydi Asagidaki Gibidir. ###\nBorc Degeri\n10101 Alinan Cekler    ",kdvDahilDeger,"TL","\n                    Alacak Degeri","\n                    600 Yurtici Satislar    ",kdvHaricDeger,"TL","\n                    391 Hesaplanan KDV",kdvTutari,"TL")
                print ("Muhasebe kaydi gerceklestirilmistir.")
                
            elif odemeTipi=="senet":
                if urunTipi=="kalem":
                    if kalem<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        alacakSenetHesabi+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="silgi":
                    if silgi<adetBilgisi: 
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        alacakSenetHesabi+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="defter":
                    if defter<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        alacakSenetHesabi+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="dosya":
                    if dosya<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        alacakSenetHesabi+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                
                print ("-----------------------------------------------------------------------------------------------------------------------------------\n### Muhasebe Kaydi Asagidaki Gibidir. ###\nBorc Degeri\n121 Alacak Senetleri    ",kdvDahilDeger,"TL","\n                    Alacak Degeri","\n                    600 Yurtici Satislar    ",kdvHaricDeger,"TL","\n                    391 Hesaplanan KDV",kdvTutari,"TL")
                print ("Muhasebe kaydi gerceklestirilmistir.")
            elif odemeTipi=="veresiye":
                if urunTipi=="kalem":
                    if kalem<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        alicilarHesabi+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="silgi":
                    if silgi<adetBilgisi: 
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        alicilarHesabi+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="defter":
                    if defter<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        alicilarHesabi+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="dosya":
                    if dosya<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        alicilarHesabi+=kdvDahilDeger
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                
                print ("-----------------------------------------------------------------------------------------------------------------------------------\n### Muhasebe Kaydi Asagidaki Gibidir. ###\nBorc Degeri\n120 Alicilar    ",kdvDahilDeger,"TL","\n                    Alacak Degeri","\n                    600 Yurtici Satislar    ",kdvHaricDeger,"TL","\n                    391 Hesaplanan KDV",kdvTutari,"TL")
                print ("Muhasebe kaydi gerceklestirilmistir.")
            
            elif odemeTipi=="bitcoin":
                if urunTipi=="kalem":
                    if kalem<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        digerStoklar+=kdvDahilDeger
                        btcHesaplama=(kdvDahilDeger/anlikBTCdegeri)
                        bitcoinCuzdani+=btcHesaplama
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="silgi":
                    if silgi<adetBilgisi: 
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        digerStoklar+=kdvDahilDeger
                        btcHesaplama=(kdvDahilDeger/anlikBTCdegeri)
                        bitcoinCuzdani+=btcHesaplama
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="defter":
                    if defter<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        digerStoklar+=kdvDahilDeger
                        btcHesaplama=(kdvDahilDeger/anlikBTCdegeri)
                        bitcoinCuzdani+=btcHesaplama
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                elif urunTipi=="dosya":
                    if dosya<adetBilgisi:
                        print ("******************************************************************************\n*************Stok yetersiz oldugu icin islem iptal edildi.*******************")
                        break
                    else:
                        digerStoklar+=kdvDahilDeger
                        btcHesaplama=(kdvDahilDeger/anlikBTCdegeri)
                        bitcoinCuzdani+=btcHesaplama
                        yurticiSatislar+=kdvHaricDeger
                        hesKDV+=kdvTutari
                        pass
                        
                
                print ("-----------------------------------------------------------------------------------------------------------------------------------\n### Muhasebe Kaydi Asagidaki Gibidir. ###\nBorc Degeri\n157 Diger Stoklar    ",kdvDahilDeger,"TRY","\n                    Alacak Degeri","\n                    600 Yurtici Satislar    ",kdvHaricDeger,"TL","\n                    391 Hesaplanan KDV",kdvTutari,"TL")
                print ("Muhasebe kaydi gerceklestirilmistir.")
                print ("Bitcoin cuzdaniniza:",(btcHesaplama),"BTC eklenmistir.")
            else:
                print ("Hatali giris yapildi.")
                continue
            
             #STOKTAN DUSUS.   
            if urunTipi=="kalem":
                if kalem>=adetBilgisi:
                    kalem-=adetBilgisi
                elif adetBilgisi==0:
                    print ("0 adet urun satmazsiniz.")
                else:
                    print ("\n*****   Girmis oldugunuz satis bilgisi stoklarimizdan fazladir. Lutfen stok girisi yapiniz.    *****")
                    break
            elif urunTipi=="silgi":
                if silgi>=adetBilgisi:
                    silgi-=adetBilgisi
                elif adetBilgisi==0:
                    print ("0 adet urun satamazsiniz.")
                else:
                    print ("\n*****   Girmis oldugunuz satis bilgisi stoklarimizdan fazladir. Lutfen stok girisi yapiniz.    *****")
                    break
            elif urunTipi=="defter":
                if defter>=adetBilgisi:
                    defter-=adetBilgisi
                elif adetBilgisi==0:
                    print ("0 adet urun satamazsiniz.")
                else:
                    print ("\n*****   Girmis oldugunuz satis bilgisi stoklarimizdan fazladir. Lutfen stok girisi yapiniz.    *****")
                    break
            elif urunTipi=="dosya":
                if dosya>=adetBilgisi:
                    dosya-=adetBilgisi
                elif adetBilgisi==0:
                    print ("0 adet urun satamazsiniz.")
                else:
                    print ("\n*****   Girmis oldugunuz satis bilgisi stoklarimizdan fazladir. Lutfen stok girisi yapiniz.    *****")
                    break
            else:
                break
            break
        
            #SATIS KISMI TAMAMLANDI.
            
    def alis():
        while True:
            global kalem
            global silgi
            global defter
            global dosya
            global kasaHesabi
            global hesKDV
            global yurticiSatislar
            global alinanCekler
            global bankaHesabi
            global alacakSenetHesabi
            global alicilarHesabi
            global digerStoklar
            global bitcoinCuzdani
            global ticariMallar
            global indKDV
            global verilenCekler
            global borcSenetleri
            global saticilarHesabi
            global adetBilgisi
            #ALINAN URUNUN NE OLDUGUNU SORUYOR.
            while True:
                urunTipi=str(input("-----------------------------------------------------------------------------------------------------------------------------------\nHangi urunu aliyorsunuz?: \n\nAlinabilecek urunler :  kalem / silgi / defter / dosya\n\nGiris yapabilirsiniz...:"))
                stoklar=["kalem","silgi","defter","dosya"]
                if urunTipi not in stoklar:
                    print("\n****    Lutfen belirtilen kriterlerde giris yapiniz. Iyi günler dileriz.   ****")
                    continue
                else:
                    break
            #ODEME YONTEMI SORULUYOR
            while True:
                odemeTipi=str(input("-----------------------------------------------------------------------------------------------------------------------------------\nHangi odeme yontemiyle oduyorsunuz?: \n\nOdeme yontemlerimiz :  nakit / banka / cek / senet / veresiye / bitcoin\n\nGiris yapabilirsiniz...:"))
                odemeTipleri=["nakit","banka","cek","senet","veresiye","bitcoin"]
                if odemeTipi not in odemeTipleri:
                    print("\n****    Lutfen belirtilen kriterlerde giris yapiniz. Iyi günler dileriz.   ****")
                    continue
                else:
                    pass
                while True:
                    if odemeTipi=="bitcoin":
                        try:
                            anlikBTCdegeri=float(input("BTC verirken anlık BTC/TRY degerini giriniz. : "))
                            break
                        except(ValueError):
                            print ("Hatali giris yaptiniz.")
                            continue
                    else:
                        break           
                break
            
            #KAC ADET URUN ALINDIGI SORULUYOR.
            while True:
                try:
                    adetBilgisi=int(input("-----------------------------------------------------------------------------------------------------------------------------------\nKac adet urun aliyorsunuz?...:"))
                    if adetBilgisi>=0:
                        pass
                    else:
                        print ("Hatali giris yaptiniz. - Deger giremezsiniz.")
                        continue
                except(ValueError):
                    print("Hatali giris yaptiniz.")
                    continue
                break
            else:
                print ("****  Lutfen sayi giriniz. Iyi gunler dileriz.  ****")
                continue
                #URUNUN ALIS FIYATI SORULUYOR.
            while True:
                try:
                    fiyatBilgisi=float(input("-----------------------------------------------------------------------------------------------------------------------------------\nUrunun alis fiyatini giriniz...:"))
                    if fiyatBilgisi>=0:
                        pass
                    else:
                        print ("Hatali giris yaptiniz. - Deger giremezsiniz")
                        continue
                except(ValueError):
                    print("Hatali giris yaptiniz.")
                    continue
                break
            
            
            else:
                pass       
            #MUHASEBE KAYDI
            kdvDahilDeger=fiyatBilgisi*adetBilgisi
            kdvHaricDeger=(kdvDahilDeger/1.18)
            kdvTutari=kdvDahilDeger-kdvHaricDeger
            
            if odemeTipi=="nakit":
                if kasaHesabi-kdvDahilDeger<0:
                    print ("********************************************************************************\n*****************Bakiye yetersiz oldugu icin islem iptal edildi.*****************\n************************************************************************************")
                    break
                else:
                    kasaHesabi-=kdvDahilDeger
                    ticariMallar+=kdvHaricDeger
                    indKDV+=kdvTutari
                
                print ("-----------------------------------------------------------------------------------------------------------------------------------\n### Muhasebe Kaydi Asagidaki Gibidir. ###\nBorc Degeri\n153 Ticari Mallar    ",kdvHaricDeger,"TL","\n191 Indirilecek KDV    ",kdvTutari,"\n                    Alacak Degeri","\n                    100 Kasa    ",kdvDahilDeger,"TL")
                print ("Muhasebe kaydi gerceklestirilmistir.")
            
            elif odemeTipi=="banka":
                if bankaHesabi-kdvDahilDeger<0:
                    print ("********************************************************************************\n*****************Bakiye yetersiz oldugu icin islem iptal edildi.*****************\n************************************************************************************")
                    break
                else:
                    bankaHesabi-=kdvDahilDeger
                    ticariMallar+=kdvHaricDeger
                    indKDV+=kdvTutari
                
                print ("-----------------------------------------------------------------------------------------------------------------------------------\n### Muhasebe Kaydi Asagidaki Gibidir. ###\nBorc Degeri\n153 Ticari Mallar    ",kdvHaricDeger,"TL","\n191 Indirilecek KDV    ",kdvTutari,"\n                    Alacak Degeri","\n                    102 Bankalar    ",kdvDahilDeger,"TL")
                print ("Muhasebe kaydi gerceklestirilmistir.")
            
            elif odemeTipi=="cek":
                    verilenCekler+=kdvDahilDeger
                    ticariMallar+=kdvHaricDeger
                    indKDV+=kdvTutari
                
                    print ("-----------------------------------------------------------------------------------------------------------------------------------\n### Muhasebe Kaydi Asagidaki Gibidir. ###\nBorc Degeri\n153 Ticari Mallar    ",kdvHaricDeger,"TL","\n191 Indirilecek KDV    ",kdvTutari,"\n                    Alacak Degeri","\n                    103 Verilen Cekler ve Odeme Emirleri    ",kdvDahilDeger,"TL")
                    print ("Muhasebe kaydi gerceklestirilmistir.")
                
            elif odemeTipi=="senet":
                    borcSenetleri+=kdvDahilDeger
                    ticariMallar+=kdvHaricDeger
                    indKDV+=kdvTutari
                
                    print ("-----------------------------------------------------------------------------------------------------------------------------------\n### Muhasebe Kaydi Asagidaki Gibidir. ###\nBorc Degeri\n153 Ticari Mallar    ",kdvHaricDeger,"TL","\n191 Indirilecek KDV    ",kdvTutari,"\n                    Alacak Degeri","\n                    321 Borc Senetleri    ",kdvDahilDeger,"TL")
                    print ("Muhasebe kaydi gerceklestirilmistir.")
            elif odemeTipi=="veresiye":
                    saticilarHesabi+=kdvDahilDeger
                    ticariMallar+=kdvHaricDeger
                    indKDV+=kdvTutari
                    print ("-----------------------------------------------------------------------------------------------------------------------------------\n### Muhasebe Kaydi Asagidaki Gibidir. ###\nBorc Degeri\n153 Ticari Mallar    ",kdvHaricDeger,"TL","\n191 Indirilecek KDV    ",kdvTutari,"\n                    Alacak Degeri","\n                    320 Saticilar    ",kdvDahilDeger,"TL")
                    print ("Muhasebe kaydi gerceklestirilmistir.")
            
            elif odemeTipi=="bitcoin":
                if digerStoklar-kdvDahilDeger<0 or bitcoinCuzdani<(kdvDahilDeger/anlikBTCdegeri) :
                    print ("********************************************************************************\n*****************Bakiye yetersiz oldugu icin islem iptal edildi.*****************\n************************************************************************************")
                    break    
                else:
                    digerStoklar-=kdvDahilDeger
                    btcHesaplama=(kdvDahilDeger/anlikBTCdegeri)
                    bitcoinCuzdani-=btcHesaplama
                    ticariMallar+=kdvHaricDeger
                    indKDV+=kdvTutari
                
                print ("-----------------------------------------------------------------------------------------------------------------------------------\n### Muhasebe Kaydi Asagidaki Gibidir. ###\nBorc Degeri\n153 Ticari Mallar    ",kdvHaricDeger,"TL","\n191 Indirilecek KDV    ",kdvTutari,"\n                    Alacak Degeri","\n                    157 Diger Stoklar    ",kdvDahilDeger,"TL")
                print ("Muhasebe kaydi gerceklestirilmistir.")
                print ("Bitcoin cuzdaninizdan:",(btcHesaplama),"BTC cekilmistir.")
            else:
                print ("Hatali giris yapildi.")
                continue
                pass
            
            #STOGA EKLENIS.   
            if urunTipi=="kalem":
                kalem+=adetBilgisi
            elif urunTipi=="silgi":
                silgi+=adetBilgisi
            elif urunTipi=="defter":
                defter+=adetBilgisi
            elif urunTipi=="dosya":
                dosya+=adetBilgisi
            else:
                break
            
            break
        
            
    def rapor():
        global yurticiSatislar
        print ("-----------------------------------------------------------------------------------------------------------------------------------\n#  #  #  #   R A P O R    #  #  #  #")
        print ("\nStoklar.....: Kalem:",kalem,"Silgi:",silgi,"Defter:",defter,"Dosya:",dosya)
        print ("\n**** MUHASEBE HESAPLARI RAPORU ****")
        print ("100 Kasa:",kasaHesabi,"TL","\n102 Bankalar: ",bankaHesabi,"TL","\n101 Alinan Cekler:",alinanCekler,"TL","\n103 Verilen Cekler",verilenCekler,"TL","\n121 Alacak Senetleri:",alacakSenetHesabi,"TL","\n120 Alicilar:",alicilarHesabi,"TL","\n157 Diger Stoklar:",digerStoklar,"TL","\nBitcoin Cuzdani:",bitcoinCuzdani,"BTC","\n600 Yurtici Satislar:",yurticiSatislar,"TL")

        print ("391 Hesaplanan KDV:",hesKDV,"TL","\n153 Ticari Mallar:",ticariMallar,"TL","\n191 Indirilecek KDV",indKDV,"TL","\n321 Borc Senetleri:",borcSenetleri,"TL","\n320 Saticilar:",saticilarHesabi,"TL")        
    
    def paraYatir():
        global kasaHesabi
        global bankaHesabi
        while True:
            
            hangiHesap=str(input("-----------------------------------------------------------------------------------------------------------------------------------\nHangi hesaba para yatirmak istiyorsunuz?\n\nKasaya para yatirmak icin : nakit\nBankaya para yatirmak icin : banka\n\nGiris yapiniz:"))
            secenekler=["nakit","banka","cek","senet","veresiye","bitcoin"]
            try:
                neKadar=float(input("-----------------------------------------------------------------------------------------------------------------------------------\nNe kadar yatirmak istiyorsunuz?"))
                pass
            except(ValueError):
                print ("Hatali giris yaptiniz.")
                continue
            if hangiHesap not in secenekler:
                print ("Hatali giris yaptiniz, lutfen girisinizi kontrol ediniz.")
                continue
            else:
                if hangiHesap=="nakit":
                    kasaHesabi+=neKadar
                    break
                elif hangiHesap=="banka":
                    bankaHesabi+=neKadar
                    break
                else:
                    print ("Hatali giris yaptiniz.")
    def paraCek():
        global kasaHesabi
        global bankaHesabi
        while True:
            hangiHesap=str(input("-----------------------------------------------------------------------------------------------------------------------------------\nHangi hesaptan para cekmek istiyorsunuz?\n\nKasaya para cekmek icin : nakit\nBankadan para cekmek icin : banka\n\nGiris yapiniz:"))
            secenekler=["nakit","banka","cek","senet","veresiye","bitcoin"]
            try:
                neKadar=float(input("-----------------------------------------------------------------------------------------------------------------------------------\nNe kadar cekmek istiyorsunuz?"))
                pass
            except(ValueError):
                print ("Hatali giris yaptiniz.")
                continue
            if hangiHesap not in secenekler:
                print ("Hatali giris yaptiniz, lutfen girisinizi kontrol ediniz.")
                continue
            else:
                if hangiHesap=="nakit":
                    if kasaHesabi>neKadar:
                        kasaHesabi-=neKadar
                        break
                    else:
                        print ("------------------------------------------------------------------\n*********  Hesapta yeterli bakiye yok.************")
                        break
                elif hangiHesap=="banka":
                    if bankaHesabi>neKadar:
                        bankaHesabi-=neKadar
                        break            
                    else:
                        print ("------------------------------------------------------------------\n*********  Hesapta yeterli bakiye yok.************")
                        break
                else:
                    print ("Hatali giris yaptiniz.")
                    
    girisKontrol=["kapat","satis","alis","rapor","para yatir","para cek"]
    if giris not in girisKontrol:
        print ("\n\n*************************************************************************\n***************  Lutfen gecerli bir giris yapiniz. **********************")
        continue
    else:
        pass
    if giris=="satis":          
        satis()
    elif giris=="alis":
        alis()
    elif giris=="rapor":
        rapor()
    elif giris=="kapat":
        break
    elif giris=="para yatir":
        paraYatir()
    elif giris=="para cek":
        paraCek()
    else:
        print ("Hatali giris yaptiniz.")
        continue