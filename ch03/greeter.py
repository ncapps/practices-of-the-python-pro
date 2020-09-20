#!/usr/bin/env python3
"""
Author : ncapps
Date   : 09/20/2020
Purpose: Store greeter class
"""

from datetime import datetime


def day():
    return datetime.now().strftime('%A')


def  part_of_day():
    current_hour = datetime.now().hour

    if current_hour < 12:
        return 'morning'
    elif current_hour < 17:
        return 'afternoon'
    else:
        return 'evening'

class Greeter():
    def greet(self, store):
        return '\n'.join([
            f'Hi! welcome to {store}!',
            f"How's your {day()} {part_of_day()} going?",
            f"Here's a coupon for 20% off!"
        ])


# --------------------------------------------------
def main():
    greeter = Greeter()
    print(greeter.greet("Walmart"))


# --------------------------------------------------
if __name__ == '__main__':
    main()
