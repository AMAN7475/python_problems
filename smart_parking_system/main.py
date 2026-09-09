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

from exceptions.parking_exceptions import (
    ParkingError
)


def setup_parking_lot():

    parking_lot = ParkingLot(
        "Indore Smart Parking"
    )

    # Bike slots

    for i in range(1, 3):

        parking_lot.add_slot(
            ParkingSlot(
                f"S-{i}",
                "SMALL"
            )
        )

    # Car slots

    for i in range(1, 3):

        parking_lot.add_slot(
            ParkingSlot(
                f"M-{i}",
                "MEDIUM"
            )
        )

    # Truck slot

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
            "Vehicles parked successfully!\n"
        )

        print(bike_ticket)
        print(car_ticket)
        print(truck_ticket)

        print(
            "\nParking Summary:"
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


if __name__ == "__main__":
    main()