
grocery_inventory = {"Milk": (113,"Dairy"),
                     "Eggs": (116,"Dairy"),
                     "Bread": (117,"Bakery"),
                     "Apples": (141, "Prodoce"),
                     "Cookies": (143, "Bakery")
                    }
bread_details = grocery_inventory["Bread"]
grocery_inventory.pop ("Eggs")

print ("Details of Bread:",bread_details)
print (grocery_inventory)
print("Inventory after adding Cookies:", grocery_inventory)  
print("Inventory after removing Eggs:", grocery_inventory)







