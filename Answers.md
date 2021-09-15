# Winter 2022 Data Science Intern Challenge

## Question 1: 

Given some sample data, write a program to answer the following:

> On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. 

### Think about what could be going wrong with our calculation. Think about a better way to evaluate this data.
There is nothing wrong with the way that the calculations were done. The problem was with the data in the dataset. There were several extreme outliers within the dataset that are throwing off the calculation of the mean (average) of the order values. Some of these outliers, when calculating the price per unit, came out to be $25,725 for each sneaker, which is obviously wrong or an extremely rare occurrence. 

There are 2 ways that could give you a more accurate value:

1. You could simply use the median value which would actually get you closer to the actual average because this value will give you the value at the middle of all values, not the average of all values. However, this is still not going to be as accurate as the next option, but it would be the quicker way to get an estimate.

   - According to my analysis, the median of the original data is: `$284`

2. You can remove the extreme outliers from the data. Then find the mean (average) of all the remaining values. I chose to use this option to get the most accurate measure of the average order value. 

   - The value I enter for the answer to question #3 is the mean from this option. With this option, I still received a median value of `$284`, which is the same as the median with the original data but the mean has taken a dramatic change closer to this value as well.

### What metric would you report for this dataset?
It really depends on the time constraint you are under at the time of analysis. Using the median would be the better metric to use for a quick estimate on the original data. However, if you have the time to analysis the data further and find the outliers and at what value the outliers should be removed, using the mean metric is the more accurate metric. The mean metric will give you a better accuracy once the extreme values are removed from the data.

### What is its value?
The mean (*Average Order Value* (AOV)) = `$301.06`

### Files associated with this set of questions are all in this repository and include the following:
- [Joanne_Middour_Winter2022_Intern_Challenge.ipynb](https://github.com/jmmiddour/shopify_winter2022/blob/main/Joanne_Middour_Winter2022_Intern_Challenge.ipynb)
- [2019_Winter_Data_Science_Intern_Challenge_Data_Set_Sheet1.csv](https://github.com/jmmiddour/shopify_winter2022/blob/main/2019_Winter_Data_Science_Intern_Challenge_Data_Set_Sheet1.csv)
- [sneakers.py](https://github.com/jmmiddour/shopify_winter2022/blob/main/sneakers.py)


## Question 2: 

For this question you’ll need to use SQL. 

Please use queries to answer the following questions. Paste your queries along with your final numerical answers below.

### How many orders were shipped by Speedy Express in total?
1. **My thought process:**

   1. Need to find what table(s) have the shipper names listed.
   
      - I found the shipper names and id numbers in the `Shippers` table and this is the only table with the `ShipperName` listed
      
   2. Next need to know which table(s) has all the orders that each shipper shipped.
   
      - I found all orders and shipper ids are in the `Orders` table and it is the only other table with the `ShipperID` listed
      
   3. Now I know that I need to `JOIN` the `Shippers` and `Orders` tables together on the `ShipperID` column.
   
   4. Finally, I need to just print out the `COUNT` of the total orders that were shipped by "Speedy Express" only.
   
2. **My query:**

   ```
   SELECT COUNT(ord.ShipperID)
   FROM Shippers AS ship 
      JOIN Orders AS ord ON Ord.ShipperID = ship.ShipperID
   WHERE ship.ShipperName = "Speedy Express";
   ```
   
3. **My Result --> `54`**

4. There is two other ways that I could have accomplished this same task without having to join the tables. 

   1. I could have also just looked at the `Shippers` table, since there are only 3 shippers, and seen that the `ShipperID` is `1` for "Speedy Express" and just ran the following query: 
      
      ```
      SELECT COUNT(ShipperID)
      FROM Orders
      WHERE ShipperID = 1;

      Result --> 54
      ```
      
      - This would give me the same result but would not be a feasible solution for a larger database.

   2. I could have also created two queries as follows if the `Shipper` table was larger and the `ShipperID` was not as easily found:
   
      ```
      SELECT ShipperID
      FROM Shippers
      WHERE ShipperName = "Speedy Express";

      Result --> 1
   
      SELECT COUNT(ShipperID)
      FROM Orders
      WHERE ShipperID = 1;
   
      Result --> 54
      ```
      
      - This way I would get the same result, but it would have taken me longer to get there and would have required an additional query.

### What is the last name of the employee with the most orders?
1. **My thought process:**

   1. I need to know what table(s) has the employee last names and what information is stored there.
   
      - I found the `Employees` table has the `LastName` of each of the employees and their `EmployeeID` and is the only table with the employees `LastName` listed
   
   2. Next I need to find the table(s) with the `EmployeeID` and the orders each employee processed based on their id number.
   
      - I found that the `Orders` table has all the information that I need to connect back to the `Employees` table and get the name of the employee with the most orders and it is the only other table with the `EmployeeID` listed
   
   3. Going to need to `JOIN` the `Orders` and `Employees` table on the `EmployeeID` column.

   4. Will then need to calculate the total number of orders for each employee based on their `EmployeeID`.
   
   5. Those totals will then need to be sorted by the total values in descending order.

   6. Finally, I will return only the `LastName` at the top of the results because I only need the top employee.

2. **My query:**

   ```
   SELECT emp.LastName
   FROM Employees AS emp
       JOIN Orders AS ord ON ord.EmployeeID = emp.EmployeeID
   GROUP BY emp.EmployeeID
   ORDER BY COUNT(emp.EmployeeID) DESC
   LIMIT 1;
   ```
   
3. **My Result --> `Peacock`**
   
### What product was ordered the most by customers in Germany?
1. **My thought process:**

   1. I need to find the table(s) has the customer's country listed and what information is stored there.
   
      - I found the `Customers` table is the only file with the `Country` listed where the customer resides.
   
   2. Next I need to find the table(s) with the `CustomerID` and the products purchased based on their id number.
   
      - I found that the `Orders` table is the only table with the `CustomerID` listed but there is nothing about the products they purchased. So going to use the `OrderID` to find out what products they ordered

      - The only other table I can find `OrderID` is in the `OrderDetails` table, but still do not have the product information yet. I will need to use `ProductID` in this table to connect to another table to get the product information

      - Now I have finally found the `ProductName` in the `Products` table, and it is the only other table with the `ProductID` listed

   3. Now that I know where all my connections are, I will need to do 3 inner joins in order to get all the information linked into one table.
   
   4. I will also need a conditional statement to only add the customers that reside in Germany.

   5. Then I need to get a total for each product and sort all of those totals in descending order.

   6. Finally, will need to return the first value in the `ProductName` column only because we only need the top product.

3. **My query:**

   ```
   SELECT prod.ProductName
   FROM Products AS prod
       JOIN OrderDetails AS details ON details.ProductID = prod.ProductID
       JOIN Orders AS ord ON ord.OrderID = details.OrderID
       JOIN Customers AS cust ON cust.CustomerID = ord.CustomerID
   WHERE cust.Country = "Germany"
   GROUP BY prod.ProductName
   ORDER BY SUM(details.Quantity) DESC
   LIMIT 1;
   ```
   
4. **My Result --> `Boston Crab Meat`**


### Files associated with this set of questions are all in this repository and include the following:
- [orders_db.sqlite3](https://github.com/jmmiddour/shopify_winter2022/blob/main/orders_db.sqlite3)
- [orders_queries.py](https://github.com/jmmiddour/shopify_winter2022/blob/main/orders_queries.py)
