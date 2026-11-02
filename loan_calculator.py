total_debt = float(input("Enter your total debt amount: "))
annual_interest_rate = float(input("Enter your annual interest rate (as a percentage): "))
monthly_payment = float(input("Enter your monthly payment amount: "))
number_of_months = int(input("Enter the number of months you plan to make payments: "))

monthly_interest_rate = annual_interest_rate / 100 / 12

for month in range(number_of_months):
    # Calculate interest generated for the current month
    interest_generated = total_debt * monthly_interest_rate
    # Update total debt by adding the generated interest
    total_debt = total_debt + interest_generated

    # Check if the total debt has been paid off
    if total_debt < 0:

        extra_balance = abs(total_debt)
        print("Congratulations! You have paid off your debt.")
        print(f"Extra balance: ${extra_balance:.2f}")
        break

# Subtract the monthly payment from the total debt
    total_debt -= monthly_payment
    print(f"Total debt after payment: ${total_debt:.2f}")