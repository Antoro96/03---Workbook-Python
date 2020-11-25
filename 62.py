ORIGINAL_PRICE = [(4.95),(9.95), (14.95), (19.95), (24.95)]

 #discount_amounts = []
 #new_price = []

print("Original price", "\t\t", "Discount amount", "\t", "New Price")
for price in ORIGINAL_PRICE:
    
    DISCOUNT_AMOUNT = "60%"
    NEW_PRICE = (price * 60) /100
    print(price, "\t\t\t", DISCOUNT_AMOUNT, "\t\t\t", NEW_PRICE)
