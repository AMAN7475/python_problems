from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, vehicle_number, owner_name):
        self.vehicle_number = vehicle_number.upper()
        self.owner_name = owner_name

    @property
    @abstractmethod
    def vehicle_type(self):
        pass

    @property
    @abstractmethod
    def required_slot_type(self):
        pass

    @abstractmethod
    def get_hourly_rate(self):
        pass

    def __str__(self):
        return (
            f"{self.vehicle_type} - "
            f"{self.vehicle_number} "
            f"(Owner: {self.owner_name})"
        )


class Bike(Vehicle):

    @property
    def vehicle_type(self):
        return "BIKE"

    @property
    def required_slot_type(self):
        return "SMALL"

    def get_hourly_rate(self):
        return 20


class Car(Vehicle):

    @property
    def vehicle_type(self):
        return "CAR"

    @property
    def required_slot_type(self):
        return "MEDIUM"

    def get_hourly_rate(self):
        return 50


class Truck(Vehicle):

    @property
    def vehicle_type(self):
        return "TRUCK"

    @property
    def required_slot_type(self):
        return "LARGE"

    def get_hourly_rate(self):
        return 100