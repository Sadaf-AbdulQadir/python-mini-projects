'''
Inputs:
Principal (P) — total loan amount
Annual Interest Rate (r) — in percentage
Loan Term (years) — number of years (N)
Compounding frequency — one of:
    Monthly → 12 times/year
    Weekly → 52 times/year
    Daily → 365 times/year
'''

def get_positive_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print("Invalid Input. Should be grater than zero.")
            else:
                break
        except ValueError:
            print('Select a positive floating point number')
    return val

def mortgage_calculator():
    print('\n***************************  Mortgage Calculator for regular compounding  ***************************\n')
    Principal = get_positive_float('Enter total loan amount: ')
    annual_rate = get_positive_float('Enter Annual Interest rate (in %): ')
    years = get_positive_float('Enter the Loan Term (in years)')
    print("\nSelect compounding interval:")
    print("1. Monthly\n2. Weekly\n3. Daily")
    while True:
        choice = input("Enter your choice (1-3): ")
        if choice in ['1', '2', '3']:
            break
        print("Invalid choice. Please select 1–3.")

    if choice == '1':
        compounds_per_year = 12
        label = "Monthly"
    elif choice == '2':
        compounds_per_year = 52
        label = "Weekly"
    else:
        compounds_per_year = 365
        label = "Daily"

    print(f"\n--- {label} Compounding Selected ---\n\n")
    r = (annual_rate/100)/compounds_per_year
    n = years * compounds_per_year
    interest_rate_power_n = (1+r)**n
    periodic_payment = Principal * (r * (1 + r) ** n )/((1 + r) ** n -1)
    total_payment = periodic_payment * n
    total_interest = total_payment - Principal
    print('Loan Details:')
    print(f'Principal amount : {Principal:,.2f} INR')
    print(f'Annual Interest Rate : {annual_rate:,.2f}% per annum')
    print(f'Loan Term : {years} years ({int(n)} payments)')
    print(f'Compounding interval : {label}\n')
    print(f'Periodic payment : {periodic_payment:,.2f}')
    print(f'Total payment : {total_payment:,.2f}')
    print(f'Total interest : {total_interest:,.2f}')

mortgage_calculator()