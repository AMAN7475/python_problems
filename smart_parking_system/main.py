from models.vehicle import Car
from models.parking_slot import ParkingSlot
from models.parking_ticket import ParkingTicket


def main():

    car = Car(
        "MP09CR5678",
        "Aman"
    )

    slot = ParkingSlot(
        "M-1",
        "MEDIUM"
    )

    slot.park_vehicle(car)

    ticket = ParkingTicket(
        car,
        slot
    )

    print(ticket)

    print(
        f"\nCurrent Fee: "
        f"₹{ticket.calculate_fee()}"
    )

    ticket.close_ticket()

    print(
        f"\nFinal Fee: "
        f"₹{ticket.calculate_fee()}"
    )


if __name__ == "__main__":
    main()