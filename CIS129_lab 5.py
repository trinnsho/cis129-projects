# Trinity Showalter, June 24 2024, Bottle Return Program code
# Calculating total bottles, total payout, and prinitng info
#  Lab 5 The Bottle Return Program
# Step 1: Declare variables below
keepGoing='y'
total_bottles=0
counter=1
today_bottles=0
total_payout=0
get_bottles=0
calcPayout=0
print_info=0
# Step 2: Loop to run program again
while keepGoing.lower() == "y":
    total_bottles=0
    counter=1
    while counter <=7:
        today_bottles = int(input(f"Enter number of bottles collected for day {counter}:"))
        total_bottles += today_bottles
        counter += 1
    total_payout = total_bottles*0.10
    print(f"Total number of bottles collected: {total_bottles}")
    print(f"Total payout: ${total_payout:.2f}")
    keepGoing = input("Do you have more data to enter? (y/n): ")
