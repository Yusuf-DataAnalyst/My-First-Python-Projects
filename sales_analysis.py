sales_data = [
    {"date": "2026-06-01", "product": "Laptop", "category": "Electronics", "price": 1200, "quantity": 2},
    {"date": "2026-06-01", "product": "Backpack", "category": "Fashion", "price": 50, "quantity": 5},
    {"date": "2026-06-02", "product": "Mouse", "category": "Electronics", "price": 25, "quantity": 10},
    {"date": "2026-06-02", "product": "T-Shirt", "category": "Fashion", "price": 30, "quantity": 3}
]

total_units = 0
total_revenue = 0
category_revenue = {} 

for sales in sales_data:

    current_sale_revenue = sales['price'] * sales['quantity']
    total_revenue += current_sale_revenue
    total_units += sales['quantity']
    category_name = sales['category']
    
    if category_name not in category_revenue:
           category_revenue[category_name] = current_sale_revenue
    else:
        category_revenue[category_name] += current_sale_revenue

print('=' * 40)
print("          Store Sales Report          ")
print('=' * 40)
print(f"Total Revenue: ${total_revenue}")
print(f"Total Units Sold: {total_units} pcs")
print('-' * 40)
print("Revenue per Category:")

for category, revenue in category_revenue.items():
    print(f" - {category}: ${revenue}")
    
print('=' * 40)