from models.vehicle import (
    Bike,
    Car,
    Truck
)

from models.parking_slot import (
    ParkingSlot
)

from services.parking_service import (
    ParkingLot
)

from services.payment_service import (
    UPIPayment
)

from exceptions.parking_exceptions import (
    ParkingError
)


def setup_parking_lot():

    parking_lot = ParkingLot(
        "Indore Smart Parking"
    )

    for i in range(1, 3):

        parking_lot.add_slot(
            ParkingSlot(
                f"S-{i}",
                "SMALL"
            )
        )

    for i in range(1, 3):

        parking_lot.add_slot(
            ParkingSlot(
                f"M-{i}",
                "MEDIUM"
            )
        )

    parking_lot.add_slot(
        ParkingSlot(
            "L-1",
            "LARGE"
        )
    )

    return parking_lot


def main():

    parking_lot = (
        setup_parking_lot()
    )

    try:

        bike = Bike(
            "MP09BK1234",
            "Rahul"
        )

        car = Car(
            "MP09CR5678",
            "Aman"
        )

        truck = Truck(
            "MP04TR9999",
            "Ramesh"
        )

        # Entry

        bike_ticket = (
            parking_lot.park_vehicle(
                bike
            )
        )

        car_ticket = (
            parking_lot.park_vehicle(
                car
            )
        )

        truck_ticket = (
            parking_lot.park_vehicle(
                truck
            )
        )

        print(
            "Vehicles parked successfully!"
        )

        # Exit car

        print(
            "\nCar Exit Process"
        )

        completed_ticket, fee = (
            parking_lot.exit_vehicle(
                car_ticket.ticket_id,
                UPIPayment()
            )
        )

        print(
            f"\nVehicle exited successfully."
        )

        print(
            f"Parking Fee: ₹{fee}"
        )

        print(
            completed_ticket
        )

        # Final summary

        print(
            "\nFinal Parking Summary:"
        )

        summary = (
            parking_lot.get_parking_summary()
        )

        for key, value in summary.items():

            print(
                f"{key}: {value}"
            )

    except ParkingError as error:

        print(
            f"Parking Error: {error}"
        )

    except Exception as error:

        print(
            f"Unexpected Error: {error}"
        )


if __name__ == "__main__":
    main()