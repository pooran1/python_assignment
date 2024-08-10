from items import Item
from laptop import Laptop

if __name__ == "__main__":
    # Creating Item and Laptop objects from data/items.csv
    items = []
    with open('data/items.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, price, quantity = row[0], float(row[1]), int(row[2])
            if name.lower() == "laptop":
                item = Laptop(name, price, quantity, "NVIDIA GTX 1650", 4)
            else:
                item = Item(name, price, quantity)
            item.apply_discount()
            items.append(item)

    # Printing all items
    for item in items:
        print(item)
    
    # Attempt to update price directly to demonstrate the restriction
    try:
        items[0].price = 200
    except ValueError as e:
        print(e)
