# Calculate the no of chocolate with a certeain amount
# consider prise 1 Rupees per unit
# Every 3 wrapper could be exchanged for 1 chocolate
# Calculate how much chocolate we can get in given amount
# Sample Input - 15 Rupees
# Sample Output - 22 Chocolate


def total_chocolate(amount):
    wrapper = amount
    chocolate = amount

    while wrapper >= 3:
        wrapper -= 2
        chocolate += 1

    return chocolate


if __name__ == "__main__":
    print(total_chocolate(15))
