from datetime import datetime
from uuid import uuid4
import math


class ParkingTicket:

    def __init__(self, vehicle, slot):

        self.ticket_id = (
            str(uuid4())[:8].upper()
        )

        self.vehicle = vehicle
        self.slot = slot

        self.entry_time = datetime.now()

        self.exit_time = None

        self.is_active = True

        self.amount_paid = 0

    def close_ticket(self):

        if not self.is_active:
            raise ValueError(
                "Ticket is already closed."
            )

        self.exit_time = datetime.now()

        self.is_active = False

    def get_parking_duration_hours(self):

        end_time = (
            self.exit_time
            if self.exit_time
            else datetime.now()
        )

        duration = (
            end_time
            - self.entry_time
        )

        hours = (
            duration.total_seconds()
            / 3600
        )

        return max(
            1,
            math.ceil(hours)
        )

    def calculate_fee(self):

        hours = (
            self.get_parking_duration_hours()
        )

        return (
            hours
            * self.vehicle.get_hourly_rate()
        )

    def __str__(self):

        status = (
            "ACTIVE"
            if self.is_active
            else "COMPLETED"
        )

        return (
            f"\nTicket ID: {self.ticket_id}\n"
            f"Vehicle: "
            f"{self.vehicle.vehicle_number}\n"
            f"Slot: {self.slot.slot_id}\n"
            f"Entry: {self.entry_time}\n"
            f"Status: {status}"
        )