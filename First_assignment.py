state = "yes"
users_list = []

while state.lower() in ["yes", "y"]:
    weight = float(input("Please enter your weight (kg):\n"))
    height = float(input("Please enter your height (m):\n"))

    # BMI calculation
    bmi = weight / (height * height)
    bmi = round(bmi, 2)
    print("Your BMI is {:.2f}".format(bmi))

    # Healthy weight range for this height
    min_weight = 18.5 * (height * height)
    max_weight = 24.9 * (height * height) 

    # Conditions + advice
    if bmi < 18.5:
        category = "Underweight"
        print("You are Underweight")
        gain = min_weight - weight
        print("You need to gain approximately {:.1f} kg to reach a healthy BMI.".format(gain))
    elif bmi < 25:
        category = "Healthy"
        print("You are Healthy")
        print("Great job! You are already within the healthy range.")
    elif bmi < 30:
        category = "Overweight"
        print("You are Overweight")
        lose = weight - max_weight
        print("You need to lose approximately {:.1f} kg to reach a healthy BMI.".format(lose))
    else:
        category = "Obesity"
        print("You have Obesity")
        lose = weight - max_weight
        print("You need to lose approximately {:.1f} kg to reach a healthy BMI.".format(lose))

    # Save user result (BMI + category)
    users_list.append((bmi, category))

    # Show healthy weight range
    print("Healthy weight range for your height: {:.1f} kg – {:.1f} kg".format(min_weight, max_weight))

    # Ask to continue
    state = input("\nDo you want to try again? (yes/no): ")

# Final summary
print("\n📊 Summary of all users:")
for i, (bmi, category) in enumerate(users_list, start=1):
    print(f"User {i}: BMI = {bmi:.2f}, Category = {category}")
