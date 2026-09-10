from models.parking_ticket import (
    ParkingTicket
)

from exceptions.parking_exceptions import (
    ParkingSlotUnavailableError,
    VehicleNotFoundError,
    InvalidVehicleError
)


class ParkingLot:

    def __init__(self, name):

        self.name = name

        self.slots = []

        # ticket_id -> ParkingTicket
        self.active_tickets = {}

        # vehicle_number -> ticket_id
        self.vehicle_registry = {}

    def add_slot(self, slot):

        self.slots.append(slot)

    def find_available_slot(self, vehicle):

        for slot in self.slots:

            if (
                slot.is_available
                and slot.slot_type
                == vehicle.required_slot_type
            ):
                return slot

        return None

    def park_vehicle(self, vehicle):

        if not vehicle.vehicle_number:

            raise InvalidVehicleError(
                "Vehicle number cannot be empty."
            )

        if (
            vehicle.vehicle_number
            in self.vehicle_registry
        ):

            raise InvalidVehicleError(
                "Vehicle is already parked."
            )

        slot = (
            self.find_available_slot(
                vehicle
            )
        )

        if not slot:

            raise (
                ParkingSlotUnavailableError(
                    f"No "
                    f"{vehicle.required_slot_type} "
                    f"slot available."
                )
            )

        slot.park_vehicle(vehicle)

        ticket = ParkingTicket(
            vehicle,
            slot
        )

        self.active_tickets[
            ticket.ticket_id
        ] = ticket

        self.vehicle_registry[
            vehicle.vehicle_number
        ] = ticket.ticket_id

        return ticket

    def get_active_ticket(
        self,
        vehicle_number
    ):

        vehicle_number = (
            vehicle_number.upper()
        )

        ticket_id = (
            self.vehicle_registry.get(
                vehicle_number
            )
        )

        if not ticket_id:

            raise VehicleNotFoundError(
                "Vehicle is not currently parked."
            )

        return self.active_tickets[
            ticket_id
        ]

    def show_available_slots(self):

        return [
            slot
            for slot in self.slots
            if slot.is_available
        ]

    def get_parking_summary(self):

        total_slots = len(
            self.slots
        )

        available_slots = len(
            self.show_available_slots()
        )






    def exit_vehicle(
        self,
        ticket_id,
        payment_method
    ):

        ticket = (
            self.active_tickets.get(
                ticket_id
            )
        )

        if not ticket:

            raise VehicleNotFoundError(
                "Active ticket not found."
            )

        fee = ticket.calculate_fee()

        payment_success = (
            payment_method.pay(
                fee
            )
        )

        if not payment_success:

            raise ParkingError(
                "Payment failed."
            )

        ticket.amount_paid = fee

        ticket.close_ticket()

        ticket.slot.remove_vehicle()

        del self.vehicle_registry[
            ticket.vehicle.vehicle_number
        ]

        del self.active_tickets[
            ticket_id
        ]

        return ticket, fee

        return {
            "parking_lot": self.name,
            "total_slots": total_slots,
            "available_slots": (
                available_slots
            ),
            "occupied_slots": (
                total_slots
                - available_slots
            ),
            "active_vehicles": len(
                self.active_tickets
            )
        }