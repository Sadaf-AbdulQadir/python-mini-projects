import math

def find_n_digits_of_pi(num):
    print(f'Value of pi till {num}th decimal point is: {math.pi:.{num}f}')

def find_n_digits_of_e(num):
    print(f'Value of e till {num}th decimal point is: {math.e:.{num}f}')

def fibonacci_series(num):
    a = 0
    b = 1
    next = b
    count = 2
    print(f'{a} {b}', end= ' ')
    while count <= num:
        print(next,end=' ')
        count+=1
        a,b = b, next
        next = a+b

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
    print(factors)


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
    print(f"{seperator}Lets Play with numbers!{seperator}")
    choiceflag = True
    while choiceflag:
        inp = input("We can do the following:\n1.find_n_digits_of_pi\n2.find_n_digits_of_e\n3.fibonacci_series\n4.prime_factors_of_a_number\n5.next_prime_number\nSelect what you'll like to do:")
        if inp.isdigit():
            inp = int(inp)
            if inp in range(1,6):
                choiceflag = False
    numflag = True
    while numflag:
        number = input("Enter the number (If you have selected choice 1 or 2 then select number between 0 and 15): ")
        if number.isdigit():
            number = int(number)
            continuechoice = 'n'
            if inp in [1,2]:
                if number>=0 and number<=15:
                    numflag = False
                    if inp == 1:
                        print(f'{seperator}Finding value of pi till {number}th decimal point!')
                        find_n_digits_of_pi(number)
                        print(seperator)

                    else:
                        print(f'{seperator}Finding value of e till {number}th decimal point!')
                        find_n_digits_of_e(number)
                        print(seperator)

            elif inp == 3:
                numflag = False
                print(f'{seperator}Finding Fibonacci Series of {number} numbers!')
                fibonacci_series(number)
                print(seperator)

            elif inp == 4:
                numflag = False
                print(f'{seperator}Finding prime factors of num = {number}!')
                prime_factors(number)
                print(seperator)

            elif inp == 5:
                print(f'{seperator}Finding next prime number after {number}!')
                next_prime_number(number)
                print(seperator)
                numflag = False


while True:
    choiceLogic()
    cont = input('Do you want to continue? (y/n): ')
    if cont.lower() != 'y':
        break
