def greet_customer ():
    print("Welcome to the Lemonade stand!")
    print("Fresh Lemonade, Made just for you.")

def calculate_total(price, cups):
    total = price * cups
    return total

def calculate_change(paid, total):
    change = paid - total
    return change

def thank_you_message(cups):
    if cups >= 5:
        return "Wow, Big order! Thank so much for your support!"
    else:
        return "Thanks for stooping by the stand!"

greet_customer()
price_per_cup = float(input("Enter the price per cup is dollars: "))
cups_sold = int(input("Enter the number of cups sold: "))
total_cost = calculate_total(price_per_cup, cups_sold)
rounded_total = round(total_cost, 2)
print("Total cost:", rounded_total)
amount_paid = float(input("Enter the amount paid by the customer: "))
change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)
closing_message = thank_you_message(cups_sold)
print("")
print("=====LEMONADE STAND RECEIPT======")
print("price per cup:", price_per_cup)
print("cups_sold:", cups_sold)
print("total cost:", rounded_total)
print("Amount_paid:", amount_paid)
print("change_due", rounded_change)
print(closing_message)
print("============================")