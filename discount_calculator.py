price = input("Enter price: ")
discount = input("Enter discount: ")
discounted_price = int(price)
def calculate_discount(price, discount_percent):
    if (discount_percent)/100 >= 0.2:
        discounted_price = price - (price*(discount_percent/100))
        print(discounted_price)
    else:
        discounted_price = price
        print(discounted_price)
calculate_discount(int(price), int(discount))