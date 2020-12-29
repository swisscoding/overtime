#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Calculate overtime and pay associated with it | ----\n", fg("red")))

# user interaction
print("Input information in this form (24-hour day notation) ->\nstart_of_work, end_of_work, hourly_rate, overtime_multiplier\nEverything over 8 hours will be overtime.\n")
# [start_of_work, end_of_work, hourly_rate, overtime_multiplier]
user_input = [float(i) for i in input(": ").split(", ")]

def calculate_overtime(start, end):
    return end - start

def calculate_pay(hours, rate, multiplier):
    if hours <= 8:
        return round(hours * rate, 2)
    elif hours > 8:
        return round(8 * rate + (hours - 8) * rate * multiplier, 2)

hours_of_work = calculate_overtime(user_input[0], user_input[1])
overtime = stylize(str(hours_of_work - 8), fg("red"))
payment = stylize(str(calculate_pay(hours_of_work, user_input[2], user_input[3])), fg("green"))

if hours_of_work - 8 > 0:
    print(f"\nHours of work: {hours_of_work}\nHours of overtime: {overtime}\nPayment: {payment}\n")
else:
    print(f"\nHours of work: {hours_of_work}\nHours of overtime: 0\nPayment: {payment}\n")
