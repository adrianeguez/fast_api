# Fastapi

```bash
conda create --name myFastApiEnv
conda activate myFastApiEnv
conda deactivate
conda install pip
pip install "fastapi[all]"
```

orjson > faster
json > edge cases

```bash
conda install pip
pip install "fastapi[all]"
pip install -r requirements.txt
pip install flake8
flake8 path/to/code/
django-admin startproject app
```

## SQLModel

### add

```python
def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)

        session.commit()
        ## Update works individually
        session.refresh(hero_1) ## Update those records that are not refreshed in code
        session.refresh(hero_2) ## Update those records that are not refreshed in code
        session.refresh(hero_3) ## Update those records that are not refreshed in code
    # session = Session(engine)
    # 
    # session.add(hero_1)
    # session.add(hero_2)
    # session.add(hero_3)
    # 
    # session.commit()
    # session.close() ## Close automatically using "with"
```

#SQL
```sql
SELECT CustomerName, City FROM Customers; -- Select
SELECT DISTINCT Country FROM Customers; -- Distintos
SELECT * FROM Customers WHERE Country='Mexico'; -- Filtrando 
SELECT * FROM Products ORDER BY Price; -- Ordenando
SELECT * FROM Customers WHERE Country = 'Spain' AND CustomerName LIKE 'G%'; -- AND
SELECT * FROM Customers WHERE Country = 'Germany' OR Country = 'Spain'; -- OR
SELECT * FROM Customers WHERE NOT Country = 'Spain'; -- NOT
SELECT * FROM Customers WHERE Country IS NULL; -- IS NULL
SELECT * FROM Customers WHERE Country IS NOT NULL; -- IS NOT NULL
-- Aggregations
SELECT MIN(Price) FROM Products; -- MIN
SELECT MAX(Price) FROM Products; -- MAX 
SELECT COUNT(*) FROM Products; -- COUNT
SELECT SUM(Quantity) FROM OrderDetails; -- SUM
SELECT AVG(Price) FROM Products; -- AVG
SELECT * FROM Customers WHERE CustomerName LIKE 'a%'; -- LIKE
SELECT * FROM Customers WHERE Country IN ('Germany', 'France', 'UK'); -- IN (array)
SELECT * FROM Products WHERE Price BETWEEN 10 AND 20; -- Between
SELECT CustomerID AS ID FROM Customers; -- Alias
-- JOINS
-- INNER JOIN (intersection)
-- LEFT JOIN (left table)
-- RIGHT JOIN (right table)
-- FULL OUTER JOIN (both tables)
SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders 
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID; -- INNER JOIN
-- UNION
-- Every SELECT statement within UNION must have the same number of columns
-- The columns must also have similar data types
-- The columns in every SELECT statement must also be in the same order
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City; -- UNION
               
SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers
ORDER BY City; -- UNION ALL

SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City; -- Union with WHERE

SELECT City, Country FROM Customers
WHERE Country='Germany'
UNION ALL
SELECT City, Country FROM Suppliers
WHERE Country='Germany'
ORDER BY City; -- Union all with WHERE
-- GROUP BY
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country; -- Group by

SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
ORDER BY COUNT(CustomerID) DESC; -- Group by order by

SELECT Shippers.ShipperName, COUNT(Orders.OrderID) AS NumberOfOrders FROM Orders
LEFT JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID
GROUP BY ShipperName; -- Group by left join
-- HAVING
-- The HAVING clause was added to SQL because the WHERE keyword cannot be used with aggregate functions.
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5
ORDER BY COUNT(CustomerID) DESC; -- HAVING
--EXISTS
SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price < 20); --EXISTS
-- ANY
SELECT ProductName
FROM Products
WHERE ProductID = ANY
      (SELECT ProductID
       FROM OrderDetails
       WHERE Quantity = 10); -- ANY (alguno cumple la condicion retorna TRUE sino FALSE)
-- ALL
SELECT ProductName
FROM Products
WHERE ProductID = ALL
      (SELECT ProductID
       FROM OrderDetails
       WHERE Quantity = 10); -- ALL (todos cumplen la condicion retorna TRUE sino FALSE)
``` 