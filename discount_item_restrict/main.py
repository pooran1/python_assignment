from items import Item

if __name__ == "__main__":
    items = Item.all_items('data/items.csv')
    for item in items:
        print(item)
    
    # Attempt to update price directly to demonstrate the restriction
    try:
        items[0].price = 200
    except ValueError as e:
        print(e)
