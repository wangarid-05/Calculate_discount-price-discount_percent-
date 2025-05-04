def calculate_discount(price, discount_percent):
    """
    Returns the price after applying discount if discount is 20% or more.
    Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

# Get user input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: ${final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
