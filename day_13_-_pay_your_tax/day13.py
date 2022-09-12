
def your_vat():
    vat_percentage = 101
    while vat_percentage > 100:
        intial_price = input("Enter item price: ")
        vat_percentage = input("Enter item VAT (%): ")

        if(vat_percentage > 100):
            print("VAT must be 100% or lower ")

    vat_amount = (intial_price / vat_percentage) * 100

    total_price = vat_amount + intial_price

    print("VAT inclsive price = ", total_price)

