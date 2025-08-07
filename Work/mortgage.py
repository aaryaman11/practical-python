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

    # always calculate the ineterest first don't mix it with the rest of the code

    # calculating interest 
    principal = principal * (1 + rate / 12)

    payments = monthly
    if time >= extra_payment_start_month and time <= extra_payment_last_month:
        # when i was doing this monthly += extra_payment i was permantely modifying original monthly which lead to decrease in no. of months from original estimation as monthly was increasing 
        payments +=  extra_payment


    ## in the last month whatever is the balance only that should be paid ot more and the principal should show 0 not negative value
    # also have to cap the payment 
    if principal < monthly:
        payments = principal

    principal -= payments
    total_paid += payments
    time += 1

    print(time, round(total_paid, 2), round(principal, 2))
    

    # while time < 12:
    # if time == 0:
    #     for i in range(12):
    #         if extra_payment_start_month != 0 and time == 0:
    #             principal = principal * (1 + rate / 12) - monthly - 1000 - extra_payment_start_month
    #         else:
    #             principal = principal * (1 + rate / 12) - monthly - 1000
    #         time += 1
    #         total_paid += monthly + 1000
    # else: 
        # principal = principal + principal * rate / 12 - monthly
        # time += 1
        # total_paid  += monthly
print(f'Total_paid {round(total_paid, 2)} \nMonths {time}')


