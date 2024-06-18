def main():
   ...:     # Constants
   ...:     COFFEE_PRICE = 5.00
   ...:     MUFFIN_PRICE = 4.00
   ...:     TAX_RATE = 0.06
   ...:
   ...:     # Input number of coffees and muffins
   ...:     print("***************************************")
   ...:     print("My Coffee and Muffin Shop")
   ...:     num_coffees = int(input("Number of coffees bought?\n"))
   ...:     num_muffins = int(input("Number of muffins bought?\n"))
   ...:     print("***************************************")
   ...:
   ...:     # Calculate subtotal, tax, and total
   ...:     subtotal = (num_coffees * COFFEE_PRICE) + (num_muffins * MUFFIN_PRICE)
   ...:     tax = subtotal * TAX_RATE
   ...:     total = subtotal + tax
   ...:
   ...:     # Print receipt
   ...:     print("***************************************")
   ...:     print("My Coffee and Muffin Shop Receipt")
   ...:     print(f"{num_coffees} Coffee at ${COFFEE_PRICE:.2f} each: ${num_coffees * COFFEE_PRICE:.2
   ...: f}")
   ...:     print(f"{num_muffins} Muffins at ${MUFFIN_PRICE:.2f} each: ${num_muffins * MUFFIN_PRICE:.
   ...: 2f}")
   ...:     print(f"{(TAX_RATE * 100):.0f}% tax: ${tax:.2f}")
   ...:     print("---------")
   ...:     print(f"Total: ${total:.2f}")
   ...:     print("***************************************")
   ...:
   ...: if __name__ == "__main__":
   ...:     main()
