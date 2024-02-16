"""
Customers manager module
"""

import json
import os
from pathlib import Path

from reservations_system.customer.customer import Customer


class CustomersManager:
    """
    Class to manage customers for hotels reservation system
    """

    def __init__(self, customers_file: str) -> None:
        """
        Initializes a new CustomersManager instance.

        Args:
            customers_file (str): The path to the customers json file.

        Returns:
            None
        """
        self.customers_file = customers_file
        self.customers = []

        self._load_customers()

    def _load_customers(self) -> None:
        """
        Load customers from a json file.

        Returns:
            None
        """
        if not os.path.exists(self.customers_file):
            Path(self.customers_file).touch()
            with open(self.customers_file, "w", encoding="utf-8") as file:
                file.write("[]")

        with open(self.customers_file, "r", encoding="utf-8") as file:
            customers = json.load(file)
            for customer in customers:
                self.customers.append(Customer(customer["name"], customer["email"]))

    def _save_customers(self) -> None:
        """
        Save customers to a json file.

        Returns:
            None
        """

        with open(self.customers_file, "w", encoding="utf-8") as file:
            customers = [customer.to_json() for customer in self.customers]
            json.dump(customers, file, ensure_ascii=False, indent=4)

    def add_customer(self, name: str, email: str) -> None:
        """
        Add a new customer to the customers list.

        Args:
            name (str): The name of the customer.
            email (str): The email of the customer.

        Returns:
            None
        """
        self.customers.append(Customer(name, email))
        self._save_customers()

    def remove_customer(self, email: str) -> None:
        """
        Remove a customer from the customers list.

        Args:
            email (str): The email of the customer.

        Returns:
            None
        """
        self.customers = [
            customer for customer in self.customers if customer.email != email
        ]
        self._save_customers()

    def edit_customer(self, email: str, new_name: str, new_email: str) -> None:
        """
        Edit a customer in the customers list.

        Args:
            email (str): The email of the customer to edit.
            new_name (str): The new name of the customer.
            new_email (str): The new email of the customer.

        Returns:
            None
        """
        for customer in self.customers:
            if customer.email == email:
                customer.name = new_name
                customer.email = new_email
        self._save_customers()

    def get_customer(self, email: str) -> Customer:
        """
        Get a customer from the customers list.

        Args:
            email (str): The email of the customer to get.

        Returns:
            Customer: The customer with the given email.
        """
        for customer in self.customers:
            if customer.email == email:
                return customer
        return None

    def display_customer(self, email: str) -> None:
        """
        Display the details of a customer.

        Args:
            email (str): The email of the customer to display.
        """
        customer = self.get_customer(email)
        if customer:
            print(customer)
        else:
            print(f"Customer with email {email} not found.")
