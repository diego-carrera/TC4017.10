"""
Customer test module
"""

import unittest

from reservations_system.customer.customer import Customer


class TestCustomer(unittest.TestCase):
    """
    TestCustomer class Test cases for the Customer class
    """

    # test __init__ method
    def test_init(self):
        """
        Test the __init__ method
        """
        customer = Customer("John Doe", "john@email.com")
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.email, "john@email.com")

    # test __str__ method
    def test_str(self):
        """
        Test the __str__ method
        """
        customer = Customer("John Doe", "john@email.com")
        self.assertEqual(str(customer), "John Doe - john@email.com")

    # test __repr__ method
    def test_repr(self):
        """
        Test the __repr__ method
        """
        customer = Customer("John Doe", "john@email.com")
        self.assertEqual(repr(customer), "John Doe - john@email.com")

    # test display_customer_info
    def test_display_customer_info(self):
        """
        Test the display_customer_info method
        """
        customer = Customer("John Doe", "john@email.com")
        self.assertEqual(customer.display_customer_info(), None)

    def test_to_json(self):
        """
        Test the to_json method
        """
        customer = Customer("John Doe", "john@email.com")
        self.assertEqual(
            customer.to_json(),
            {"name": "John Doe", "email": "john@email.com"},
        )


if __name__ == "__main__":
    unittest.main()
