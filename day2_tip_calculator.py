print("Welcome to the tip calculator.")

total = float(input("What was the total bill? "))
percentage = int(input("What percentage would you like to give? 10, 12, or 15? "))
pax = int(input("How many people to split the bill? "))

valor = round(((total*(percentage/100)+total)/pax), 2)

print(f"Each person should pay: ${valor}")
