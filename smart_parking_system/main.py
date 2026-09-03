from models.vehicle import (
    Bike,
    Car,
    Truck
)


def main():

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

    print(bike)
    print(car)
    print(truck)

    print()

    print(
        f"Bike Rate: ₹{bike.get_hourly_rate()}/hour"
    )

    print(
        f"Car Rate: ₹{car.get_hourly_rate()}/hour"
    )

    print(
        f"Truck Rate: ₹{truck.get_hourly_rate()}/hour"
    )


if __name__ == "__main__":
    main()