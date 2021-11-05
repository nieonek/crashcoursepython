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