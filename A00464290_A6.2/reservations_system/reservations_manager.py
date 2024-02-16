"""
Reservations Manager module for hotels reservation system
"""
import os
import json

from pathlib import Path

from reservations_system.hotel.room import RoomStatus
from reservations_system.reservation.reservation import Reservation


class ReservationsManager:
    """
    Class to manage reservations for hotels
    """

    def __init__(self, reservations_file: str) -> None:
        """
        Initializes a new ReservationsManager instance.

        Args:
            hotels_file (str): The path to the hotels json file.
            customers_file (str): The path to the customers json file.
            reservations_file (str): The path to the reservations json file.

        Returns:
            None
        """
        self.reservations_file = reservations_file

        self.reservations = []

        self._load_reservations()

    def _load_reservations(self) -> None:
        """
        Load reservations from a json file.

        Returns:
            None
        """

        if not os.path.exists(self.reservations_file):
            Path(self.reservations_file).touch()
            with open(self.reservations_file, "w", encoding="utf-8") as file:
                file.write("[]")

        with open(self.reservations_file, "r", encoding="utf-8") as file:
            reservations = json.load(file)
            for reservation in reservations:
                self.reservations.append(reservation)
                # self.reservations.append(
                #     Reservation(
                #         reservation["hotel"],
                #         CustomersManager.get_customer(reservation["customer"]),
                #         reservation["room"],
                #         reservation["check_in"],
                #         reservation["check_out"],
                #         reservation["id"],
                #     )
                # )

    def _save_reservations(self) -> None:
        """
        Save reservations to a json file.

        Returns:
            None
        """

        with open(self.reservations_file, "w", encoding="utf-8") as file:
            reservations = [reservation.to_json() for reservation in self.reservations]
            json.dump(reservations, file, ensure_ascii=False, indent=4)

    def reserve_room(self, **kwargs) -> Reservation:
        """
        Reserve a room in a hotel for a customer.

        Args:
            hotel (Hotel): The name of the hotel.
            room (Room): The room to reserve.
            customer (Customer): The customer making the reservation.
            check_in (datetime): The check-in date and time.
            check_out (datetime): The check-out date and time.

        Returns:
            Reservation: The reservation made by the customer.
        """

        hotel = kwargs.get("hotel")
        room = kwargs.get("room")
        customer = kwargs.get("customer")
        check_in = kwargs.get("check_in")
        check_out = kwargs.get("check_out")

        if room.room_status == RoomStatus.AVAILABLE:
            # change room status
            room.room_status = RoomStatus.RESERVED
            reservation = Reservation(hotel, customer, room, check_in, check_out)
            self.reservations.append(reservation)

            self._save_reservations()
            return reservation

        return None

    def cancel_reservation(self, reservation_id: str) -> None:
        """
        Cancel a reservation.

        Args:
            reservation_id (str): The id of the reservation to cancel.

        Returns:
            None
        """
        self.reservations = [
            reservation
            for reservation in self.reservations
            if reservation.id != reservation_id
        ]
        self._save_reservations()
