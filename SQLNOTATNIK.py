import SQLNOTATNIK

SQLLITE

SELECT prod_name, prod_id, prod_price
FROM Products;


            LUB

SELECT prod_name
       ,prod_id
       ,prod_price
FROM Products;



SELECT *   (wszystkie kolumny)
FROM Products;



SELECT prod_name
FROM Products;
LIMIT 5;


INSERT INTO Shoes
        (ID
         ,Brand
         ,Type
         ,Color
         ,Price
         ,Desc
         )
VALUES ('1234'
        ,'Gucci'
        ,'klapki'
        ,'czerwone'
        ,'45.00'
        ,NULL
        );



CREATE TEMPORARY TABLE Sandals AS
    (
        SELECT *
        FROM Shoes
        WHERE shoe_type = 'sandals'
    )



ADDING COMMENTS
/*      /*




WHERE

SELECT column_name, column_name
FROM table_name
WHERE column_name operator_value;

WHERE operators:             PRZYKLADY
=                            WHERE ProductName = "Tofu" ProductPrice = 50;
<> (inne wersje sql != )     WHERE ProductName <>"Ketchup";
>
<
>=
<=
BETWEEN                      WHERE UnitsInStock BETWEEN 20 AND 100;
IS NULL                      WHERE ProductName IS NULL;

PRZYKLAD:
SELECT ProductName, UnitPrice, SupplierID
FROM Products
WHERE productname = "Tofu";

BETWEEN


IN

pisze sie w ( )

SELECT ProductName, UnitPrice, SupplierID
FROM Products
WHERE SupplierID IN (9,10,11);
lub
WHERE ProductType IN ("ketchup", "majonez", "musztarda")

OR

SELECT ProductName, UnitPrice, SupplierID
FROM Products
WHERE ProductName = "Tofu" OR "Cheese";

Jak znajdzie tofu to juz nie bedzie szukal cheese KOLEJNOSC ma znaczenie!!!!
Generalnie IN lepsze

OR with AND

SELECT ProductName, UnitPrice, SupplierID
FROM Products
WHERE SupplierID = 9 OR SupplierID = 11
w Pierwszym przykladzie mozemy dostac wyniki z unit price mniejszym niz 15 bo SQL czyta OR przed  AND
WHERE (SupplierID = 9 OR SupplierID = 11)  ROZNICA Z () I BEZ!!!! teraz wyniki tylko z unitprice > 15


AND UnitPrice >15;

NOT

SELECT *
FROM Employees
WHERE NOT City="Radom" AND NOT City="Kielce";


WILDCARDS

Tylko do uzycia z tekstem/stringami
"%Pizza" - łapie wszystko co sie konczy slowem Pizza
"Pizza%" - łapie wszystko co jest po słowie Pizza
"%Pizza%" - wszystko przed i po pizza
"S%E" - łapie wsio co znajduje sie pomiedzy S i E np Sadie
"t%@gmail.com" - łapie emaile zacz sie na t w gmailu

WILDACARDy nie wylapuja NULLi

LIKE

*	Represents zero or more characters	bl* finds bl, black, blue, and blob
?	Represents a single character	h?t finds hot, hat, and hit
[]	Represents any single character within the brackets	h[oa]t finds hot and hat, but not hit NIE DZIALA W SQLITE
!	Represents any character not in the brackets	h[!oa]t finds hit, but not hot and hat
-	Represents any single character within the specified range	c[a-b]t finds cat and cbt
#	Represents any single numeric character	2#5 finds 205, 215, 225, 235, 245, 255, 265, 275, 285, and 295


ORDER BY

SELECT something
FROM database
ORDER BY characteristic

ORDER BY moze:
brac pod uwage wiecej niz 1 kolumne
Przecinek po kazdej nazwie kolejnej kolumny
Musi byc ostatnim warunkiem selecta
Mozna sortowac po kolumnie ktorej nie selectowalismy w zapytaniu

np
ORDER BY kolumna2 ASC, kolumna3 DESC

DESC - descending
ASC   - ascending


GROUP BY

SELECT Region, COUNT(CustomerID) AS total_customers
FROM Customers
GROUP BY Region;


HAVING

SELECT CustomerID, COUNT (*) AS orders
FROM Orders
GROUP BY CustomerId
HAVING COUNT (*) >=2;



AVERAGE
AVG()

SELECT AVG(UnitPrice) AS avg_price
FROM Products

COUNT()
SELECT COUNT(CustomerID) AS Total_Customers  #IGNORUJE NULLe
FROM Customers;

SELECT COUNT(*) AS Total_Customers  #LICZY WSZYSTKIE ROWy z value or NULL
FROM Customers;

MIN() / MAX()  # IGNORUJA NULLe

SELECT MAX(UnitPrice) AS max_prod_price, MIN(UnitPrice) AS min_prod_price
FROM Products

przyklad z zadan:
SELECT
MIN(Biweekly_High_Rate)
From salary_range_by_job_classification
GROUP BY Biweekly_High_Rate
HAVING Biweekly_High_Rate > "$0.00"
ORDER BY min(Biweekly_High_Rate) ASC;

SUM()

SELECT SUM(UnitPrice) AS total_prod_price
FROM Products

SELECT SUM(UnitPrice*UnitsInStock) AS total_price
FROM Products
Where SupplierID = 23;

DISTINCT
jak go nie wstawimy SQL wychodzi z zalozenia ze chcemy wszystkie dane
nie mozna go uzywac w COUNT(*)
sprawdza czy są duplikaty

SELECT COUNT(DISTINCT CustomerID)

DZIALANIA NA DANYCH

SELECT
ProductID\
,UnitsOnOrder
,UnitPrice
,UnitsOnOrder*UnitPrice AS Total_Order_Cost
FROM Products




JOINS AND SUBQUERIES

Chcemy znac region z ktorego jest kazdy customer ktory mial ladunek wiekszy niz 100

SELECT CustomerID, CompanyName, Region
FROM Customers
WHERE CustomerId in (SELECT CustomerID
    FROM Orders
    WHERE Freight > 100);



SELECT COUNT (*) AS orders
FROM Orders
WHERE customer_id = "143569";


SELECT customer_name
    ,customer_state
    (SELECT COUNT (*) AS orders)
    FROM Orders
    WHERE Orders.customer_id =
Customer.customer_id) AS orders
    FROM customers
    ORDER BY Customer_name


CARTESIAN (CROSS) JOIN EXAMPLE

SELECT product_name
,unit_price
,company_name
FROM suppliers CROSS JOIN products;

INNER JOIN

SELECT suppliers.CompanyName
,ProductName
,UnitPrice
FROM Suppliers INNER JOIN Products
ON Suppliers.supplierid = \
Products.supplierid

INNY RODZAJ ZAPISU
FROM Orders o   przypisujemy o do order --> o.OrderID

PRZYKLAD
PODWOJNY INNER JOIN

SELECT o.OrderID, c.CompanyName, e.LastName
FROM ((Orders o INNER JOIN Customers c ON o.CustomerID = c.CustomerID)
                INNER JOIN Employees e ON o.EmployeeID = e.EmployeeID);

CREATING ALIASES FOR COLUMNS

SELECT column_name
FROM table_name AS alias_name

przyklad
SELECT vendor_name
,product_name
,product_price
FROM Vendors AS v, Products AS productname WHERE v.vendor_id= p.vendor_id;

SELF JOINS

SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
FROM Customers A, Customers B   # to samo tylko 2 razy jako A i B
WHERE A.CustomerID = B.CustomerID
AND A.City = B.City
ORDER BY A.City;

LEFT RIGHT AND FULL OUTER JOINS

SQLITE TYLKO LEFT JOIN

SELECT C.CustomerName, O.OrderID
FROM Customers City
LEFT JOIN Orders O ON C.CustomerID = SQLNOTATNIK.customer_id
ORDER BY C.CustomerName;

RIGHT JOIN na odwrot

FULL OUTER JOIN

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;


UNIONS

Kazdy select musi miec tyle samo COLUMN i TEN SAM TYP DANYCH
W TEJ SAMEJ KOLEJNOSCI

SELECT column_name(s) FROM
table1

UNION

SELECT column_name(s) FROM
table2;


SELECT City, Country FROM Customers
WHERE Country="Germany"

UNION

SELECT City, Country FROM Suppliers

WHERE Country="Germany"
ORDER BY City;