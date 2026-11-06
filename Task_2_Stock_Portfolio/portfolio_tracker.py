import csv
import os
import yfinance as yf

print("===================================")
print("    STOCK PORTFOLIO TRACKER")
print("===================================")

portfolio = {}

while True:
    stock = input("Enter stock symbol (or DONE to finish): ").strip().upper()

    if stock == "DONE":
        break

    if not stock.isalpha():
       print("Please enter a valid stock symbol!")
       continue

    if stock in portfolio:
        print("Stock already added!")
        continue

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

    portfolio[stock] = {
        "quantity": quantity,
        "buy_price": buy_price
    }

if not portfolio:
    print("No stocks were added!")
    exit()

total_investment = 0
total_current_value = 0
csv_rows = []

for stock, details in portfolio.items():

    try:
        data = yf.Ticker(stock).history(period="1d")

        if data.empty:
            print("Price unavailable for", stock)
            continue

        current_price = data["Close"].iloc[-1]

        quantity = details["quantity"]
        buy_price = details["buy_price"]

        investment = quantity * buy_price
        current_value = quantity * current_price
        profit_loss = current_value - investment

        percentage = (profit_loss / investment) * 100

        total_investment += investment
        total_current_value += current_value
        csv_rows.append([
             stock, quantity, buy_price, current_price,
            investment, current_value, profit_loss, percentage
        ])

        print("\nStock:", stock)
        print("Quantity:", quantity)
        print("Buy Price:", buy_price)
        print("Latest Available Close:", round(current_price, 2))
        print("Investment:", round(investment, 2))
        print("Current Value:", round(current_value, 2))
        print("Profit/Loss:", round(profit_loss, 2))
        print("Profit/Loss Percentage:", round(percentage, 2), "%")

    except Exception as error:
        print("Unable to retrieve price for", stock)
        print("Reason:", error)

print("\n========== TOTAL PORTFOLIO SUMMARY ==========")

total_profit_loss = total_current_value - total_investment

if total_investment > 0:
    total_percentage = (total_profit_loss / total_investment) * 100
else:
    total_percentage = 0

print("Total Investment:", round(total_investment, 2))
print("Total Current Value:", round(total_current_value, 2))
print("Total Profit/Loss:", round(total_profit_loss, 2))
print("Total Return:", round(total_percentage, 2), "%")
csv_path = os.path.join(
    os.path.dirname(__file__),
    "portfolio_summary.csv"
)

with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Stock", "Quantity", "Buy Price",
        "Current Price", "Investment",
        "Current Value", "Profit/Loss",
        "Profit/Loss Percentage"
    ])

    writer.writerows(csv_rows)

    writer.writerow([
        "TOTAL", "", "", "",
        total_investment,
        total_current_value,
        total_profit_loss,
        total_percentage
    ])

print("\nPortfolio saved successfully!")
print("File location:", csv_path)