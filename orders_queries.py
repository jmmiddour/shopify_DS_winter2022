# Imports
import sqlite3

# Create connection to database
conn = sqlite3.connect('orders_db.sqlite3')
cur = conn.cursor()


def get_query_results(query, title=None):
    """
    Function to execute the query specified and print the result to the terminal

    :param
        query : *str* :
            SQL query to be executed on the database

        title : *str* :
            the title to be printed with the result

    :return:
         Prints the given title and result in the terminal
    """
    res = cur.execute(query).fetchone()
    print(f'{title}{res[0]}')


# Set up my titles
title1 = 'Total Number of Orders Shipped by Speedy Express: '
title2 = 'The Last Name of the Employee with the Most Orders: '
title3 = 'The Product Ordered the Most by Customers in Germany: '

# Set up my Queries
query1 = """
    SELECT COUNT(ord.ShipperID)
    FROM Shippers AS ship 
        JOIN Orders AS ord ON Ord.ShipperID = ship.ShipperID
    WHERE ship.ShipperName = "Speedy Express";
"""
query2 = """
    SELECT emp.LastName
    FROM Employees AS emp
        JOIN Orders AS ord ON ord.EmployeeID = emp.EmployeeID
    GROUP BY emp.EmployeeID
    ORDER BY COUNT(emp.EmployeeID) DESC
    LIMIT 1;
"""
query3 = """
    SELECT prod.ProductName
    FROM Products AS prod
        JOIN OrderDetails AS details ON details.ProductID = prod.ProductID
        JOIN Orders AS ord ON ord.OrderID = details.OrderID
        JOIN Customers AS cust ON cust.CustomerID = ord.CustomerID
    WHERE cust.Country = "Germany"
    GROUP BY prod.ProductName
    ORDER BY SUM(details.Quantity) DESC
    LIMIT 1;
"""

# Add all my titles and queries to a dictionary
query_dict = {
    title1: query1,
    title2: query2,
    title3: query3
}

# Iterate through my dictionary and execute all my queries and print them
for k, v in query_dict.items():
    get_query_results(v, k)
