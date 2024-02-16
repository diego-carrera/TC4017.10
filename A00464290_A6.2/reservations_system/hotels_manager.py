"""
Hotels Manager module for hotels reservation system
"""

import json
import os

from pathlib import Path

from reservations_system.hotel.hotel import Hotel
from reservations_system.hotel.room import Room, RoomStatus, RoomType


class HotelsManager:
    """
    Class to manage hotels for hotels reservation system
    """

    def __init__(self, hotels_file: str) -> None:
        """
        Initializes a new HotelsManager instance.

        Args:
            hotels_file (str): The path to the hotels json file.

        Returns:
            None
        """
        self.hotels_file = hotels_file
        self.hotels = []

        self._load_hotels()

    def _load_hotels(self) -> None:
        """
        Load hotels from a json file.

        Returns:
            None
        """

        if not os.path.exists(self.hotels_file):
            Path(self.hotels_file).touch()
            with open(self.hotels_file, "w", encoding="utf-8") as file:
                file.write("[]")

        with open(self.hotels_file, "r", encoding="utf-8") as file:
            hotels = json.load(file)
            for hotel in hotels:
                rooms = []
                for room in hotel["rooms"]:
                    rooms.append(
                        Room(
                            room["room_number"],
                            RoomType(room["room_type"]),
                            RoomStatus(room["room_status"]),
                            room["room_price"],
                        )
                    )
                self.hotels.append(Hotel(hotel["name"], hotel["location"], rooms))

    def _save_hotels(self) -> None:
        """
        Save hotels to a json file.

        Returns:
            None
        """

        with open(self.hotels_file, "w", encoding="utf-8") as file:
            hotels = [hotel.to_json() for hotel in self.hotels]
            json.dump(hotels, file, ensure_ascii=False, indent=4)

    def add_hotel(self, hotel: Hotel) -> None:
        """
        Add a new hotel to the system.

        Args:
            hotel (Hotel): The hotel to add to the system.

        Returns:
            None
        """
        # check if the hotel already exists
        for h in self.hotels:
            if h.name == hotel.name:
                return

        self.hotels.append(hotel)
        self._save_hotels()

    def get_hotel(self, hotel_name: str) -> Hotel:
        """
        Get a hotel from the system.

        Args:
            hotel_name (str): The name of the hotel to get from the system.

        Returns:
            Hotel: The hotel with the given name.
        """

        print(self.hotels, hotel_name)
        for hotel in self.hotels:
            if hotel.name == hotel_name:
                return hotel
        return None

    def remove_hotel(self, hotel_name: str) -> None:
        """
        Remove a hotel from the system.

        Args:
            hotel_name (str): The name of the hotel to remove from the system.

        Returns:
            None
        """
        self.hotels = [hotel for hotel in self.hotels if hotel.name != hotel_name]
        self._save_hotels()

    def edit_hotel(self, hotel_name: str, new_name: str, new_location: str) -> None:
        """
        Edit a hotel in the system.

        Args:
            hotel_name (str): The name of the hotel to edit.
            new_name (str): The new name of the hotel.
            new_location (str): The new location of the hotel.

        Returns:
            None
        """
        for hotel in self.hotels:
            if hotel.name == hotel_name:
                hotel.name = new_name
                hotel.location = new_location
        self._save_hotels()

    def display_hotel(self, hotel_name: str) -> None:
        """
        Display the details of a hotel.

        Args:
            hotel_name (str): The name of the hotel to display.

        Returns:
            None
        """
        hotel = self.get_hotel(hotel_name)
        if hotel:
            print(hotel)
        else:
            print(f"Hotel {hotel_name} not found")

    def reserve_room(self, hotel: Hotel, room: Room) -> None:
        """
        Reserve a room in a hotel for a customer.

        Args:
            hotel (Hotel): The name of the hotel.
            room (Room): The room to reserve.

        Returns:
            None
        """
        for h in self.hotels:
            if h.name == hotel.name:
                for r in h.rooms:
                    if (
                        r.room_number == room.room_number
                        and r.room_status == RoomStatus.AVAILABLE
                    ):
                        r.room_status = RoomStatus.RESERVED

        self._save_hotels()

    def cancel_reservation(self, hotel: Hotel, room: Room) -> None:
        """
        Cancel a reservation for a room in a hotel.

        Args:
            hotel (Hotel): The name of the hotel.
            room (Room): The room to cancel the reservation for.

        Returns:
            None
        """
        for h in self.hotels:
            if h.name == hotel.name:
                for r in h.rooms:
                    if r.room_number == room.room_number:
                        r.room_status = RoomStatus.AVAILABLE
        self._save_hotels()
