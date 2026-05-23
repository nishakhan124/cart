import sqlite3
import logging
from config import DB_Name, TABLE_NAME
logger = logging.getLogger(__name__)

def get_db_connection():
    conn = sqlite3.connect("cart.db")
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS cart_items (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   item TEXT NULL UNIQUE,
                   price REAL NOT NULL,
                   quantity REAL NOT NULL
                   )
                   
                   """)

    conn.commit()
    conn.close()
    logging.info(f"Database inittialized sucessfully.")


def load_cart():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT item, price, quantity FROM cart_items")
        rows = cursor.fetchall()
        #print("*"*50)
        conn.close
        cart = []
        for row in rows:
            cart.append({"item": row[0],
                         "price": row[1],
                         "quantity": row[2]})
        logging.info("Cart Loaded sucessfully..")
        return cart
    except Exception as e:
        logging.info(f"database connection failed {e}")
        return []
    
def save_cart(cart):
    try: 
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cart_items")

        # Insert data into cart
        for cart_item in cart:
            cursor.execute(
                
            "INSERT INTO cart_items (item, price, quantity) VALUES (? , ?, ?)", 
            (cart_item["item"], cart_item["price"], cart_item["quantity"])
           
            )
        
        conn.commit()
        conn.close()
        logging.info(f"cart Saved into the database table:  cart_items")

    except Exception as e:
        logging.info(f"failed to Save cart in memeory {e}")


