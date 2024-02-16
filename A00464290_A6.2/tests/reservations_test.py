"""
Reservations test modules
"""

import unittest

from reservations_system.hotel.hotel import Hotel
from reservations_system.customer.customer import Customer
from reservations_system.hotel.room import Room, RoomType, RoomStatus

from reservations_system.reservation.reservation import Reservation


class TestReservation(unittest.TestCase):
    """
    TestReservation class Test cases for the Reservation class
    """

    # test __init__ method
    def test_init(self):
        """
        Test the __init__ method
        """
        hotel = Hotel("Hilton", "New York", [])
        customer = Customer("John Doe", "john@email.com")
        room = Room("101", RoomType.SINGLE, RoomStatus.AVAILABLE, 100.0)
        reservation = Reservation(hotel, customer, room, "2021-01-01", "2021-01-03")
        self.assertEqual(reservation.hotel, hotel)
        self.assertEqual(reservation.customer, customer)
        self.assertEqual(reservation.room, room)
        self.assertEqual(reservation.check_in, "2021-01-01")
        self.assertEqual(reservation.check_out, "2021-01-03")

    # test __str__ method
    def test_str(self):
        """
        Test the __str__ method
        """
        hotel = Hotel("Hilton", "New York", [])
        customer = Customer("John Doe", "john@email.com")
        room = Room("101", RoomType.SINGLE, RoomStatus.AVAILABLE, 100.0)
        reservation = Reservation(hotel, customer, room, "2021-01-01", "2021-01-03")

        self.assertEqual(
            str(reservation),
            "Reservation for John Doe at Hilton from 2021-01-01 to 2021-01-03",
        )

    # test __repr__ method
    def test_repr(self):
        """
        Test the __repr__ method
        """
        hotel = Hotel("Hilton", "New York", [])
        customer = Customer("John Doe", "john@email.com")
        room = Room("101", RoomType.SINGLE, RoomStatus.AVAILABLE, 100.0)
        reservation = Reservation(hotel, customer, room, "2021-01-01", "2021-01-03")

        self.assertEqual(
            repr(reservation),
            "Reservation for John Doe at Hilton from 2021-01-01 to 2021-01-03",
        )


if __name__ == "__main__":
    unittest.main()
