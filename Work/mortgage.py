# mortgage.py
#
# Exercise 1.7
principal = 500000.0 
rate = 0.05
payment = 2684.11
total_paid = 0.0
number_of_months = 0

extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108


while principal > 0:
    interest = principal * (rate / 12)
    current_payment = payment

    if extra_payment_start_month <= number_of_months + 1 <= extra_payment_end_month:
        current_payment += extra_payment
    if principal + interest < current_payment:
        current_payment = principal + interest
    
    principal = principal + interest - current_payment
    total_paid += current_payment
    number_of_months += 1

    print(number_of_months, round(total_paid, 2), round(principal, 2))

print(f'Total paid {total_paid}')
print(f'Number of months {number_of_months}')