"""
Customer class
"""


class Customer:
    """
    Customer class
    """

    def __init__(self, name: str, email: str) -> None:
        """
        Initializes a new Customer instance.

        Args:
            name (str): The name of the customer.
            email (str): The email of the customer.

        Returns:
            None
        """

        self.name = name
        self.email = email

    def __str__(self) -> str:
        """
        Returns a string representation of the Customer instance.

        Returns:
            str: A string representation of the Customer instance.

        """
        return f"{self.name} - {self.email}"

    def __repr__(self) -> str:
        """
        Returns a string representation of the Customer instance.

        Returns:
            str: A string representation of the Customer instance.

        """
        return f"{self.name} - {self.email}"

    def display_customer_info(self) -> None:
        """
        Display customer information.

        Returns:
            None
        """
        print(f"Customer: {self.name} - {self.email}")

    # json serialization
    def to_json(self) -> dict:
        """
        Returns a dictionary representation of the Customer instance.

        Returns:
            dict: A dictionary representation of the Customer instance.

        """
        return {
            "name": self.name,
            "email": self.email,
        }
