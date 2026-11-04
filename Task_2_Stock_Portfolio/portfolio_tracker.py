import csv
import os
print("===================================")
print("    STOCK PORTFOLIO TRACKER    ")
print("===================================")
while True:
    stock = input("Enter stock symbol: ").strip().upper()

    if stock.isalpha():
        break

    print("Please enter a valid stock symbol!")

while True:
    try:
        quantity = int(input("Enter quantity: "))
        if quantity > 0:
            break
        print("Quantity must be greater than zero!")
    except ValueError:
        print("Please enter a valid whole number!")

while True:
    try:
        buy_price = float(input("Enter buy price: "))
        if buy_price > 0:
            break
        print("Buy price must be greater than zero!")
    except ValueError:
        print("Please enter a valid price!")

while True:
    try:
        current_price = float(input("Enter current price: "))
        if current_price > 0:
            break
        print("Current price must be greater than zero!")
    except ValueError:
        print("Please enter a valid price!")

investment = quantity * buy_price
current_value = quantity * current_price
profit_loss = current_value - investment
print("\n============= PORTFOLIO SUMMARY =================")
print("Stock Symbol:", stock)
print("Quantity:", quantity)
print("Total Investment:", investment)
print("Current Value:", current_value)
print("Profit/Loss:", profit_loss)
if profit_loss > 0:
    print("Status: PROFIT")
elif profit_loss < 0:
    print("Status: LOSS")
else:
    print("Status: NO PROFIT, NO LOSS")
csv_path = os.path.join(os.path.dirname(__file__), "portfolio.csv")

file_exists = os.path.isfile(csv_path)

with open(csv_path, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(["Stock", "Quantity", "Buy Price",
                         "Current Price", "Investment",
                         "Current Value", "Profit/Loss"])

    writer.writerow([stock, quantity, buy_price,
                     current_price, investment,
                     current_value, profit_loss])

print("Portfolio data saved successfully!")
print("\n========== SAVED PORTFOLIO RECORDS ==========")

with open(csv_path, "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(" | ".join(row))