


https://www.w3schools.com/sql/sql_ref_keywords.asp 

https://youtu.be/AZzTHWF7tEc?si=_hvLLbbUWiAMiDkf

https://www.youtube.com/watch?v=yH1zCq-iaeU&list=PLdOKnrf8EcP17p05q13WXbHO5Z_JfXNpw

a CTE allows you to define your data logic at the top, like a variable in Python or Java.
1 Better Readability 
2. Reusability within one query
If you need to use the same subset of data multiple times 

cte:
A CTE (Common Table Expression) is a temporary result set that you define at the start of a query.
 You can think of it as a temporary "view" or a named variable for a table that exists only
  while that specific query is running.
 It helps you organize complex logic into smaller, named pieces that are easier to read.

A simple CTE (Common Table Expression) query is basically a "temporary table" that you name and use within 
a single SELECT, INSERT, UPDATE, or DELETE statement.
 It helps you organize complex logic into smaller, named pieces that are easier to read.



Here is the most basic example: finding employees with a high salary using a CTE. 
'''
WITH HighEarners AS (
    -- This is the CTE definition
    SELECT name, salary, department
    FROM employees
    WHERE salary > 80000
)
-- This is the main query that uses the CTE
SELECT * 
FROM HighEarners
WHERE department = 'Engineering';
'''

windowing function
predefined function
nvl
collese lateral view
table view 
re
joins
subquery
incremetal sum
mysql interview questions 
ETL

# 8. What are the differences between CHAR and VARCHAR data types in MySQL?
# Column length is fixed in CHAR but VARCHAR length is variable.
# CHAR is faster than VARCHAR.

# DELETE is like removing specific record from a table,
# while TRUNCATE remove complete data and structure as it is .
# Drop removes both data  and structure 

# Use indexing 
# Avoid SELECT *: Only pull the columns you need. This reduces the amount of data moved from the disk to the network.
# Filter with LIMIT: If you only need 10 rows, tell MySQL to stop searching once it finds them.
# Replace Subqueries with JOINs: MySQL's optimizer is much better at handling Joins. Subqueries (especially correlated ones) can be very slow.
# Use EXISTS instead of IN: For large datasets, EXISTS is often faster because it stops searching as soon as it finds a single match.

#inner joins
# SELECT Orders.OrderID, Customers.CustomerName
# FROM Orders
# INNER JOIN Customers
# ON Orders.CustomerID=Customers.CustomerID; 


"""
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;

"""

"""
SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
FROM Orders
RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
ORDER BY Orders.OrderID;

"""

# The FULL OUTER JOIN keyword returns all matching records from both tables,
#  when there is a match in left (table1) or right (table2) table records.
"""SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2
ON table1.column_name = table2.column_name
WHERE condition;"""


#having and group by 
GROUP BY	Groups the result set (used with aggregate functions: COUNT, MAX, MIN, SUM, AVG)
HAVING	Used instead of WHERE with aggregate functions
    
# The HAVING clause was added to SQL because the WHERE keyword cannot be used with aggregate functions.
# Designed to work with aggregate functions.
"""SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5;"""

"""
The PRIMARY KEY constraint is used to uniquely identify each record in a table.
Primary keys contain unique values, and cannot contain NULL values.
Each table only ONE primary key. 

A constraint that used to link two tables together
A FOREIGN KEY is a field  in one table, that refers to the PRIMARY KEY in another table.
The table with the foreign key is called the child table,
and the table with the primary key is called the referenced or parent table.
"""
#indexex :Indexes are used to retrieve data from the database more quickly than otherwise.
# big(n)> after applying indexing in the column big(logn)
# basically it create seperate memory location where values are stored in  the sorted manner 
# in backend b trees use 
# we apply indexing in read intensive db  


#
# DELETE FROM Employees WHERE Status = 'Inactive';
# TRUNCATE TABLE Temp_Staging;
# DROP TABLE employees;


#second highest salaryy

# SELECT salary 
# FROM employees 
# ORDER BY salary DESC 
# LIMIT 1 OFFSET 1;
 
# ORDER BY salary DESC: Sorts salaries from highest to lowest.

# LIMIT 1: Tells MySQL to return only one row.

# OFFSET 1: Tells MySQL to skip the first row (the highest) and start at the second.
