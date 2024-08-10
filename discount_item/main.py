from items import Item

if __name__ == "__main__":
    items = Item.all_items('data/items.csv')
    for item in items:
        print(item)
