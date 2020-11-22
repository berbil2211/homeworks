

# kullanıcı dışardan sipariş alınacak kitap adeti girecek
# birim fiyatı 5t
# sipariş sayısı : 0 veya altı ise uyarı ver
# sipariş sayısı 1 - 20 (dahil) 5% indirim
# sipariş sayısı 21 - 50 (dahil) 10% indirim
# sipariş sayısı 51 - 80 (dahil) 15% indirim
# sipariş sayısı 81 - 100 (dahil) 20% indirim
# sipariş sayısı 100'den fazla 25% indirim

# işlem sonunda toplam ödenmesi gereken tutar, verilen sipariş adedi, yapılan indiirm oranı gösterilecek

try:

    order = int(input("lütfen sipariş adedini giriniz"))
    pay = order * 5
    result = "iskonto oranınız : {} "
    
    if order <= 0 :
        print("geçersiz adet girdiniz!")
    else:
        if order <= 20:
            result = result.format("5%")
            pay = pay * 0.95
            print("ödemeniz gereken tutar: ₺", pay, "\nsipariş adedi: ", order, "\n",result)
        elif order <= 50:
            result = result.format("10%")
            pay = pay * 0.90
            print("ödemeniz gereken tutar: ₺", pay, "\nsipariş adedi: ", order, "\n",result)
        elif order <= 80:
            result = result.format("15%")
            pay = pay * 0.85
            print("ödemeniz gereken tutar: ₺", pay, "\nsipariş adedi: ", order, "\n",result)
        elif order <=100:
            result = result.format("20%")
            pay = pay * 0.80
            print("ödemeniz gereken tutar: ₺", pay, "\nsipariş adedi: ", order, "\n",result)
        else:
            result = result.format("25%")
            pay = pay * 0.75
            print("ödemeniz gereken tutar: ₺", pay, "\nsipariş adedi: ", order, "\n",result)
except ValueError as error:
    print(error)
