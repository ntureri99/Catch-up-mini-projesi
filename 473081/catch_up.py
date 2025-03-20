from pygame import * # kütüphanemiz tüm fonksiyonları bağlandı
#oyun penceresi oluştur
window=display.set_mode((700,500)) #700*500 boyutunda pencere oluşturur ( genişlik,uzunluk)
display.set_caption("Catchup/Yakalamak") #pencerenin başlığını ayarladık
#sahne arka planını ayarla
background= transform.scale(image.load("background.png"),(700,500)) #pencere boyutunda bir görüntü nesnesi oluşturduk

#2 sprite oluştur ve onları sahneye yerleştir
x1=100  # resmin yerleşeceği koordinartlar
y1=300

x2=300
y2=300
#Bir resim nesnesi oluşturun ve onu 100x100 kareye sığdırın.
sprite1= transform.scale(image.load("sprite1.png"),(100,100)) 
sprite2= transform.scale(image.load("sprite2.png"),(100,100))
speed=5  #Bir tuşa basıldığında sprite'5 piksel hareket ettirsin.

game=True
clock = time.Clock()  # Zamanı takip eden bir "saat" nesnesi oluşturun. 
FPS=60 #Hemen bir FPS sabiti oluşturacağız ve istenen kare hızını ayarlayacağız.

while game:
    window.blit(background,(0,0)) #pencerede bir arka plan resmi görüntülemek için
    window.blit(sprite1,(x1,y1))  #Sprite'ı pencerede (x1, y1) noktasına yerleştirin.
    window.blit(sprite2,(x2,y2))
    for e in event.get(): #Gerçekleşen olayların listesini döndürür
        if e.type==QUIT: # çarpıya (kapatma tuşuna) tıklandı mı
            game=False # while False oyun biticek
            
    keys_pressed = key.get_pressed() #Geçerli anahtar durumlarıyla (True — atlanmış, False — yükseltilmiş) bir yapı döndürür.
    # referans noktası sol üst köşe 
    if keys_pressed[K_LEFT] and x1>5:
        x1 -=speed  # speed=5  x1-=5
    if keys_pressed[K_RIGHT] and x1<595:
        x1 +=speed
    if keys_pressed[K_UP] and y1>5:  #Yukarı Ok tuşu basılırsa, Sprite1'in Y koordinatı 10 piksel azaltılır.
        y1 -=speed
    if keys_pressed[K_DOWN] and y1<395:
        y1 +=speed

    if keys_pressed[K_a] and x2>5:
        x2 -=speed
    if keys_pressed[K_d] and x2<595: # beeni resmim 100*100 595+10=695 benim sahnem 700
        x2 +=speed
    if keys_pressed[K_w] and y2>5:
        y2 -=speed
    if keys_pressed[K_s] and y2<395: #S" tuşuna basılırsa ve ekranın alt kısmına ulaşılamazsa, Sprite2'nin Y koordinatını 10 piksel artırın.
        y2 +=speed

    display.update()
    clock.tick(FPS) #Her karede bir saniye 60'a bölünecektir. 1/60 saniyelik bir gecikme olacaktır.
#"Pencereyi kapat" düğmesine tıklayın" olayını ele alın