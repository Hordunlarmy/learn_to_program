investment, interest = input("Enter your \
investment amount and expected interest: ").split()
investment, interest = float(investment), float(interest)
interest /= 100

for i in range(1, 11):
    investment += investment * interest
    print(f"Your {i} year earnings will be {investment:.2f}")
