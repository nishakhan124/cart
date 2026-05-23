import time 
import json
import logging
import p2


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - Line:%(lineno)d - %(message)s"
    )


logging.info(" Program Started \n")

cart =  []

item_dict = {}
item = ''


def open_file():
    try: 
        with open("nisha_cart_item.json", "r") as file:
            cart = json.load(file)
        logging.info("Cart loaded successfully..")
        return cart
        
    except FileNotFoundError:
        logging.error("cart file not found..")
    except json.JSONDecodeError:
        logging.error("Invalid JSON Format")
    

def save_file(cart):
    try:
        with open("nisha_cart_item.json", "w") as file :
            json.dump(cart,file, indent=4 )
        logging.info("Cart Saved Succcessfully....!")
    except Exception as e:
        logging.error(f"Failed to save cart: {e}")


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
                logging.warning("Price must be greater then 0")
                continue
            break
        except ValueError:
            logging.warning("Please Enter Valid price")
    while True:    
        try:    
            quantity = int(input("Quantity: "))
            if quantity <=0:
                logging.warning("quantity must be greater then 0")
                continue

            break
        except ValueError:
            logging.warning("Please Enter Valid Quantity")
    item_dict =   {}
    item_dict["item"] = item
    item_dict["price"] = price
    item_dict["quantity"] = quantity

    cart.append(item_dict)
    logging.info(f"item : {item} added in the cart")
    logging.info(cart)
    return cart


def clear_cart(cart):
    if len(cart) > 0:
        cart.clear()
        logging.info("your cart has been cleared")
    else:
        logging.warning("Your cart is already empty")


def remove_item(cart):
    relove_flag = True
    item = input("\n Enter your item to remove! ").strip()
    print(item)
    print(type(item))
    for cart_item in cart:
        print(cart_item)
        time.sleep(5)
        if cart_item['item'].upper() == item.upper():
            cart.remove(cart_item)
            logging.info(f"Item {item} Removed !")
            relove_flag = False
            break
    if relove_flag:
        logging.warning( f"Item {item} Not available in the cart !")


def cart_view(cart):
    for item in cart:
        logging.info(item)


def exit_program():
    exit(0)


def calculation(cart):
    Total_bill = 0
    print("*"*100)
    print("\n")
    print("-"*50)
    for cart_item in cart:
        logging.info(f"total price of {cart_item['item']} is {cart_item['quantity'] * cart_item['price']}")
        Total_bill = Total_bill + cart_item['quantity'] * cart_item['price']
    print("-"*50)
    print("\n")
    logging.info(f"Total bill is {Total_bill}")
    print("*"*100)

def update_quantity(cart):
    item_found = False
    item = input("Enter Item name to update the quantity: ").strip()
    if item == "":
        logging.warning("Invlaid Item Name ")
        return
    
    for cart_item in cart:
        if cart_item['item'].upper()== item.upper():
            while True:
                try:
                    new_qyt  = int(input("Enter New Quantity: "))
                    if new_qyt <=0:
                        logging.warning("New quantity must be greater then 0")
                        continue
                    cart_item['quantity'] = new_qyt
                    logging.info( f"New Quantity : {new_qyt} updated for the item {cart_item['item']}")

                    return
                except Exception:
                    logging.warning(f"Please enter valid Quantity for the item {item}")
            item_found = True
    
    if item_found == False:
        logging.warning("Item not available in the cart")

def search_cart(cart):
    item = input("Enter item to search...")
    for cart_item in cart:
        if cart_item['item'].upper() == item.upper():
            logging.info("Item found")
            logging.info(cart_item)
            break

flag = True
cart = open_file()  # Load cart ONCE before the loop
while flag:
    p2.print_menue()
    user_input = input("\nPlease Enter Your choice !! \n")
    
    if user_input == "1":
        # First check if item already exists in cart
        item = input("Please Enter Item Name to Add ").strip()
        if item == "":
            logging.error("Invalid Item to Add")
            continue
        if check_duplicate(cart, item):
            logging.warning(f"Item '{item}' already exists in cart!")
        else:
            cart = add_item_to_cart(item)
        

    elif user_input == "2":
        clear_cart(cart)
        
    elif user_input == "3":
        remove_item(cart)

    elif user_input == "4":
        cart_view(cart)
    
    elif user_input == "5":
        update_quantity(cart)

    elif user_input == "6":
        calculation(cart)

    elif user_input == "7":
        search_cart(cart)

    elif user_input == "8":
        save_file(cart)
        exit_program()

    else:
        logging.warning("Invalid Choice")
   
 