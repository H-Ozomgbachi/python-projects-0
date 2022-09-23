'''
    Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.
'''
def dis(price, discount):
    discountValue = price * (discount / 100)
    return price - discountValue
