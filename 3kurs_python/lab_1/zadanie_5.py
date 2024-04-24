price_rub = int(input("Стоимость пирожка (рубли): "))
price_kop = int(input("Стоимость пирожка (копейки): "))
quantity = int(input("Сколько пирожков: "))
total_rub = price_rub * quantity + (price_kop * quantity) // 100
total_kop = (price_kop * quantity) % 100
print(f"К оплате: {total_rub} руб. {total_kop} коп.")