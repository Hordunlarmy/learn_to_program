age = eval(input("Enter Age: "))

if (age < 5):
    print("Too young for school")
elif (age == 5):
    print("Go to Kindergarten")
elif (age >= 6) and (age <= 17):
    grade = age - 5
    print(f"Go to grade {grade}")
else:
    print("Go to College")
