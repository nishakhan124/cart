# # no empty name allowed
# # Check case for duplicate
# # never crash your program
# # Your Price should be in float
# # Never accepts bad data
# # Qty should be able to update




# import time
# cart = []
 
# item_dict = {}
# item =''

# def check_duplicate(cart,itme):
#     for list_item in cart:
#             if list_item['item'].upper() == item.upper():
#                 return False
# def add_item_to_cart(item):
#     price = int(input("item price:"))
#     quantity = int(input("Quantity:"))
#     item_dict["item"] = item
#     item_dict["price"] = price
#     item_dict["quantity"] = quantity

#     cart.append(item_dict)
#     print("item:", item, "added in cart")
#     print(cart)

#     def clear_cart(cart):
#         if len(cart)<0:
#             cart.clear()
#             print("your cart has been cleared")
#         else:
#          print("Your cart is already empty")
# def remove_item(cart):
#     item = input("\n Enter your item to remove!")
#     for cart_item in cart:
#         cart_item['item'] == item
#         cart.remove(cart_item)
#         break
# def cart_view(cart):
#     for item in cart:
#         print(item)
# def exit_program():
#     exit()

# def calculation(cart):
#     pass
# flag = True
# while flag:

#     print("\n")
#     print("1. Add Item")
#     print("2. Clear")
#     print("3. Remove Item")
#     print("4. View Item and Its Total")
#     print("5. Exit !!")
#     user_input = input("\nPlease Enter Your choice !! \n")
    
#     if user_input == "1":
#       # First check if item already exists in cart
#       item = input("Enter item name:").strip()
#       if item =="":
#           print("Invalid item to Add")
#           continue
#       if check_duplicate(cart, item):
#           print(f"Item'{item}'already exits in cart!")
#       else:
#           add_item_to_cart(item)
#           item_dict = {}

#     elif user_input =="2":
#         clear_cart(cart) 
    
#     elif user_input =="3":
#         remove_item(cart)
#     elif user_input =="4":   
#         cart_view(cart)
#     elif user_input =="5":
#         exit_program()
#     else:
#         print("Invalid Choice")
def print_menue():
    print("1. Add Item")
    print("2. Clear")
    print("3. Remove Item")
    print("4. View Items")
    print("5. Update quantity")
    print("6. Get Total")
    print("7. Search cart Item")
    print("8. Exit !!")