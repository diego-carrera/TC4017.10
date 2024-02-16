"""
Customer Manager Test cases for the CustomersManager class
"""

import unittest
import json
from pathlib import Path

from reservations_system.customer.customer import Customer

from reservations_system.customers_manager import CustomersManager


class TestCustomersManager(unittest.TestCase):
    """
    TestCustomersManager class Test cases for the CustomersManager class
    """

    def setUp(self) -> None:
        self.customers_file = "tests/customers.json"
        return super().setUp()

    def tearDown(self) -> None:
        Path(self.customers_file).unlink(missing_ok=True)
        return super().tearDown()

    def test_init(self):
        """
        Test the __init__ method
        """
        customers_manager = CustomersManager(self.customers_file)
        self.assertEqual(customers_manager.customers_file, self.customers_file)
        self.assertEqual(len(customers_manager.customers), 0)

    def test_load_customers(self):
        """
        Test the _load_customers method
        """
        customers = [
            {"name": "John Doe", "email": "jhon@email.com"},
            {"name": "Jane Doe", "email": "jane@email.com"},
        ]
        with open(self.customers_file, "w", encoding="utf-8") as file:
            json.dump(customers, file)

        customers_manager = CustomersManager(self.customers_file)
        self.assertEqual(len(customers_manager.customers), 2)
        self.assertEqual(customers_manager.customers[0].name, "John Doe")
        self.assertEqual(customers_manager.customers[0].email, "jhon@email.com")
        self.assertEqual(customers_manager.customers[1].name, "Jane Doe")
        self.assertEqual(customers_manager.customers[1].email, "jane@email.com")

    def test_add_customer(self):
        """
        Test the add_customer method
        """
        customers_manager = CustomersManager(self.customers_file)
        customers_manager.add_customer("John Doe", "john@email.com")
        self.assertEqual(len(customers_manager.customers), 1)
        self.assertEqual(customers_manager.customers[0].name, "John Doe")
        self.assertEqual(customers_manager.customers[0].email, "john@email.com")

    def test_get_customer(self):
        """
        Test the get_customer method
        """
        customers = [
            {"name": "John Doe", "email": "john@email.com"},
            {"name": "Jane Doe", "email": "jane@email.com"},
        ]
        with open(self.customers_file, "w", encoding="utf-8") as file:
            json.dump(customers, file)

        customers_manager = CustomersManager(self.customers_file)
        customer = customers_manager.get_customer("john@email.com")

        self.assertIsInstance(customer, Customer)
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.email, "john@email.com")

        none_customer = customers_manager.get_customer("non-existent")
        self.assertIsNone(none_customer)

    def test_edit_customer(self):
        """
        Test the edit_customer method
        """
        customers_manager = CustomersManager(self.customers_file)
        customer = Customer("John Doe", "john@email.com")

        customers_manager.add_customer(customer.name, customer.email)
        customers_manager.edit_customer("john@email.com", "Jane Doe", "jane@email.com")
        self.assertEqual(len(customers_manager.customers), 1)
        self.assertEqual(customers_manager.customers[0].name, "Jane Doe")
        self.assertEqual(customers_manager.customers[0].email, "jane@email.com")

    def test_remove_customer(self):
        """
        Test the remove_customer method
        """
        customers_manager = CustomersManager(self.customers_file)
        customers_manager.add_customer("John Doe", "john@email.com")
        customers_manager.remove_customer("john@email.com")
        self.assertEqual(len(customers_manager.customers), 0)

    def test_display_customer(self):
        """
        Test the display_customer method
        """
        customers = [
            {"name": "John Doe", "email": "john@email.com"},
            {"name": "Jane Doe", "email": "jane@email.com"},
        ]
        with open(self.customers_file, "w", encoding="utf-8") as file:
            json.dump(customers, file)

        customers_manager = CustomersManager(self.customers_file)
        customers_manager.display_customer("john@email.com")

        customers_manager.display_customer("non-existent")


if __name__ == "__main__":
    unittest.main()
