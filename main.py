#Trying the input user function - creating a calculator

user_select_1 = input("Pick the first number: ")
user_select_2 = input("Pick the second number: ")


choice = input("Enter your choice (1/2/3/4): ")

# Step 3: Do the calculation based on the user's choice
if choice == "1":
    result = float(user_select_1) + float(user_select_2)
    print("Result:", result)
elif choice == "2":
    result = float(user_select_1) - float(user_select_2)
    print("Result:", result)
elif choice == "3":
    result = float(user_select_1) * float(user_select_2)
    print("Result:", result)
elif choice == "4":
    if float(user_select_2) != 0:
        result = float(user_select_1) / float(user_select_2)
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid choice.")