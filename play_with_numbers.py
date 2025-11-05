'''
Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.

Find e to the Nth Digit - Just like the previous problem, but with e instead of π (pi). Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.

Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence till that number

Prime Factorization - Have the user enter a number and find all unique Prime Factors (if there are any) and display them.

Next Prime Number - Have the program find next prime number of the entered number.
'''
import math

def find_n_digits_of_pi(num):
    print(f'Value of pi till {num}th decimal point is: {math.pi:.{num}f}')

def find_n_digits_of_e(num):
    print(f'Value of e till {num}th decimal point is: {math.e:.{num}f}')

def fibonacci_series(num):
    a, b = 0, 1
    print(a, b, end=' ')
    for _ in range(2, num):
        a, b = b, a + b
        print(b, end=' ')
    print()  # for clean line break

def prime_factors(num):
    factors = set()
    while num % 2 == 0:
        factors.add(2)
        num //= 2
    for i in range(3, int(num**0.5) + 1, 2):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 2:
        factors.add(num)
    print(f'Prime factors: {sorted(factors)}')

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def next_prime_number(num):
    nextprime = num + 1
    while not is_prime(nextprime):
        nextprime += 1
    print(f'Next prime number after {num} is {nextprime}')

def choiceLogic():
    seperator = "\n#########################################\n"
    print(f"{seperator}Let's Play with Numbers!{seperator}")
    while True:
        inp = input("Choose an option:\n1. find_n_digits_of_pi\n2. find_n_digits_of_e\n3. fibonacci_series\n4. prime_factors_of_a_number\n5. next_prime_number\nYour choice: ")
        if inp.isdigit() and int(inp) in range(1, 6):
            inp = int(inp)
            break
        print("Invalid choice. Please select a number between 1 and 5.")

    while True:
        number = input("Enter a number (For options 1 or 2, enter 0–15): ")
        if number.isdigit():
            number = int(number)
            if inp in [1, 2] and 0 <= number <= 15:
                print(f'{seperator}')
                if inp == 1:
                    print(f'Finding value of pi till {number}th decimal point!')
                    find_n_digits_of_pi(number)
                else:
                    print(f'Finding value of e till {number}th decimal point!')
                    find_n_digits_of_e(number)
                print(seperator)
                break
            elif inp == 3:
                print(f'{seperator}Fibonacci Series of {number} terms:')
                fibonacci_series(number)
                print(seperator)
                break
            elif inp == 4:
                print(f'{seperator}Prime factors of {number}:')
                prime_factors(number)
                print(seperator)
                break
            elif inp == 5:
                print(f'{seperator}')
                next_prime_number(number)
                print(seperator)
                break
            else:
                print("For options 1 and 2, please choose a number between 0 and 15.")
        else:
            print("Please enter a valid number.")

# Main loop
while True:
    choiceLogic()
    cont = input('Do you want to continue? (y/n): ')
    if cont.lower() != 'y':
        print("Goodbye!")
        break
