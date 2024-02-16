"""
HotelsManager tests
"""

import unittest
import json
from pathlib import Path

from reservations_system.hotel.hotel import Hotel
from reservations_system.hotel.room import Room, RoomStatus, RoomType
from reservations_system.hotels_manager import HotelsManager


class TestHotelsManager(unittest.TestCase):
    """
    TestHotelsManager class Test cases for the HotelsManager class
    """

    def tearDown(self) -> None:
        hotels_file = "tests/hotels.json"
        Path(hotels_file).unlink(missing_ok=True)
        return super().tearDown()

    def test_init(self):
        """
        Test the __init__ method
        """
        hotels_file = "tests/hotels.json"
        with open(hotels_file, "w", encoding="utf-8") as file:
            file.write("[]")

        hotels_manager = HotelsManager(hotels_file)
        self.assertEqual(hotels_manager.hotels_file, hotels_file)
        self.assertEqual(len(hotels_manager.hotels), 0)

    def test_init_empty(self):
        """
        Test the __init__ method with an empty file
        """
        hotels_file = "tests/hotels.json"
        hotels_manager = HotelsManager(hotels_file)
        self.assertEqual(hotels_manager.hotels_file, hotels_file)
        self.assertEqual(len(hotels_manager.hotels), 0)

    def test_load_hotels(self):
        """
        Test the _load_hotels method
        """
        hotels_file = "tests/hotels.json"
        with open(hotels_file, "w", encoding="utf-8") as file:
            file.write(
                json.dumps(
                    [
                        {
                            "name": "hotel1",
                            "location": "location1",
                            "rooms": [
                                {
                                    "room_number": "101",
                                    "room_type": "single",
                                    "room_status": "available",
                                    "room_price": 100,
                                }
                            ],
                        }
                    ]
                )
            )

        hotels_manager = HotelsManager(hotels_file)
        self.assertEqual(len(hotels_manager.hotels), 1)
        self.assertIsInstance(hotels_manager.hotels[0], Hotel)
        self.assertEqual(hotels_manager.hotels[0].name, "hotel1")
        self.assertEqual(hotels_manager.hotels[0].location, "location1")
        self.assertEqual(len(hotels_manager.hotels[0].rooms), 1)
        self.assertIsInstance(hotels_manager.hotels[0].rooms[0], Room)
        self.assertEqual(hotels_manager.hotels[0].rooms[0].room_number, "101")
        self.assertEqual(hotels_manager.hotels[0].rooms[0].room_type, RoomType.SINGLE)

    def test_add_hotel(self):
        """
        Test the add_hotel method
        """

        hotels_file = "tests/hotels.json"
        with open(hotels_file, "w", encoding="utf-8") as file:
            file.write("[]")

        hotels_manager = HotelsManager(hotels_file)
        hotel = Hotel("hotel1", "location1", [])
        hotels_manager.add_hotel(hotel)
        self.assertEqual(len(hotels_manager.hotels), 1)
        self.assertIsInstance(hotels_manager.hotels[0], Hotel)
        self.assertEqual(hotels_manager.hotels[0].name, "hotel1")
        self.assertEqual(hotels_manager.hotels[0].location, "location1")
        self.assertEqual(len(hotels_manager.hotels[0].rooms), 0)

        hotels_manager.add_hotel(hotel)
        self.assertEqual(len(hotels_manager.hotels), 1)

    def test_get_hotel(self):
        """
        Test the get_hotel method
        """

        hotels_file = "tests/hotels.json"
        with open(hotels_file, "w", encoding="utf-8") as file:
            file.write(
                json.dumps(
                    [
                        {
                            "name": "hotel1",
                            "location": "location1",
                            "rooms": [
                                {
                                    "room_number": "101",
                                    "room_type": "single",
                                    "room_status": "available",
                                    "room_price": 100,
                                }
                            ],
                        }
                    ]
                )
            )

        hotels_manager = HotelsManager(hotels_file)
        hotel = hotels_manager.get_hotel("hotel1")

        self.assertIsInstance(hotel, Hotel)
        self.assertEqual(hotel.name, "hotel1")
        self.assertEqual(hotel.location, "location1")
        self.assertEqual(len(hotel.rooms), 1)
        self.assertIsInstance(hotel.rooms[0], Room)
        self.assertEqual(hotel.rooms[0].room_number, "101")
        self.assertEqual(hotel.rooms[0].room_type, RoomType.SINGLE)

        none_hotel = hotels_manager.get_hotel("hotel2")
        self.assertEqual(none_hotel, None)

    def test_remove_hotel(self):
        """
        Test the remove_hotel method
        """

        hotels_file = "tests/hotels.json"
        with open(hotels_file, "w", encoding="utf-8") as file:
            file.write(
                json.dumps(
                    [
                        {
                            "name": "hotel1",
                            "location": "location1",
                            "rooms": [
                                {
                                    "room_number": "101",
                                    "room_type": "single",
                                    "room_status": "available",
                                    "room_price": 100,
                                }
                            ],
                        }
                    ]
                )
            )

        hotels_manager = HotelsManager(hotels_file)
        hotels_manager.remove_hotel("hotel1")
        self.assertEqual(len(hotels_manager.hotels), 0)

    def test_edit_hotel(self):
        """
        Test the edit_hotel method
        """
        hotels_file = "tests/hotels.json"
        with open(hotels_file, "w", encoding="utf-8") as file:
            file.write(
                json.dumps(
                    [
                        {
                            "name": "hotel1",
                            "location": "location1",
                            "rooms": [
                                {
                                    "room_number": "101",
                                    "room_type": "single",
                                    "room_status": "available",
                                    "room_price": 100,
                                }
                            ],
                        }
                    ]
                )
            )

        hotels_manager = HotelsManager(hotels_file)
        hotels_manager.edit_hotel("hotel1", "hotel2", "location2")

        hotel = hotels_manager.get_hotel("hotel2")

        self.assertIsInstance(hotel, Hotel)
        self.assertEqual(hotel.name, "hotel2")
        self.assertEqual(hotel.location, "location2")
        self.assertEqual(len(hotel.rooms), 1)

    def test_display_hotel(self):
        """
        Test the display_hotel method
        """
        hotels_file = "tests/hotels.json"
        with open(hotels_file, "w", encoding="utf-8") as file:
            file.write(
                json.dumps(
                    [
                        {
                            "name": "hotel1",
                            "location": "location1",
                            "rooms": [
                                {
                                    "room_number": "101",
                                    "room_type": "single",
                                    "room_status": "available",
                                    "room_price": 100,
                                }
                            ],
                        }
                    ]
                )
            )

        hotels_manager = HotelsManager(hotels_file)
        hotels_manager.display_hotel("hotel1")
        hotels_manager.display_hotel("hotel2")

    def test_reserve_room(self):
        """
        Test the reserve_room method
        """
        hotels_file = "tests/hotels.json"
        with open(hotels_file, "w", encoding="utf-8") as file:
            file.write(
                json.dumps(
                    [
                        {
                            "name": "hotel1",
                            "location": "location1",
                            "rooms": [
                                {
                                    "room_number": "101",
                                    "room_type": "single",
                                    "room_status": "available",
                                    "room_price": 100,
                                }
                            ],
                        }
                    ]
                )
            )

        hotels_manager = HotelsManager(hotels_file)
        hotel = hotels_manager.get_hotel("hotel1")
        room = hotel.get_room("101")

        hotels_manager.reserve_room(hotel, room)
        self.assertEqual(room.room_status, RoomStatus.RESERVED)

    def test_cancel_reservation(self):
        """
        Test the cancel_reservation method
        """
        hotels_file = "tests/hotels.json"
        with open(hotels_file, "w", encoding="utf-8") as file:
            file.write(
                json.dumps(
                    [
                        {
                            "name": "hotel1",
                            "location": "location1",
                            "rooms": [
                                {
                                    "room_number": "101",
                                    "room_type": "single",
                                    "room_status": "reserved",
                                    "room_price": 100,
                                }
                            ],
                        }
                    ]
                )
            )

        hotels_manager = HotelsManager(hotels_file)
        hotel = hotels_manager.get_hotel("hotel1")
        room = hotel.get_room("101")

        hotels_manager.cancel_reservation(hotel, room)
        self.assertEqual(room.room_status, RoomStatus.AVAILABLE)


if __name__ == "__main__":
    unittest.main()
