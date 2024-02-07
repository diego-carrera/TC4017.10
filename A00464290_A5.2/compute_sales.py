"""
Program: compute_sales.py
Author: Diego Carrera Nicholls A00464290
Date: 2023-01-30
Version: 1.0
Description: Compute total sales for a given dataset.
"""

import sys
import json
import time

from os.path import exists


def read_products(catalog_json: str) -> dict:
    """
    Read the product catalog from a JSON file.

    Args:
        catalog_json (str): The path to the JSON file
        containing the product catalog.

    Returns:
        dict: A dictionary representing the product catalog.
    """
    products_dict = {}
    with open(catalog_json, "r", encoding="utf-8") as file:
        products = json.load(file)
        # reducir a un diccionario title:price
        for product in products:
            name = product["title"]
            try:
                price = float(product["price"])
            except ValueError:
                print(f"Error: Price is not a number for product {name}")
                continue

            if price < 0:
                print(f"Error: Price is negative for product {name}")
                continue

            products_dict[name] = price
    return products_dict


def read_sales(sales_json: str) -> dict:
    """
    Read sales data from a JSON file.

    Args:
        sales_json (str): The path to the JSON file containing the sales data.

    Returns:
        dict: A dictionary representing the sales data.
    """
    sales_dict = {}
    with open(sales_json, "r", encoding="utf-8") as file:
        sales = json.load(file)
        # reducir a un diccionario Product:Quantity
        for sale in sales:
            product = sale["Product"]
            try:
                quantity = int(sale["Quantity"])
            except ValueError:
                print(f"Error: Quantity is not a number in sale {sale}")
                continue

            if quantity < 0:
                print(f"Error: Quantity is negative in sale {sale}")
                continue

            if product in sales_dict:
                sales_dict[product] += quantity
            else:
                sales_dict[product] = quantity
    return sales_dict


def compute_sales(products: dict, sales: dict) -> float:
    """
    Computes the total sales based on the given products and sales data.

    Args:
        products (dict): A dictionary representing the product catalog.
        sales (dict): A dictionary representing the sales data.

    Returns:
        float: The total sales amount.

    """
    total_sales = 0

    for product, quantity in sales.items():

        if product in products:
            price = products[product]
            total_sales += price * quantity
        else:
            print(f"Error: Product {product} not found in the catalog.")

    return total_sales


def write_results(total_sales: float, elapsed: float) -> None:
    """
    Writes the total sales and elapsed time to a file.

    Args:
        total_sales (float): The total sales value.
        elapsed (float): The elapsed time.

    Returns:
        None
    """
    with open("sales_results.txt", "w", encoding="utf-8") as file:
        file.write(f"Total sales:\t{total_sales:.2f}\n")
        file.write(f"Time:\t{elapsed}\n")


def main() -> None:
    """
    Main function of the program.
    Checks the command line arguments and computes the total sales.
    """

    if len(sys.argv) != 3:
        print("Usage: python compute_sales.py catalog_json sales_json")
        sys.exit(1)

    start = time.time()

    catalog_json = sys.argv[1]
    sales_json = sys.argv[2]

    if not exists(catalog_json):
        print(f"Error: {catalog_json} does not exist.")
        sys.exit(1)

    if not exists(sales_json):
        print(f"Error: {sales_json} does not exist.")
        sys.exit(1)

    products = read_products(catalog_json)
    sales = read_sales(sales_json)

    if not products or not sales:
        print("Error: No products or sales data found.")
        sys.exit(1)

    total_sales = compute_sales(products, sales)

    end = time.time()
    elapsed = end - start

    write_results(total_sales, elapsed)

    print(f"Total sales:\t{total_sales:.2f}")
    print(f"Time:\t{elapsed}")


if __name__ == "__main__":
    main()
