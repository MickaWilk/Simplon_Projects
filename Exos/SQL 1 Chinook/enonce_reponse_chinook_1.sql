Use Chinook;
-- QUERY 1
-- Exploration of the Customer table in the Chinook database
SELECT * FROM Customer;

-- QUERY 2
-- Extract CustomerId, Company and City data from the customer table in the Chinook database
SELECT CustomerId, Company, City FROM customers


-- QUERY 3
-- Extract the Lastname, Firstname, email and city from the same table
SELECT Lastname, Firstname, email, city FROM customers


-- QUERY 4
-- Extract the Lastname, Firstname, email, city and country from the same table
-- and select only the country starting with "AUSTR"
-- What do you observe?
SELECT *,Lastname, Firstname, email, city FROM customers
WHERE Country LIKE "AUSTR%"


-- QUERY 5
-- Extract the Lastname, Firstname, email, city and country from the same table
-- only from USA and Canada
SELECT *,Lastname, Firstname, email, city FROM customers
WHERE Country LIKE 'USA' OR Country like 'Canada'


-- QUERY 6
-- Use the previous query and order the extracted data by lastname ascending
SELECT *,Lastname, Firstname, email, city FROM customers
WHERE Country like 'USA' OR Country like 'Canada'
ORDER BY LastName ASC


-- QUERY 7
-- Show the top 5 data in alphabetical order
SELECT *,Lastname, Firstname, email, city FROM customers
WHERE Country like 'USA' OR Country like 'Canada'
ORDER BY LastName ASC
LIMIT 5


-- QUERY 8
-- Extract the Top 5 data starting at row 5
SELECT *,Lastname, Firstname, email, city FROM customers
WHERE Country like 'USA' OR Country like 'Canada'
ORDER BY LastName ASC
LIMIT 5 OFFSET 5



-- QUERY 9
-- Count the number of clients you have in USA
-- Count the number of clients you have in Canada
SELECT Country, count(Country) FROM customers
WHERE Country LIKE 'USA'
SELECT Country, count(Country) FROM customers
WHERE Country LIKE 'Cananda'



-- QUERY 10
-- Count the number of clients you have in Berlin and in Paris (1 request and 1 line per cities)
SELECT Country, count(Country) FROM customers
WHERE Country LIKE 'Berlin' OR Country like 'Paris'
GROUP BY Country


-- QUERY 11
-- How many states are there and how many cities per state ?
SELECT count(DISTINCT State) FROM customers


-- QUERY 12
-- Count the number of clients per country and order them from the largest to the smallest.
SELECT DISTINCT Country, count(Country) as yes FROM customers
GROUP BY Country
Order BY yes DESC


--------------------------------
-- Let's change table !
-- Explore the Track table
Use Track;
SELECT * FROM Track;


-- QUERY 13
-- Extract the data about songs with name starting by let'
-- Extract the data about songs with name containing good in it
-- Extract the data about songs with name ending by you
SELECT * FROM tracks
WHERE name LIKE 'let%'

SELECT * FROM tracks
WHERE name LIKE '%good%'

SELECT * FROM tracks
WHERE name LIKE '%you'


-- QUERY 14
-- Extract the data about songs which length is from 230 et 240 seconds and order them from the longest to the shortest
SELECT * FROM tracks
WHERE Milliseconds BETWEEN 230000 AND 240000
ORDER BY Milliseconds DESC


-- QUERY 15
-- Extract data from the top 10 long songs which cost 0.99
SELECT * FROM tracks
WHERE UnitPrice = 0.99
ORDER BY Milliseconds DESC
LIMIT 10



-- QUERY 16
-- Extract the different prices apply to the songs
-- Extract the different composer from the table
-- Extract song where the price is bigger than the average price
SELECT DISTINCT UnitPrice FROM tracks

SELECT DISTINCT Composer FROM tracks

SELECT * FROM tracks
WHERE UnitPrice > (SELECT AVG(Unitprice) FROM tracks)


-- QUERY 17
-- Extract data of songs which genreid is 20 and album id is 253.
-- Order them by the id of each track
SELECT * FROM tracks
WHERE genreid = 20 and albumid = 253
ORDER BY TrackId


-- QUERY 18
-- Calculate the length of songs in seconds
-- Count the number of songs whose songs are longer than the average length of song (eventually use a CASE)
SELECT SUM(Milliseconds / 1000) as Len FROM tracks
SELECT count(TrackId) as Len FROM tracks
WHERE Milliseconds > (SELECT avg(MIlliseconds) FROM tracks)



-- QUERY 19
-- Calculate the average length of songs by album and count the number of songs by album
-- order by the number of songs descending
SELECT avg(Milliseconds), Count(TrackId) as nbsongs FROM tracks
GROUP BY AlbumId
ORDER BY nbsongs DESC


-- QUERY 20 / Review
-- Extract the top 10 composers order from the longest average length of tracks and count the number of album the composer appear in
SELECT composer, avg(Milliseconds), Count(DISTINCT AlbumId)
FROM tracks
WHERE Composer IS NOT NULL
GROUP BY Composer
ORDER BY avg(Milliseconds) DESC
LIMIT 10


-- Bonus:
-- QUERY 21 (line count : 58)
-- Name the composers whose total of length songs are longer than the total of the length songs of queen
SELECT composer, SUM(Milliseconds) as song_len
FROM tracks
WHERE Composer IS NOT NULL
GROUP BY Composer
HAVING song_len > (SELECT SUM(Milliseconds) FROM tracks WHERE Composer LIKE '%queen%')


-- QUERY 22
-- How many composers did not compose any songs ?
-- How many of songs are not refered to a composer ?
SELECT count(DISTINCT composer)
FROM tracks
WHERE TrackId IS NULL

SELECT Name
FROM tracks
WHERE composer IS NULL


-- QUERY 23 (line count : 10)
-- Select the top 10 of composers by their number of tracks
-- You will see that the first one on the top is no-one
-- How is that possible? Comment here in 1 sentence
SELECT composer, count(TrackId) as nb
FROM tracks
WHERE composer IS NOT NULL
GROUP BY composer
ORDER BY nb DESC
LIMIT 10
