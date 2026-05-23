cart = []
item_dict = {}

flag = True
while flag:
    print("\n1. Add Item, and Its Price and Quantity ")
    print("2. Clear")
    print("3. Remove Item")
    print("4. View Item and Its Total")
    #print("7. Packaging")
    
    print("5. Exit !!")
    user_input = input("\nPlease Enter Your choice !! \n")
    #print(user_input)
    
    if user_input == "1":
        #item = input("\nEnter  your item and Price and Quantity! ")
        item = input("Please Provide item Name")
        price = input("Please Provide item price")
        quantity = input("Please Provide Quantity")
        item_dict["item"] = item
        item_dict["price"] = price
        item_dict["quantity"] = quantity
        cart.append(item_dict)
        print ("\n",item_dict, ": has been added into cart")
        
    elif user_input == "3":
        item = input("\nEnter  your item  to remove! ")
        if item in cart:
            cart.remove(item)
            print ("\n",item, ": has been removed into cart")
        else :
            print (item, ": did not found in cart")
            
    elif user_input == "4":
        for item in cart:
            print(item)
        # add logic to show the price 
        # handle the logic of Total Price based on item * quatity * Price and minus Discount 
    
    elif user_input == "2":
        if len(cart) > 0:
            cart.clear()
            print("your cart has been cleared")
        else:
            print("Your cart is already empty")
        
    
    elif user_input == "9":
        print("\nTata !!")
        break
    else:
        print("Invaid choice entered !!")
        
    
    
    
    



    #  if len(cart) == 0:
    #     print("Cart is empty")
    #     return

    # total = 0

    # print("\n------ BILL ------")

    # for item in cart:

    #     item_total = item['price'] * item['quantity']

    #     total += item_total

    #     print(f"Item : {item['item']}")
    #     print(f"Price : {item['price']}")
    #     print(f"Quantity : {item['quantity']}")
    #     print(f"Total : {item_total}")
    #     print("-------------------")

    # print(f"\nFinal Cart Price = {total}")
    
    
   
    
    
    
    
    
    


 