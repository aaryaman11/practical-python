# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05 # annual interest 
monthly = 2684.11
total_paid = 0.0
time = 0 # months
extra_payment = float(input("How much extra payment you want to do: "))
extra_payment_start_month = float(input("extra payment start month: "))
extra_payment_last_month = float(input("extra payment last month: "))

while principal > 0:
    # while time < 12:
    if time == 0:
        for i in range(12):
            if extra_payment_start_month != 0 and time == 0:
                principal = principal * (1 + rate / 12) - monthly - 1000 - extra_payment_start_month
            else:
                principal = principal * (1 + rate / 12) - monthly - 1000
            time += 1
            total_paid += monthly + 1000
    else: 
        principal = principal + principal * rate / 12 - monthly
        time += 1
        total_paid  += monthly
print('Total_paid', total_paid, 'over', time, "months")

