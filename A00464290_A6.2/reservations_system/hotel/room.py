"""
Room class
"""
import uuid

from enum import Enum


class RoomType(Enum):
    """
    Enum representing the types of rooms available in the hotel.

    Attributes:
        SINGLE (str): Represents a single room.
        DOUBLE (str): Represents a double room.
        SUITE (str): Represents a suite room.
    """

    SINGLE = "single"
    DOUBLE = "double"
    SUITE = "suite"


class RoomStatus(Enum):
    """
    Enum representing the status of a hotel room.

    Attributes:
        AVAILABLE: The room is available for reservation.
        RESERVED: The room has been reserved but not yet occupied.
        OCCUPIED: The room is currently occupied by a guest.
        OUT_OF_ORDER: The room is temporarily out of order and cannot be occupied.
    """

    AVAILABLE = "available"
    RESERVED = "reserved"
    OCCUPIED = "occupied"
    OUT_OF_ORDER = "out_of_order"


class Room:
    """Base Room class"""

    def __init__(
        self,
        room_number: str,
        room_type: RoomType,
        room_status: RoomStatus,
        room_price: float,
    ) -> None:

        """
        Initializes a new Room instance.

        Args:
            room_number (str): The room number.
            room_type (RoomType): The type of room.
            room_status (RoomStatus): The status of the room.
            room_price (float): The price of the room.

        Returns:
            None
        """
        self.id = uuid.uuid4().hex
        self.room_number = room_number
        self.room_type = room_type
        self.room_status = room_status
        self.room_price = room_price

    def __str__(self) -> str:
        """
        Returns a string representation of the Room instance.

        Returns:
            str: A string representation of the Room instance.
        """
        return f"Room {self.room_number} - {self.room_type} - {self.room_status}"

    def __repr__(self) -> str:
        """
        Returns a string representation of the Room instance.

        Returns:
            str: A string representation of the Room instance.
        """

        return f"Room {self.room_number} - {self.room_type} - {self.room_status}"

    # json serialization
    def to_json(self) -> dict:
        """
        Returns a dictionary representation of the Room instance.

        Returns:
            dict: A dictionary representation of the Room instance.
        """
        return {
            "id": self.id,
            "room_number": self.room_number,
            "room_type": self.room_type.value,
            "room_status": self.room_status.value,
            "room_price": self.room_price,
        }
