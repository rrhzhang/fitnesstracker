condition = "y"
while condition == "y":
    choice = input("""What would you to calculate?
        Water intake (1)
        Protein intake (2)
        Calorie intake (3) 
    """)

    if choice == "1":
        weight = int(input("How much do you weigh (lbs)? "))
        exer_time = int(input("How much time do you plan to exercise (min)? "))
        water = (weight * 0.5) + (exer_time/30.0 * 12)
        print("You should drink " + str(water) + " oz. of water daily.")
    elif choice == "2":
        protein = 0
        weight = int(input("How much do you weigh (lbs)? "))
        p_choice = input("""Do you wish to:
            Maintain muscle (1)
            Gain muscle (2)
            Lose fat? (3)
        """)
        if p_choice == "1":
            print("You should take " + str(weight*0.64) + "-" + str(weight*0.91) + " grams of protein daily.")
        elif p_choice == "2":
            print("You should take " + str(weight*0.73) + "-" + str(weight*1.10) + " grams of protein daily.")
        else:
            print("You should take " + str(weight*0.73) + "-" + str(weight*1.10) + " grams of protein daily.")
    else:
        gender = input("What is your assigned gender at birth (m/f)? ")
        weight = int(input("How much do you weigh (lbs)? "))
        height = int(input("How tall are you (cm)? "))
        age = int(input("How old are you (years)? "))
        bmr = 0
        if gender == "m":
            bmr = (10 * weight/2.2) + (6.25 * height) - (5 * age) + 5
        else:
            bmr = (10 * weight/2.2) + (6.25 * height) - (5 * age) - 161
        amr = bmr * 1.5
        print("You need to consume " + str(amr) + " calories daily in order to maintain your current weight.")
    condition = input("Do you want to calculate another thing (y/n)? ")


    
        


