from services.payment_service import (
    CashPayment,
    CardPayment,
    UPIPayment
)


def process_payment(
    payment_method,
    amount
):

    payment_method.pay(amount)


def main():

    amount = 150

    print("Cash Payment:")
    process_payment(
        CashPayment(),
        amount
    )

    print("\nCard Payment:")
    process_payment(
        CardPayment(),
        amount
    )

    print("\nUPI Payment:")
    process_payment(
        UPIPayment(),
        amount
    )


if __name__ == "__main__":
    main()