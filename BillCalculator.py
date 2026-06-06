print("Welcome to Bill Calculator..!!")

bill = float(input('What was the total bill? '))
tip = int(input('what percentage tip would you like to give? '))
people = int(input('How many people to split the bill? '))
bill_with_tip = tip/100*bill + bill

split = bill_with_tip/people
print("Each person should pay: ",round(split,2))