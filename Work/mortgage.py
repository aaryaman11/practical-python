# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05 # annual interest 
monthly = 2684.11
total_paid = 0.0
time = 0 # moths
while principal > 0:
    principal = principal + principal * rate / 12 - monthly
    time += 1
    total_paid  += monthly
print('Total_paid', total_paid, 'over', time, "months")

