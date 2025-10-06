# !/usr/bin/env python3

# starting variable amounts
bill = 0.0
tip_pct = 0.0
tip_amount = 0.0
total_with_tip = 0.0
per_person = 0.0
people = 0

# Introduction
print(" Bill Buddy - Your Very Own Bill Splitter")
print("--------------------------------------------")

name = input("Hi there and welcome to Bill Buddy! I am Bill, your dining assistant. What's your name? ")
print("--------------------------------------------")
print("Hi " + name + ", let's get started!")
print("                                            ")

# getting the bill total
def get_bill_total():
    while True:
        try:
            bill_total = float(input("Please enter the total bill amount: $"))
        except ValueError:
            print("Oops, please enter a number like 123.45")
            continue

        if bill_total >= 0.01:
            print(f"Your total bill amount is set to: ${bill_total:.2f}")
            return bill_total
        else:
            print(f"Please enter an amount of at least $0.01")

# getting tip percentage
def get_tip_percentage():
    while True:
        try:
            tip = float(input("How much would you like to tip (ex. 15 for 15%): "))
        except ValueError:
            print("Sorry, that's an invalid input! Try to enter a whole number or decimal (ex. 15 or 18.5)")
            continue

        if 0 <= tip <= 100:
            print(f"Tip percentage set to: {tip:.2f}%")
            return tip
        else:
            print("Please enter a percentage between 0 and 100")

# getting number of people
def get_num_people():
    while True:
        try:
            num_people = int(input("How many people are splitting the bill?: "))
        except ValueError:
            print("Please enter a whole number (like 2)")
            continue

        if num_people < 1:
            print("Please enter a whole number greater than 0.")
            continue
        if num_people == 1:
            print("The bill will not be split and I will leave. Bye, enjoy your meal!")
            quit() # exit program if only one person
        print(f"Your bill will be split among {num_people} people.")
        return num_people
# calculations
def main():
    bill = get_bill_total()
    tip_pct = get_tip_percentage()
    people = get_num_people()

    tip_amount = bill * (tip_pct / 100.0)
    total_with_tip = bill + tip_amount
    per_person = total_with_tip / people

    # final output
    print("                                            ")
    print("-------------Overall Meal Split-------------")
    print(f"Bill: ${bill:.2f}")
    print(f"Tip Amount: ({tip_pct:.2f}%): ${tip_amount:.2f}")
    print(f"Each person pays: ${per_person:.2f}")
    print("--------------------------------------------")


if __name__ == "__main__":
    main()


