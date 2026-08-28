# CodeAlpha Internship
# Task 2 - Stock Portfolio Tracker

# Stock names and their prices
stock_prices = {
    "TCS": 3500,
    "INFY": 1600,
    "RELIANCE": 2900,
    "HDFC": 1700,
    "WIPRO": 550,
    "ITC": 480
}

# Store purchased stocks
portfolio = {}

print("======================================")
print("        STOCK PORTFOLIO TRACKER")
print("======================================")

print("\nAvailable Stocks:")
print("--------------------------------------")

for stock, price in stock_prices.items():
    print(stock, "-> ₹", price)

print("--------------------------------------")

# Ask user how many different stocks they want
while True:
    try:
        number_of_stocks = int(input("\nHow many stocks do you want to add? "))

        if number_of_stocks <= 0:
            print("Please enter a number greater than 0.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")

# Take stock details
for count in range(number_of_stocks):

    while True:
        stock_name = input(
            "\nEnter stock name "
            "(TCS/INFY/RELIANCE/HDFC/WIPRO/ITC): "
        ).upper().strip()

        if stock_name in stock_prices:
            break

        print("Stock not found. Please choose from the available stocks.")

    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid quantity.")

    # Calculate investment value
    investment = stock_prices[stock_name] * quantity

    # Save stock information
    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity

    print(
        stock_name,
        "added successfully.",
        "Investment value: ₹",
        investment
    )


# Calculate total portfolio value
total_value = 0

print("\n\n======================================")
print("          PORTFOLIO SUMMARY")
print("======================================")

print(
    "{:<12} {:<12} {:<15}".format(
        "Stock", "Quantity", "Value"
    )
)

print("--------------------------------------")

for stock, quantity in portfolio.items():

    value = stock_prices[stock] * quantity
    total_value += value

    print(
        "{:<12} {:<12} ₹{:<15}".format(
            stock,
            quantity,
            value
        )
    )

print("--------------------------------------")
print("Total Portfolio Value: ₹", total_value)
print("======================================")