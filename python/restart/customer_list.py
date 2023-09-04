customer_list = []

while (True):
    option = input("Enter Customer??(Yes, No): ")
    option = option.upper()

    if (option == "Y") or (option == "YES"):
        first_name, last_name = input("Enter Customer Name: ").split()
        customer_list.append({"firstName": first_name, "lastName": last_name})

    else:
        # print(customer_list)
        break

for name in customer_list:
    print(name["firstName"], name["lastName"])
