
from util.global_function import tax_calculate
products = [ {"name": "apple", "price": 1.20}, 
             {"name": "banana", "price": 0.80}, 
             {"name": "orange", "price": 1.50}
             ]
vendors = [ {"name": "Deba", "location": "Kolkata"},
            {"name": "Ram", "location": "June"},
            {"name": "Sham", "location": "Bangalore"}
            ]
tax_calculate(products = products, vendors = vendors)
print(products, vendors)