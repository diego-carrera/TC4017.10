"""
Hotel class and HotelsManager class
"""
import uuid

from reservations_system.hotel.room import Room


class Hotel:
    """
    Base Hotel class
    """

    def __init__(self, name: str, location: str, rooms: list[Room]) -> None:
        """
        Initializes a new Hotel instance.

        Args:
            name (str): The name of the hotel.
            location (str): The location of the hotel.
            rooms (list[Room]): The rooms in the hotel.

        Returns:
            None
        """
        self.id = uuid.uuid4().hex
        self.name = name
        self.location = location
        self.rooms = rooms
        self.reservations = []

    def __str__(self) -> str:
        """
        Returns a string representation of the Hotel instance.

        Returns:
            str: A string representation of the Hotel instance.
        """
        return f"{self.name} in {self.location}"

    def __repr__(self) -> str:
        """
        Returns a string representation of the Hotel instance.

        Returns:
            str: A string representation of the Hotel instance.
        """
        return f"{self.name} in {self.location}"

    def display_hotel_info(self) -> None:
        """
        Display hotel information.

        Returns:
            None
        """
        print(f"Hotel: {self.name}")
        print(f"Location: {self.location}")
        print("Rooms:")
        for room in self.rooms:
            print(room)

    def add_room(self, room: Room) -> None:
        """
        Add a room to the hotel.

        Args:
            room (Room): The room to add.

        Returns:
            None
        """
        self.rooms.append(room)

    def get_room(self, room_number: str) -> Room:
        """
        Get a room from the hotel.

        Args:
            room_number (str): The room number to get.

        Returns:
            Room: The room with the given number.
        """
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    # json serialization
    def to_json(self) -> dict:
        """
        Returns a dictionary representation of the Hotel instance.

        Returns:
            dict: A dictionary representation of the Hotel instance.
        """
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "rooms": [room.to_json() for room in self.rooms],
        }
