# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}

# Convert each sales string to float, then sum
total_sales_list = ["1.20", "0.50", "2.50", "1.75"]
total_sales = sum(float(s) for s in total_sales_list)

print(total_sales)