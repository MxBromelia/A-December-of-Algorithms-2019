"""December 1st"""

def sevenish_number(num):
    """Sevenish Number"""
    power_of_two = 0
    sevenish = 0
    while num > 0:
        val = pow(7, power_of_two) if num % 2 == 1 else 0
        sevenish += val
        power_of_two += 1
        num //= 2
    return sevenish
