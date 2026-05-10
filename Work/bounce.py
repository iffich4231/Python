# bounce.py
#
# Exercise 1.5
initial_height = 100.0 # Initial height (meters)
bounce_factor = 0.6 # Bounce factor (3/5th of the previous height)
count = 0 # Count of bounces
number_of_bounces = 1 # Number of bounces to calculate
while count < 10:
    print(number_of_bounces,round(initial_height * bounce_factor, 4))
    count += 1
    number_of_bounces += 1
    initial_height = initial_height * bounce_factor

