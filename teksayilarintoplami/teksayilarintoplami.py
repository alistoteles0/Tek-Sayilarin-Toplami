while True:
    try:
        n = int(input("Lütfen bir tam sayı giriniz: "))
        break
    except ValueError:
        print("Lütfen bir tam sayı giriniz.")
if n>1:
    toplam = 0
    for i in range(1, n+1, 2):
        toplam += i
    print("Çift sayıların toplamı:", toplam)
else:
    print("Lütfen 1'den büyük bir sayı giriniz.")
    




    
