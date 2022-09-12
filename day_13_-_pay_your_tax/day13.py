
def your_vat():
    vat_percentage = 101
    while vat_percentage > 100:
        initial_price = int(input("Enter item price: "))
        vat_percentage = int(input("Enter item VAT (%): "))

        if vat_percentage > 100:
            print("VAT must be 100% or lower ")

    vat_amount = (vat_percentage * initial_price) / 100

    total_price = vat_amount + initial_price

    print("VAT inclsive price = ", total_price)


your_vat()

