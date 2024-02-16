"""
Hotels test module
"""
import unittest

from reservations_system.hotel.hotel import Hotel
from reservations_system.hotel.room import Room, RoomStatus, RoomType


class TestHotel(unittest.TestCase):
    """
    TestHotel class Test cases for the Hotel class
    """

    # test __init__ method
    def test_init(self):
        """
        Test the __init__ method
        """
        hotel = Hotel("Hilton", "New York", [])
        self.assertEqual(hotel.name, "Hilton")
        self.assertEqual(hotel.location, "New York")
        self.assertEqual(hotel.rooms, [])
        self.assertEqual(hotel.reservations, [])

    # test __str__ method
    def test_str(self):
        """
        Test the __str__ method
        """
        hotel = Hotel("Hilton", "New York", [])
        self.assertEqual(str(hotel), "Hilton in New York")

    # test __repr__ method
    def test_repr(self):
        """
        Test the __repr__ method
        """
        hotel = Hotel("Hilton", "New York", [])
        self.assertEqual(repr(hotel), "Hilton in New York")

    # test display_hotel_info
    def test_display_hotel_info(self):
        """
        Test the display_hotel_info method
        """
        hotel = Hotel("Hilton", "New York", [])
        hotel.add_room(Room("101", RoomType.SINGLE, RoomStatus.AVAILABLE, 100.0))
        hotel.add_room(Room("102", RoomType.DOUBLE, RoomStatus.AVAILABLE, 200.0))
        hotel.add_room(Room("103", RoomType.SUITE, RoomStatus.AVAILABLE, 300.0))
        self.assertEqual(hotel.display_hotel_info(), None)


if __name__ == "__main__":
    unittest.main()
