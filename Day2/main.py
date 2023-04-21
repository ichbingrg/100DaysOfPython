print("Welcome to tip calculator.")

amount = float(input("What was the total bill amount ? €"))
count_people = int(input("How many people to split the bill ? "))
tip_percent = float(
    input("What percent tip would you like to give? 10,12 or 15 ? "))

total_amount = amount * (1+(tip_percent)/100)
print(total_amount)
billpp = (total_amount/(count_people))

billpp = round(billpp, 2)
print(f"Each person shall pay : €{billpp}")
