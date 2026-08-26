class CreditCard:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class PayPal:
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")


class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


# Create payment methods
credit_card = CreditCard()
upi = UPI()
paypal = PayPal()

# Select Credit Card
payment = Payment(credit_card)
payment.make_payment(1000)

# Change strategy to UPI
payment = Payment(upi)
payment.make_payment(500)

# Change strategy to PayPal
payment = Payment(paypal)
payment.make_payment(750)
