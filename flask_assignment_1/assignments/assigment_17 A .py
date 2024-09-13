from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root@123',
        database='assignment_db'
    )

# Create tables if they do not exist
def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS category (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            cat_id INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (cat_id) REFERENCES category(id)
        )
    ''')
    connection.commit()
    connection.close()

init_db()

# Hello Flask endpoint
@app.route('/', methods=['GET'])
def hello_flask():
    return jsonify({'message': 'Hello Flask'}), 200

# Add a new category
@app.route('/categories', methods=['POST'])
def add_category():
    data = request.json
    name = data['name']
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO category (name) VALUES (%s)', (name,))
    connection.commit()
    connection.close()
    return jsonify({'message': 'Category added successfully'}), 201

# Get all categories
@app.route('/categories', methods=['GET'])
def get_categories():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM category')
    categories = cursor.fetchall()
    connection.close()
    return jsonify(categories)

# Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    name = data['name']
    cat_id = data['cat_id']
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO product (name, cat_id) VALUES (%s, %s)', (name, cat_id))
    connection.commit()
    connection.close()
    return jsonify({'message': 'Product added successfully'}), 201

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('''
        SELECT p.id, p.name, c.name AS category, p.created_at, p.updated_at
        FROM product p
        LEFT JOIN category c ON p.cat_id = c.id
    ''')
    products = cursor.fetchall()
    connection.close()
    return jsonify(products)

# Update a product's name
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    name = data['name']
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE product SET name = %s WHERE id = %s', (name, id))
    connection.commit()
    connection.close()
    return jsonify({'message': 'Product updated successfully'})

# Delete a product
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM product WHERE id = %s', (id,))
    connection.commit()
    connection.close()
    return jsonify({'message': 'Product deleted successfully'})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=4000)


# app.run(
#     debug=True,
#     port=3000
# )