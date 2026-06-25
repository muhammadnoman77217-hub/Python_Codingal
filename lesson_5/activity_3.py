buy_price = int(input("enter the buy price : "))
sell_price = int(input("enter the price you sold it at : "))

if sell_price>buy_price:
    profit = sell_price - buy_price
    print("you have made a profit of ",profit)
else:
    print("you have incured a loss")