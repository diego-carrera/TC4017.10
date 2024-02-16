"""
Rooms test module
"""
import unittest

from reservations_system.hotel.room import Room, RoomType, RoomStatus


class TestRoom(unittest.TestCase):
    """
    TestRoom class Test cases for the Room class
    """
    # test __init__ method
    def test_init(self):
        """
        Test the __init__ method
        """
        room = Room("101", RoomType.SINGLE, RoomStatus.AVAILABLE, 100.0)
        self.assertEqual(room.room_number, "101")
        self.assertEqual(room.room_type, RoomType.SINGLE)
        self.assertEqual(room.room_status, RoomStatus.AVAILABLE)
        self.assertEqual(room.room_price, 100.0)

    # test __str__ method
    def test_str(self):
        """
        Test the __str__ method
        """
        room = Room("101", RoomType.SINGLE, RoomStatus.AVAILABLE, 100.0)
        self.assertEqual(str(room), "Room 101 - RoomType.SINGLE - RoomStatus.AVAILABLE")

    # test __repr__ method
    def test_repr(self):
        """
        Test the __repr__ method
        """
        room = Room("101", RoomType.SINGLE, RoomStatus.AVAILABLE, 100.0)
        self.assertEqual(
            repr(room), "Room 101 - RoomType.SINGLE - RoomStatus.AVAILABLE"
        )

    def test_to_json(self):
        """
        Test the to_json method
        """
        room = Room("101", RoomType.SINGLE, RoomStatus.AVAILABLE, 100.0)
        self.assertEqual(
            room.to_json(),
            {
                "id": room.id,
                "room_number": "101",
                "room_type": "single",
                "room_status": "available",
                "room_price": 100.0,
            }
        )


if __name__ == "__main__":
    unittest.main()
