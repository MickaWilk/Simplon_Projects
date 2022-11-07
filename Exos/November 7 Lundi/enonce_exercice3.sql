
/* Exercise 1 */

-- Query 1 : Display the CDs that came out in 1998. (line count: 35)
SELECT * From Disc
WHERE YEar = 1998

-- Query 2 : Display the CDs published in 21st century. (line count: 142)
SELECT * From Disc
WHERE Year BETWEEN 2000 AND 2100

-- Query 3 : Display the CDs that came out in the 90s. (line count: 291)
SELECT * From Disc
WHERE Year BETWEEN 1990 AND 1999

-- Query 4 : Display the different names of states of CDs (without repretition). (line count: 4)
SELECT DISTINCT State From Disc


-- Query 5 : Find the titles of all damaged CDs. (line count: 170)
SELECT Title From Disc
WHERE State = 'Damaged'

-- Query 6 : Find cheap used CDs (price below 11). Order the result by the price (ascending). (line count: 30)
SELECT * From Disc
WHERE State = 'Used' AND price < 11
ORDER BY price ASC

-- Query 7 : Find CDs that came out either in 1990 or 1995 and whose price is between 10 and 15. (line count: 26)
SELECT * From Disc
WHERE (Year = 1990 OR Year = 1995) AND price BETWEEN 10 AND 15


-- Query 8 : Find the number of CDs that came out in the 80s and their price is between 12 and 14. (line count:
42)
SELECT * From Disc
WHERE (Year BETWEEN 1980 AND 1989) AND (price BETWEEN 12 AND 14)


-- Query 9 : Find the total of prices of destroyed CD. (the answer is 627.97) (line count: 1)
SELECT SUM(price) From Disc
WHERE State = 'Destroyed'


-- Query 10 : Find CD by ’The Beatles’. (line count: 6)
SELECT * From Disc
JOIN Artist ON Artist.ID = Disc.Artist_ID
WHERE Name LIKE 'The Beatles%'


-- Query 11 : Find CDs by ’AC DC’ that came out in the 90s. (line count: 4)
SELECT * From Disc
JOIN Artist ON Artist.ID = Disc.Artist_ID
WHERE Name LIKE 'AC DC' and Year BETWEEN 1990 AND 1999


-- Query 12 : Find artists names who had a CD in 1991. (line count: 25)
SELECT DISTINCT Name From Disc
JOIN Artist ON Artist.ID = Disc.Artist_ID
WHERE Year = 1991


-- Query 13 : Find the sum of prices of all CD by Georges Brassens. (the answer is 200.73) (line count: 1)
SELECT SUM(price) From Disc
JOIN Artist ON Artist.ID = Disc.Artist_ID
WHERE Name = 'Georges Brassens'


-- Query 14 : Find titles of song of the Rock genre. (line count: 5504)
SELECT Title
FROM Song
JOIN Genre as g ON g.id = Song.Genre_ID
WHERE name = 'Rock'


-- Query 15 : List titles of songs whose genre description uses the word ’afric’. (line count: 334)



-- Query 16 : Find the number of folk songs whose lyrics are not covered by copyright. (the answer is 124) (line
count: 1)

-- Query 17 : Find song titles written by Jacques Brel. (line count: 134)

-- Query 18 : Find artists who have written the song ’Anybody Seen My Baby?’. (line count: 2)

-- Query 19 : find the number of CDs with songs written by Mick Jagger. (the answer is 54) (line count: 1)


/* Become now harder */
/*Si vous avez des requêtes imbriquées, il faut utiliser un WITH ! */

-- Query 20 : Find the song list on the CD A Night at the Opera, in the order of their position. (line count: 12)

-- Query 21 : Find name of srtists who have not written a single song. (line count: 506)

-- Query 22 : List songs performed by Lenny Kravitz that are present on David Bowie’s CDs. (line count: 1)

-- Query 23 : Find CDs that contain at least one song performed by an artist different from the (main) artist of the
-- disc. (line count: 37)

-- Query 24 : Find CDs that contain at least one song written by an artist different from the (main) artist of the
-- CD. (line count: 83)

-- Query 25 : List the number and the average price of CD for every different state. (line count: 4)

-- Query 26 : For every artist find the number of their CDs. Display the results in the descending order of the
-- number of CDs (line count: 273)

-- Query 27 : For every CD list its title and the number of songs it contains. display only CD with at least 10 songs
-- (line count: 688)

-- Query 28 : For every genre find the number of CDs that contain a song of this genre. Mind not to count the
-- same CD more than once. Display genres with more than 50 songs (line count: 4)

-- Query 29 : List the artists in the descending order of the average price of their CDs. List only those artists who
-- have at least 4 CDs for which the average CD price is above 12. (line count: 61)


/* Questions Bonus (Optionnelles) */

-- Query 30 : Find CD whose list of songs is potentially incomplete. (Hint: compare the number of songs with
-- the position of the last song). (line count: 24)

-- Query 31 : Find frequent collaborators. Any pair of artists who have performed a song on the same CD are
-- collaborators. If there are at least 2 CDs, then this pair are frequent collaborators. (there is only 5 such pairs)
-- (line count: 10)
