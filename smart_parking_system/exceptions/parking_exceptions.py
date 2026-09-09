class ParkingError(Exception):
    """Base exception for parking errors."""
    pass


class ParkingSlotUnavailableError(
    ParkingError
):
    pass


class VehicleNotFoundError(
    ParkingError
):
    pass


class InvalidVehicleError(
    ParkingError
):
    pass