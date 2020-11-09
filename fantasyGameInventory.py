def displayInventory(inventory):
    items = []
    numberOfItems = []
    for k in inventory.keys():
        items.append(k)
    for v in inventory.values():
        numberOfItems.append(v)
    print('Inventory:')
    for i in range(len(inventory)):
        print(numberOfItems[i], items[i])
    count = 0
    for n in numberOfItems:
        count += n
    print('Total number of items: ' + str(count))

displayInventory({'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12})
