# no empty name allowed
# Check case for duplicate
# never crash your program # try except
# Your Price should be in float
# Never accepts bad data
# Qty should be able to update
# when QTY update update Price also 



import time 
import json
cart =  []

item_dict = {}
item = ''

def open_file():
    with open("nisha_cart_item.json", "r") as file:
        cart = json.load(file)
    return cart

def save_file(cart):
    with open("nisha_cart_item.json", "w") as file :
        json.dump(cart,file, indent=4 )
    print("Cart Saved Succcessfully....!")


def check_duplicate(cart, item):
    for list_item in cart:
        if list_item['item'].upper() == item.upper():
            return True
    return False

def add_item_to_cart (item):
    while True:
        try:
            price = float(input("item price: "))
            if price <=0:
                print("Price must be greater then 0")
                continue
            break
        except ValueError:
            print("Please Enter Valid price")
    while True:    
        try:    
            quantity = int(input("Quantity: "))
            if quantity <=0:
                print("quantity must be greater then 0")
                continue

            break
        except ValueError:
            print("Please Enter Valid Quantity")
    item_dict =   {}
    item_dict["item"] = item
    item_dict["price"] = price
    item_dict["quantity"] = quantity

    cart.append(item_dict)
    print("item : ",item, "added in the cart") 
    print(cart)
    return cart




def search_item(cart):

    item_name = input("Enter Item Name To Search : ").strip()

    if item_name == "":
        print("Invalid Item Name")
        return

    item_found = False

    for item in cart:

        if item['item'].upper() == item_name.upper():

            print("\nItem Found")
            print("------------------")
            print("Item :", item['item'])
            print("Price :", item['price'])
            print("Quantity :", item['quantity'])

            item_found = True
            break

    if item_found == False:
        print("Item Not Found In Cart")


def clear_cart(cart):
    if len(cart) > 0:
        cart.clear()
        print("your cart has been cleared")
    else:
        print("Your cart is already empty")


def remove_item(cart):
    item = input("\n Enter  your item  to remove! ")
    for cart_item in cart:
        cart_item['item'].upper()== item.upper()
        cart.remove(cart_item)
        print("Item",item, " Removed !")
        break


def cart_view(cart):
    for item in cart:
        print(item)


def exit_program():
    exit(0)


def calculation(cart):
     if len(cart) == 0:
        print("Cart is empty")
        return

     total = 0 

     print("\n------ BILL ------")

     for item in cart:

        item_total = item['price'] * item['quantity']

        total += item_total

        print(f"Item : {item['item']}")
        print(f"Price : {item['price']}")
        print(f"Quantity : {item['quantity']}")
        print(f"Total : {item_total}")
        print("-------------------")

        print(f"\nFinal Cart Price = {total}")
    
    
   
    
   
   
 

def update_quantity(cart):
    item_found = False
    item = input("Enter Item name to update the quantity: ").strip()
    if item == "":
        print("Invlaid Item Name ")
        return
    
    for cart_item in cart:
        if cart_item['item'].upper()== item.upper():
            while True:
                try:
                    new_qyt  = int(input("Enter New Quantity: "))
                    if new_qyt <=0:
                        print("New quantity must be greater then 0")
                        continue
                    # qty_bkp = cart_item['quantity']
                    cart_item['quantity'] = new_qyt
                    # # Assumption ; price / quantity = price of one quantity
                    # price_per_qty = cart_item['price'] / qty_bkp
                    # total_qty_price = new_qyt * price_per_qty
                    # cart_item['price'] = total_qty_price

                    
                    print(f"Quantity updated for the item {item}")
                    return
                except Exception:
                    print(f"Please enter valid Quantity for the item {item}")
            item_found = True
    
    if item_found == False:
        print("Item not available in the cart")



def get_total (cart):
    pass




flag = True
cart = open_file()  # Load cart ONCE before the loop

while flag:
    print("1. Add Item")
    print("2. Clear")
    print("3. Search Item")
    print("4. Remove Item")
    print("5. View Items")
    print("6. Update quantity")
    print("7. Get Total")
    print("8. Exit !!")
    user_input = input("\nPlease Enter Your choice !! \n")
    
    if user_input == "1":
        # First check if item already exists in cart
        item = input("Enter item name: ").strip()
        if item == "":
            print("Invalid Item to Add")
            continue
        if check_duplicate(cart, item):
            print(f"Item '{item}' already exists in cart!")
        else:
            cart = add_item_to_cart(item)
        

    elif user_input == "2":
        clear_cart(cart)

    elif user_input == "3":
      search_item(cart)
        
    elif user_input == "4":
        remove_item(cart)

    elif user_input == "5":
        cart_view(cart)
    
    elif user_input == "6":
        update_quantity(cart)

    elif user_input == "7":
        calculation(cart)

    elif user_input == "8":
        save_file(cart)
        exit_program()

    else:
        print("Invalid Choice")
   
   
# We learned JSON Module 
# Two Method IN JSON : load (when we read json file from disk) , dump (when we save json file into disk)
# If file is empty then json.load will not work
# file need to be present
# Date 2nd May - Homework : Write 2 Lines about the program and Remember 
    
    

   