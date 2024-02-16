"""
Reservations Manager Test
"""

import unittest
import json
from pathlib import Path
from reservations_system.customer.customer import Customer
from reservations_system.hotel.hotel import Hotel
from reservations_system.hotel.room import Room, RoomStatus, RoomType
from reservations_system.reservation.reservation import Reservation

from reservations_system.reservations_manager import ReservationsManager


class TestReservationsManager(unittest.TestCase):
    """
    TestReservationsManager class Test cases for the ReservationsManager class
    """

    def tearDown(self) -> None:
        Path("tests/reservations.json").unlink(missing_ok=True)
        return super().tearDown()

    def test_init(self):
        """
        Test the __init__ method
        """
        reservations_manager = ReservationsManager("tests/reservations.json")
        self.assertEqual(
            reservations_manager.reservations_file, "tests/reservations.json"
        )
        self.assertEqual(reservations_manager.reservations, [])

    def test_load_reservations(self):
        """
        Test the _load_reservations method
        """
        reservations = [
            {
                "id": 1,
                "hotel": "Hilton",
                "customer": 1,
                "room": "101",
                "check_in": "2021-01-01",
                "check_out": "2021-01-02",
            }
        ]
        with open("tests/reservations.json", "w", encoding="utf-8") as file:
            json.dump(reservations, file)

        reservations_manager = ReservationsManager("tests/reservations.json")
        self.assertEqual(len(reservations_manager.reservations), 1)
        self.assertEqual(reservations_manager.reservations[0]["id"], 1)
        self.assertEqual(reservations_manager.reservations[0]["hotel"], "Hilton")
        self.assertEqual(reservations_manager.reservations[0]["customer"], 1)
        self.assertEqual(reservations_manager.reservations[0]["room"], "101")
        self.assertEqual(reservations_manager.reservations[0]["check_in"], "2021-01-01")
        self.assertEqual(
            reservations_manager.reservations[0]["check_out"], "2021-01-02"
        )

    def test_load_reservations_no_file(self):
        """
        Test the _load_reservations method with no file
        """
        reservations_manager = ReservationsManager("tests/non-existent.json")
        self.assertEqual(reservations_manager.reservations, [])
        self.assertTrue(Path("tests/non-existent.json").exists())

    def test_reserve_room(self):
        """
        Test the reserve_room method
        """
        reservations_manager = ReservationsManager("tests/reservations.json")

        room = Room("101", RoomType.SINGLE, RoomStatus.AVAILABLE, 100.0)
        hotel = Hotel("Hilton", "New York", [room])
        customer = Customer("John Doe", "john@email.com")

        reservation = reservations_manager.reserve_room(
            hotel=hotel,
            room=room,
            customer=customer,
            check_in="2021-01-01",
            check_out="2021-01-02",
        )
        # check instance type
        self.assertIsInstance(reservation, Reservation)
        # check reservation details
        self.assertEqual(reservation.hotel, hotel)
        self.assertEqual(reservation.customer, customer)
        self.assertEqual(reservation.room, room)
        self.assertEqual(reservation.check_in, "2021-01-01")
        self.assertEqual(reservation.check_out, "2021-01-02")
        # check room status
        self.assertEqual(room.room_status, RoomStatus.RESERVED)

    def test_cancel_reservation(self):
        """
        Test the cancel_reservation method
        """

        reservations_manager = ReservationsManager("tests/reservations.json")

        room = Room("101", RoomType.SINGLE, RoomStatus.AVAILABLE, 100.0)
        hotel = Hotel("Hilton", "New York", [room])
        customer = Customer("John Doe", "john@email.com")

        reservation = reservations_manager.reserve_room(
            hotel=hotel,
            room=room,
            customer=customer,
            check_in="2021-01-01",
            check_out="2021-01-02",
        )
        # check instance type
        self.assertIsInstance(reservation, Reservation)

        reservations_manager.cancel_reservation(reservation.id)

        self.assertEqual(len(reservations_manager.reservations), 0)


if __name__ == "__main__":
    unittest.main()
