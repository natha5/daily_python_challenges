

def my_discount():

    input_price = int(input('input price : '))
    input_discount = int(input('input discount (%) : '))

    decimal_discount = (100 - input_discount) / 100

    discounted_price = input_price * decimal_discount

    print(discounted_price)

    return discounted_price

my_discount()