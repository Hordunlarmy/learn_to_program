print("....COMPOUND INTEREST CALCULATOR....\n")

investment = eval(input("Enter your investment: "))
interest = eval(input("Enter your expected interest: "))
year = eval(input("Enter year: "))
print("\n")

if (type(interest) == int):
    interest = float(interest) * 0.01

# interest = float(interest) * 0.01
investment = float(investment)
earnings = investment + (investment * interest)

print(f"Earnings after 1 year : {earnings:.2f}")
for i in range(2, (year + 1)):
    earnings += earnings * interest
    print(f"Earnings after {i} years : {earnings:.2f}")
