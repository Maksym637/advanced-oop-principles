from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid ${amount:.2f} using Credit Card [{self.card_number}].")


class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid ${amount:.2f} using PayPal account [{self.email}].")


class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Paid ${amount:.2f} using Bitcoin wallet [{self.wallet_address}].")


class ShoppingCart:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.items = []
        self.payment_strategy = payment_strategy

    def add_item(self, item, price):
        self.items.append((item, price))

    def calculate_total(self):
        return sum(price for _, price in self.items)

    def checkout(self):
        total = self.calculate_total()
        print(f"Total amount: ${total:.2f}")
        self.payment_strategy.pay(total)


paypal_strategy = PayPalPayment("user@example.com")

cart = ShoppingCart(paypal_strategy)

cart.add_item("Book", 12.99)
cart.add_item("Pen", 1.49)
cart.checkout()
