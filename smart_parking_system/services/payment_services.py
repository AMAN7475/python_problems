from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CashPayment(PaymentMethod):

    def pay(self, amount):

        print(
            f"Cash payment of ₹{amount} completed."
        )

        return True


class CardPayment(PaymentMethod):

    def pay(self, amount):

        print(
            f"Card payment of ₹{amount} completed."
        )

        return True


class UPIPayment(PaymentMethod):

    def pay(self, amount):

        print(
            f"UPI payment of ₹{amount} completed."
        )

        return True