from pizzas import KlasikPizza, TurkPizza, MargheritaPizza, SadePizza, Zeytin, Mantarlar, KeciPeyniri, Et, Sogan, Misir
import csv
import datetime

def print_menu():
    print("*************************************")
    print("*             PİZZA MENÜSÜ          *")
    print("*************************************")
    print("* 1 - Sade Pizza        : 15 TL      *")
    print("* 2 - Klasik Pizza      : 20 TL      *")
    print("* 3 - Margarita Pizza   : 25 TL      *")
    print("* 4 - Türk Pizza        : 30 TL      *")
    print("*                                   *")
    print("* Soslar:                           *")
    print("* 11 - Zeytin           : 3 TL       *")
    print("* 12 - Mantarlar        : 3 TL       *")
    print("* 13 - Keci Peyniri     : 5 TL       *")
    print("* 14 - Et               : 7 TL       *")
    print("* 15 - Soğan            : 2 TL       *")
    print("* 16 - Mısır            : 2 TL       *")
    print("*************************************")

def main():
    print_menu()

    pizza_choice = input("Lütfen pizza seçiminizi yapınız (1-4): ")
    sauce_choice = input("Lütfen sos seçiminizi yapınız (11-16) veya 0 (sos istemiyorum) tuşlayınız: ")

    pizza = None

    if pizza_choice == "1":
        pizza = SadePizza()
    elif pizza_choice == "2":
        pizza = KlasikPizza()
    elif pizza_choice == "3":
        pizza = MargheritaPizza()
    elif pizza_choice == "4":
        pizza = TurkPizza()
    else:
        print("Geçersiz Pizza Seçimi")

    while True:
        if sauce_choice == "11":
            pizza = Zeytin(pizza)
        elif sauce_choice == "12":
            pizza = Mantarlar(pizza)
        elif sauce_choice == "13":
            pizza = KeciPeyniri(pizza)
        elif sauce_choice == "14":
            pizza = Et(pizza)
        elif sauce_choice == "15":
            pizza = Sogan(pizza)
        elif sauce_choice == "16":
            pizza = Misir(pizza)
        elif sauce_choice == "0":
            break
        else:
            print("Geçersiz sos seçimi.")

        sauce_choice = input("Lütfen sos seçiminizi yapınız (11-16) veya 0 (sos istemiyorum) tuşlayınız: ")

    print("Pizza: {}, Fiyat: {} TL".format(pizza.get_description(), pizza.get_cost()))
    accept = input("Siparişinizi Onaylıyormusunuz? 'Evet veya Hayır Yazınız' ").lower()

    if accept =="evet":
        name = input("Adınız: ")
        tc = input("TC Kimlik Numaranız: ")
        cc_number = input("Kredi Kartı Numaranız: ")
        cc_password = input("Kredi Kartı Şifreniz: ")
        print("Siparişiniz hazırlanıyor...")


        with open('Orders_Database.csv', mode='a') as order_file:
            writer = csv.writer(order_file)
            writer.writerow([datetime.datetime.now(), pizza.get_description(), f"{pizza.get_cost()}TL", name, tc, cc_number, cc_password])

if __name__ == "__main__":
    main()