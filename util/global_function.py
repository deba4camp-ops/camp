
def tax_calculate(products, vendors):
    for product in products:
        product["price"] = product["price"] + 10.00
    for vendor in vendors:
        vendor["location"] = vendor["location"] + " City"
        