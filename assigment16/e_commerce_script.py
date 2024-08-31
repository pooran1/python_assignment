import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root@123",
        database="e_commerce_database"
    )
    return connection

def add_category():
    name = input("Enter category name: ")
    description = input("Enter category description: ")

    query = "INSERT INTO Categories (name, description) VALUES (%s, %s)"
    cursor.execute(query, (name, description))
    conn.commit()
    print("Category added successfully!")

def add_product():
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = float(input("Enter product price: "))
    stock_quantity = int(input("Enter stock quantity: "))
    category_id = int(input("Enter category ID: "))

    query = "INSERT INTO Products (name, description, price, stock_quantity, category_id) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (name, description, price, stock_quantity, category_id))
    conn.commit()
    print("Product added successfully!")

def add_customer():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    country = input("Enter country: ")

    query = "INSERT INTO Users (first_name, last_name, email, password, address, city, country) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (first_name, last_name, email, password, address, city, country))
    conn.commit()
    print("Customer added successfully!")

def add_order():
    user_id = int(input("Enter user ID: "))
    status = input("Enter order status: ")

    query = "INSERT INTO Orders (user_id, status) VALUES (%s, %s)"
    cursor.execute(query, (user_id, status))
    order_id = cursor.lastrowid
    conn.commit()
    print(f"Order added successfully! Order ID: {order_id}")

    add_order_details(order_id)

def add_order_details(order_id):
    while True:
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))
        price_query = "SELECT price FROM Products WHERE id = %s"
        cursor.execute(price_query, (product_id,))
        price = cursor.fetchone()[0]

        query = "INSERT INTO Order_Details (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (order_id, product_id, quantity, price))
        conn.commit()

        more_products = input("Add another product to this order? (yes/no): ")
        if more_products.lower() != 'yes':
            break

def add_payment():
    order_id = int(input("Enter order ID: "))
    amount = float(input("Enter payment amount: "))
    status = input("Enter payment status: ")

    query = "INSERT INTO Payments (order_id, amount, status) VALUES (%s, %s, %s)"
    cursor.execute(query, (order_id, amount, status))
    conn.commit()
    print("Payment added successfully!")

def display_sales_metrics():
    query = "SELECT SUM(amount) FROM Payments WHERE status = 'Completed'"
    cursor.execute(query)
    total_revenue = cursor.fetchone()[0]
    print(f"Total Revenue: ${total_revenue:.2f}")

    query = """
    SELECT Products.name, SUM(Order_Details.quantity * Order_Details.price) AS revenue 
    FROM Order_Details 
    JOIN Products ON Order_Details.product_id = Products.id 
    GROUP BY Products.name 
    ORDER BY revenue DESC
    """
    cursor.execute(query)
    print("Revenue by Product:")
    for row in cursor.fetchall():
        print(f"{row[0]}: ${row[1]:.2f}")

def display_order_metrics():
    query = "SELECT COUNT(*) FROM Orders"
    cursor.execute(query)
    total_orders = cursor.fetchone()[0]

    query = "SELECT COUNT(*) FROM Orders WHERE status = 'Pending'"
    cursor.execute(query)
    pending_orders = cursor.fetchone()[0]

    query = "SELECT COUNT(*) FROM Orders WHERE status = 'Cancelled'"
    cursor.execute(query)
    cancelled_orders = cursor.fetchone()[0]

    successful_orders = total_orders - pending_orders - cancelled_orders

    print(f"Total Orders: {total_orders}")
    print(f"Pending Orders: {pending_orders}")
    print(f"Cancelled Orders: {cancelled_orders}")
    print(f"Successful Orders: {successful_orders}")

def display_payment_metrics():
    query = "SELECT SUM(amount) FROM Payments WHERE status = 'Pending'"
    cursor.execute(query)
    pending_payments = cursor.fetchone()[0]

    query = "SELECT SUM(amount) FROM Payments WHERE status = 'Completed'"
    cursor.execute(query)
    successful_payments = cursor.fetchone()[0]

    print(f"Pending Payments: ${pending_payments:.2f}")
    print(f"Successful Payments: ${successful_payments:.2f}")

def display_product_metrics():
    query = "SELECT name, stock_quantity FROM Products"
    cursor.execute(query)
    print("Inventory Levels:")
    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]} units")

    query = "SELECT COUNT(*) FROM Products WHERE stock_quantity = 0"
    cursor.execute(query)
    out_of_stock = cursor.fetchone()[0]

    print(f"Out of Stock Products: {out_of_stock}")

def display_geographical_metrics():
    query = """
    SELECT city, COUNT(*) AS order_count 
    FROM Users 
    JOIN Orders ON Users.id = Orders.user_id 
    GROUP BY city 
    ORDER BY order_count DESC
    """
    cursor.execute(query)
    print("Top Cities by Sales:")
    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]} orders")

    query = """
    SELECT country, SUM(Payments.amount) AS revenue 
    FROM Users 
    JOIN Orders ON Users.id = Orders.user_id 
    JOIN Payments ON Orders.id = Payments.order_id 
    GROUP BY country 
    ORDER BY revenue DESC
    """
    cursor.execute(query)
    print("Top Countries by Sales:")
    for row in cursor.fetchall():
        print(f"{row[0]}: ${row[1]:.2f}")

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Add Category")
        print("2. Add Product")
        print("3. Add Customer")
        print("4. Add Order")
        print("5. Add Payment")
        print("6. Display Sales Metrics")
        print("7. Display Order Metrics")
        print("8. Display Payment Metrics")
        print("9. Display Product Metrics")
        print("10. Display Geographical Metrics")
        print("11. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_category()
        elif choice == '2':
            add_product()
        elif choice == '3':
            add_customer()
        elif choice == '4':
            add_order()
        elif choice == '5':
            add_payment()
        elif choice == '6':
            display_sales_metrics()
        elif choice == '7':
            display_order_metrics()
        elif choice == '8':
            display_payment_metrics()
        elif choice == '9':
            display_product_metrics()
        elif choice == '10':
            display_geographical_metrics()
        elif choice == '11':
            break
        else:
            print("Invalid choice! Please try again.")

# Connect to the database
conn = connect_db()
cursor = conn.cursor()

# Start the application
main_menu()

# Close the connection
cursor.close()
conn.close()
