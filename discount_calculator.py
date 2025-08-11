# create a function that calculate discount price.

def calculate_discount(price: int, discount_percent: float):
    """
    calculate the discount price based on the original price and discount percentage.

    parameters:
    price (int): The original price of the item.
    discount_percent (float): The dicount precentage to apply.

    returns:
    float: The price after applying the discount.

    """
    if discount_percent >= 0.2:
        amount_paid = price * (1 - discount_percent)
        return f"Price after a {discount_percent * 100}% discount is: {amount_paid:.2f}"
    else:
        return f"Discount percentage {discount_percent * 100}% is too low, no discount applied. Price remains: {price}"
    
if __name__ == "__main__":
    while True:
        try:
            price = int(input("Enter the original price of the item: "))
            diccount_percent = float(input("Enter the discount percentage (as a decimal): "))
            result = calculate_discount(price, diccount_percent)
            print(result)
            
        except ValueError:
            print("Invalid input. Please enter numeric values for price and discount percentage.")

        done = input("Do you want to calculate another discount? (yes/no): ").strip().lower()
        if done != 'yes':
            print("Exiting the discount calculator.")
            break


