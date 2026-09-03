from models.vehicle import Car
from models.parking_slot import ParkingSlot


def main():

    car = Car(
        "MP09CR5678",
        "Aman"
    )

    slot = ParkingSlot(
        "M-1",
        "MEDIUM"
    )

    print(slot)

    print("\nParking vehicle...\n")

    slot.park_vehicle(car)

    print(slot)

    print(
        f"Parked Vehicle: "
        f"{slot.vehicle.vehicle_number}"
    )

    print("\nRemoving vehicle...\n")

    removed_vehicle = (
        slot.remove_vehicle()
    )

    print(
        f"Removed: "
        f"{removed_vehicle.vehicle_number}"
    )

    print(slot)


if __name__ == "__main__":
    main()