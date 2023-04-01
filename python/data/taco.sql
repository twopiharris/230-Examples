DROP TABLE IF EXISTS shell;
CREATE TABLE shell (
  ID INTEGER PRIMARY KEY,
  name
);

INSERT INTO shell VALUES(null, 'hard');
INSERT INTO shell VALUES(null, 'soft');


DROP TABLE IF EXISTS taco;
CREATE TABLE taco (
  id INTEGER PRIMARY KEY,
  meat VARCHAR(15),
  shellID INTEGER,
  price FLOAT
);

INSERT INTO taco VALUES (null, 'fish', 1, 8);
INSERT INTO taco VALUES (null, 'chicken', 2, 4.99);
INSERT INTO taco VALUES (null, 'shrimp', 2, 30);
INSERT INTO taco VALUES (null, 'narwhal', 1, 50);


SELECT 
  meat,
  shell.name as SHELL,
  price

FROM taco, shell
WHERE taco.shellID = shell.ID;


DROP TABLE IF EXISTS topping;
CREATE TABLE topping (
  id INTEGER PRIMARY KEY,
  name VARCHAR(20)
);

INSERT INTO topping VALUES(null, 'lettuce');
INSERT INTO topping VALUES(null, 'cheese');
INSERT INTO topping VALUES(null, 'tomatoes');
INSERT INTO topping VALUES(null, 'sour cream');
INSERT INTO topping VALUES(null, 'guacamole');

SELECT * FROM topping;

DROP TABLE IF EXISTS taco_topping;
CREATE TABLE taco_topping(
  id INTEGER PRIMARY KEY,
  tacoID integer,
  toppingID integer
);


INSERT INTO taco_topping VALUES(null, 1, 1);
INSERT INTO taco_topping VALUES(null, 1, 2);
INSERT INTO taco_topping VALUES(null, 1, 3);
INSERT INTO taco_topping VALUES(null, 1, 4);
INSERT INTO taco_topping VALUES(null, 1, 5);
INSERT INTO taco_topping VALUES(null, 2, 1);


DROP VIEW IF EXISTS tacoToppingsView;
CREATE VIEW tacoToppingsView AS
SELECT 
  taco.meat AS 'meat',
  shell.name AS 'shell',
  topping.name AS 'topping'
FROM
  taco, topping, taco_topping, shell
WHERE
  taco_topping.tacoID = taco.ID
AND
  taco_topping.toppingID = topping.ID
AND 
  taco.shellID = shell.ID;

SELECT * FROM tacoToppingsView
WHERE meat = 'fish';

