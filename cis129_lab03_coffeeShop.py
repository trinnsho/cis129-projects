def main():
    # Constants
    COFFEE_PRICE = 5.00
    MUFFIN_PRICE = 4.00
    SCONES_PRICE = 2.00
    TEA_PRICE = 4.00
    TAX_RATE = 0.06
    
    # Input number of items
    print("***************************************")
    print("My Coffee and Muffin Shop")
    num_coffees = int(input("Number of coffees bought?\n"))
    num_muffins = int(input("Number of muffins bought?\n"))
    num_scones = int(input("Number of scones bought?\n"))
    num_teas = int(input("Number of teas bought?\n"))
    print("***************************************")
    
    # Calculate subtotal, tax, and total
    subtotal = (num_coffees * COFFEE_PRICE) + (num_muffins * MUFFIN_PRICE) + (num_scones * SCONES_PRICE) + (num_teas * TEA_PRICE)
    tax = subtotal * TAX_RATE
    total = subtotal + tax
    
    # Print receipt
    print("***************************************")
    print("My Coffee and Muffin Shop Receipt")
    print(f"{num_coffees} Coffee at ${COFFEE_PRICE:.2f} each: ${num_coffees * COFFEE_PRICE:.2f}")
    print(f"{num_muffins} Muffins at ${MUFFIN_PRICE:.2f} each: ${num_muffins * MUFFIN_PRICE:.2f}")
    print(f"{num_scones} Scones at ${SCONES_PRICE:.2f} each: ${num_scones * SCONES_PRICE:.2f}")
    print(f"{num_teas} Teas at ${TEA_PRICE:.2f} each: ${num_teas * TEA_PRICE:.2f}")
    print(f"{(TAX_RATE * 100):.0f}% tax: ${tax:.2f}")
    print("---------")
    print(f"Total: ${total:.2f}")
    print("***************************************")
    
    # Thank you message
    print("Thank you for supporting My Coffee and Muffin Shop!")

if __name__ == "__main__":
    main()
