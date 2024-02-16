"""
Reservation class
"""
import uuid

from reservations_system.hotel.hotel import Hotel, Room
from reservations_system.customer.customer import Customer


# The Reservation class is used to manage reservations for a particular event or resource.
class Reservation:
    """
    Represents a reservation made by a customer for a room in a hotel.

    Attributes:
        hotel (Hotel): The hotel where the reservation is made.
        customer (Customer): The customer who made the reservation.
        room (Room): The room reserved.
        check_in (datetime): The check-in date and time.
        check_out (datetime): The check-out date and time.
    """

    def __init__(
        self, hotel: Hotel, customer: Customer, room: Room, check_in, check_out
    ) -> None:
        """
        Initializes a new Reservation instance.

        Args:
            hotel (Hotel): The hotel where the reservation is made.
            customer (Customer): The customer who made the reservation.
            room (Room): The room reserved.
            check_in (datetime): The check-in date and time.
            check_out (datetime): The check-out date and time.

        Returns:
            None
        """

        self.id = uuid.uuid4().hex
        self.hotel = hotel
        self.customer = customer
        self.room = room
        self.check_in = check_in
        self.check_out = check_out

    def __str__(self) -> str:
        """
        Returns a string representation of the Reservation instance.

        Returns:
            str: A string representation of the Reservation instance.
        """
        return f"Reservation for {self.customer.name} at {self.hotel.name} from {self.check_in} to {self.check_out}"

    def __repr__(self) -> str:
        """
        Returns a string representation of the Reservation instance.

        Returns:
            str: A string representation of the Reservation instance.
        """
        return f"Reservation for {self.customer.name} at {self.hotel.name} from {self.check_in} to {self.check_out}"

    # json serialization
    def to_json(self) -> dict:
        """
        Returns a dictionary representation of the Reservation instance.

        Returns:
            dict: A dictionary representation of the Reservation instance.
        """
        return {
            "id": self.id,
            "hotel": self.hotel.to_json(),
            "customer": self.customer.to_json(),
            "room": self.room.to_json(),
            "check_in": self.check_in,
            "check_out": self.check_out,
        }
