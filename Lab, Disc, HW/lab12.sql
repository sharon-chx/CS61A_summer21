.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color ='blue' AND pet='dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color ='blue' AND pet='dog';;


CREATE TABLE matchmaker AS
  SELECT a.pet AS pet, a.song AS song, a.color AS color, b.color AS color
  FROM students AS a, students AS b 
  WHERE a.pet = b.pet AND a.song = b.song AND a.time < b.time;


CREATE TABLE sevens AS
  SELECT seven FROM students AS s, numbers AS n
  WHERE s.number = 7 AND n.'7' = 'True' and s.time = n.time;


CREATE TABLE favpets AS
  SELECT DISTINCT pet, count(*) as total_count FROM students
  GROUP BY pet
  ORDER BY total_count DESC LIMIT 10;


CREATE TABLE dog AS
  SELECT pet, count(*) as total_count FROM students
  WHERE pet = 'dog';


CREATE TABLE bluedog_agg AS
  SELECT song, count(*) AS count FROM bluedog_songs
  GROUP BY song
  ORDER by count DESC;


CREATE TABLE instructor_obedience AS
  SELECT seven, instructor, count(*) FROM students
  WHERE seven = '7'
  GROUP BY instructor;




