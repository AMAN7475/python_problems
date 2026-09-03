class ParkingSlot:

    def __init__(self, slot_id, slot_type):

        self.slot_id = slot_id
        self.slot_type = slot_type

        self.__is_available = True
        self.__vehicle = None

    @property
    def is_available(self):

        return self.__is_available

    @property
    def vehicle(self):

        return self.__vehicle

    def park_vehicle(self, vehicle):

        if not self.__is_available:
            raise ValueError(
                f"Slot {self.slot_id} "
                "is already occupied."
            )

        if vehicle.required_slot_type != self.slot_type:

            raise ValueError(
                f"{vehicle.vehicle_type} cannot park "
                f"in {self.slot_type} slot."
            )

        self.__vehicle = vehicle
        self.__is_available = False

    def remove_vehicle(self):

        if self.__is_available:

            raise ValueError(
                f"Slot {self.slot_id} "
                "is already empty."
            )

        vehicle = self.__vehicle

        self.__vehicle = None
        self.__is_available = True

        return vehicle

    def __str__(self):

        status = (
            "AVAILABLE"
            if self.__is_available
            else "OCCUPIED"
        )

        return (
            f"Slot: {self.slot_id} | "
            f"Type: {self.slot_type} | "
            f"Status: {status}"
        )