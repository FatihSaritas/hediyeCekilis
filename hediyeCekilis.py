import random


isimler =['fatih','ali','nida',
          'songül','ayşegül','süleyman']

def hediye_cekilisi():
    
    alanlar = isimler.copy()
    verenler = isimler.copy()
    
    while len(alanlar) > 0 :                                
        
        alici_indeks = random.randint(0,len(alanlar) -1 )
        verici_indeks = random.randint(0,len(verenler) -1)
        
        
        while alanlar[alici_indeks] == verenler[verici_indeks]:   #While yaptıgımız zmaan aynı kişi gelecegi anda tekrar döngüyü çalıştır demiş oluruz ve ayni kişileri vermez bize
            alici_indeks = random.randint(0,len(alanlar) -1 )
            verici_indeks = random.randint(0,len(verenler) -1)
            
            
        
        
        print(alanlar[alici_indeks],'Şu kişiye hediye alıcak: ',verenler[verici_indeks])
        
        del alanlar[alici_indeks]
        del verenler[verici_indeks]

    #verenler.remove(verenler[verici_indeks]) bu del verenler ile aynı anlamı ifade etmektedir.
    
    
    
hediye_cekilisi()    
     
     

'''
isimler: Bir liste oluşturuyorsunuz, 
içerisinde kişilerin isimlerini içeriyor.

hediye_cekilisi(): 
Hediye çekilişi işlemini gerçekleştiren bir fonksiyon tanımlıyorsunuz.

alanlar ve verenler: İki ayrı liste oluşturuyorsunuz. 
İlk başta her iki liste de isimler listesini kopyalıyor.

while len(alanlar) > 0:: Alanlar listesi boş olana kadar bir çekiliş döngüsü başlatıyorsunuz.

alici_indeks ve verici_indeks: Rastgele indeksler seçiyorsunuz. Bu indeksler, alanlar ve verenler listelerinde rastgele kişileri belirtir.

while alanlar[alici_indeks] == verenler[verici_indeks]:: Eğer aynı kişi kendisine hediye alacaksa, yeni rastgele indeksler seçiyorsunuz.
Bu durumda aynı kişiye hediye alınmamasını sağlıyorsunuz.

print(alanlar[alici_indeks],'Şu kişiye hediye alıcak: ',verenler[verici_indeks]): Çekiliş sonucunu ekrana basıyorsunuz.

del alanlar[alici_indeks] ve del verenler[verici_indeks]: Çekilen kişileri listelerden siliyorsunuz, 
çünkü aynı kişiye birden fazla hediye vermemek için.





'''     