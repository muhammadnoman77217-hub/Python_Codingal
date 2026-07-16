print("=== ATM Cash Dispenser ===")
print("Dispensing cash for customers one at a time. \n")
notes = [100, 50, 20, 10, 5, 1]
customers_served = 0
total_dispensed = 0
log = []    # stores each customer's note breakdown for the daily report

serving = True
while serving:
    name = input("Enter customer name: ")
    amount = int(input("Hello {name}! Enter Withdrawl amount: "))
    if amount <= 0:
        print("Invalid amount. Please Enter a positive number. \n")
        continue
    print(f"\nDispensing {amount} units for {name}: ")
    print("-" * 30)
    remaining = amount
    1 = 0
    used = {}
    while i < len(notes):
        count = remaining  // notes [i]
        if count > 0:
            print(f"    {count}     x       {notes[i]}-unit note(s) = {count * notes[i]}")
            used[notes[i]] = count
            remaining -= count * notes[i]
            i+= 1

customers_served += 1
total_dispensed += amount
log.append( {"name": name, "used": used})
print(f"Transaction Complete! Please collect your Cash, {name}.\n")
again = input("Text customer? (yes / No): ").strip().lower()
if again != "yes":
    serving = False