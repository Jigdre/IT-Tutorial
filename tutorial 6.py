PI=3.14159

def greet(name):
    return (f"Hello, {name}!")

print(greet("Python"))



def rectangle(l,w):
    return l*w
print(rectangle(5,4))


def power(base,exponent=2):
    return base**exponent
print(power(3))



def circle_area(r):
    "Compute area of a circle of radius r."
    return PI*(r**2)

print(circle_area(2))


#Quick Exercises-------------------------------------------------------------

def fahrenheit_to_celcius(f):
    return (f-32)*(5/9)
print(fahrenheit_to_celcius(100))


def is_even(n):
    if n%2==0:
        return True
    else:
        return False

print(is_even(2))
print(is_even(8))
print(is_even(9))
print(is_even(4))



def triangle_area(b,h=1):
    return (1/2)*b*h

print(triangle_area(3,4))

#Mortgage calculations-------------------------------------------------------
#Wasnt able to do it

def input():
    annual_interest_rate=float(input("Enter annual rate of interest(%): "))
    monthly_payment=input("Enter monthly payment: ")
    beg_of_month_balance=input("Enter beginning of month balance: ")
    monthly_rate=annual_interest_rate/12
    interest_paid=interest_paid(monthly_interest_rate,beg_of_month_balance)
    reduction_of_principal=reduction_of_principal(monthly_payment,interest_paid)
    
def calculations():
def interest_paid(monthly_rate,beg_of_month_balance):
    return monthly_rate/100*beg_of_month_balance

def reduction_of_principal(monthly_payment,interest_paid):
    return monthly_payment-interest_paid

def mortgage_balance(beg_of_month_balance):
    if beg_of_month_balance
    beg_of_month_balance-interest_paid

print(interest_paid(2.5,2000))
