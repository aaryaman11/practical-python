# bounce.py
#
# Exercise 1.5
h = 100
# for i in range(10):
#     h = h*(3/5)
#     print((i + 1), round(h, 4))

# second way to write the solution
bounce = 1
while bounce <= 10:
    h = h*(3/5)
    print(bounce, round(h, 4))
    bounce += 1

    