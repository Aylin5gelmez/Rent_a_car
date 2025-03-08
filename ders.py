"""renkler =["yeşil","sarı","turuncu","kırmızı","mavi"]
for renk in renkler:
    print(renk)"""
    
"""gelirler =[2000,3000,4000,8000,7500]
for gelir in gelirler:
    print(gelir*2)"""
    
   # Parametre ve Argüman Farkı:
#Parametre: Fonksiyon tanımlanırken kullanılan değişkenlerdir.
#Argüman: Fonksiyon çağrılırken parametrelere verilen gerçek değerlerdir.
    #FONKSİYONLAR
"""def kare_al(x):  #programa istenen işlemi bir kere tanımlayıp gerekli yerlerde hızlıca yapabilmemizi sağlar.
    print(x**2)  # Bu satır ekrana sonucu yazdırıyor ama bir değer döndürmüyor
kare_al(7)

def alan(r,pi=3.14):
 print(pi*r**2)
alan(4)
print("Aylin","Gelmez",sep="15",end="\n")
 """
"""def alan(r,pi=3.14):
    return pi*r**2
alan1=alan(5)
alan2=alan(8)
print(alan1+alan2)

def cift_mi(x):
 if x%2==0:
     print("Bu sayı çifttir.")"""
#Nesne Tabanlı Programlama
"""class Ogrenci:
     isim="mehmet"
     soyisim="Tek"
     yaş=17
     not_ort=85

bir=Ogrenci()
print(bir.isim)"""

#Initializer or Constructor

#__init__() bir fonksiyondur

class Ogrenci():
    def __init__(self,isim,soyisim,yaş,not_ort):
     self.isim=isim
     self.soyisim=soyisim
     self.yaş=yaş
     self.not_ort=not_ort    

bir=Ogrenci("Mehmet","Tek",18,85)
ikinci=Ogrenci("Aylin","Gelmez",18,95)
