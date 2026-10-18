
class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    # Property for getting the discount
    @property
    def discount(self):
        return self._discount

    # Setter for checking the discount
    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    # Add an item to the cash register
    def add_item(self, item, price, quantity=1):
        if not isinstance(price, (int, float)) or isinstance(price, bool) or price < 0:
            print("Not valid price")
            return

        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            print("Not valid quantity")
            return

        cost = price * quantity
        self.total = round(self.total + cost, 2)

        for _ in range(quantity):
            self.items.append(item)

        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }

        self.previous_transactions.append(transaction)

    # Apply discount to the total
    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total = round(self.total - discount_amount, 2)

            if float(self.total).is_integer():
                self.total = int(self.total)

            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    # Remove the last transaction
    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            print("There are no transactions to void.")
            return

        last_transaction = self.previous_transactions.pop()

        cost = last_transaction["price"] * last_transaction["quantity"]
        self.total = round(self.total - cost, 2)

        for _ in range(last_transaction["quantity"]):
            self.items.pop()

        print("Last transaction has been voided.")
