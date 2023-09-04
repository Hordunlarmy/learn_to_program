age = eval(input("Enter age: "))

if (age < 5):
    print("Too young for school")
elif (age == 5):
    print("Go to Kindergarten")
elif (age >= 6) and (age <= 17):
    grade = age - 5
    print(f"goes to grade {grade}")
elif (age > 17):
    print("Go to college")
