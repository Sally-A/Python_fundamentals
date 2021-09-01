class Queue:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print("Sorry we don't have that flavor")
        elif scoops < 1 or scoops > 3:
            print("Choose between 1-3 scoops")
        else:
            print("Order Created")
            order = {"Customer": customer, "Flavor": flavor, "Scoops": scoops}
            self.orders.enqueue(order)

    def show_all_orders(self):
        print("All Pending Ice Cream Orders")
        for order in self.orders.items:
            print("Customer: ", order["Customer"], " -- Flavor: ", order["Flavor"], " -- Scoops: ", order["Scoops"])


    def next_order(self):
        order = self.orders.dequeue()
        print("\nNext Order Up!")
        print("Customer: ", order["Customer"], " -- Flavor: ", order["Flavor"], " -- Scoops: ", order["Scoops"])


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()