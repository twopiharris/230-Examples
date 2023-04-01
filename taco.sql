/* drops */
DROP TABLE IF EXISTS bad_taco;
DROP TABLE IF EXISTS taco;
DROP TABLE IF EXISTS shell;
DROP VIEW IF EXISTS taco_shell_view;
DROP TABLE IF EXISTS topping;
DROP TABLE IF EXISTS taco_topping;
DROP VIEW IF EXISTS taco_topping_view;

/* creates */
CREATE TABLE bad_taco (
  ID INTEGER PRIMARY KEY,
  shell VARCHAR(20),
  meat VARCHAR(20),
  toppings VARCHAR(100),
  price CURRENCY
);

CREATE TABLE taco(
  ID INTEGER PRIMARY KEY,
  name VARCHAR(20),
  shellID INTEGER,
  price CURRENCY
);

CREATE TABLE shell(
  ID INTEGER PRIMARY KEY,
  name VARCHAR(20)
);

CREATE VIEW taco_shell_view AS
SELECT
  taco.id AS 'ID',
  taco.name AS 'taco',
  shell.name AS 'shell',
  taco.price AS 'price'
FROM
  taco, shell
WHERE
  taco.shellID = shell.ID;

CREATE TABLE topping (
  ID INTEGER PRIMARY KEY,
  name
);

CREATE TABLE taco_topping (
  ID INTEGER PRIMARY KEY,
  tacoID INTEGER,
  toppingID INTEGER
);

CREATE VIEW taco_topping_view AS
SELECT
  taco.ID AS 'ID',
  taco.name AS 'taco',
  topping.name AS 'topping'
FROM
  taco, topping, taco_topping
WHERE
  taco.ID = taco_topping.tacoID
AND
  topping.ID = taco_topping.toppingID;
  

/* inserts */
INSERT INTO bad_taco VALUES(null, 'hard', 'oppossum', 'tomatoes and lettuce', 1.50);
INSERT INTO bad_taco VALUES(null, 'hard', 'oppossum', 'tomato, lettuce, cheese, sour cream', 3.50);
INSERT INTO bad_taco VALUES(null, 'hard', 'oppossum', 'tom, let, sc, guac, extra cheese', 4.25);

INSERT INTO taco VALUES(null, 'standard', 1, 1.50);
INSERT INTO taco VALUES(null, 'bonus', 1, 2.50);
INSERT INTO taco VALUES(null, 'deluxe', 2, 3.50);

INSERT INTO shell VALUES(null, 'hard');
INSERT INTO shell VALUES(null, 'soft');

INSERT INTO topping VALUES(null, 'lettuce');
INSERT INTO topping VALUES(null, 'tomato');
INSERT INTO topping VALUES(null, 'guacamole');
INSERT INTO topping VALUES(null, 'cheese');
INSERT INTO topping VALUES(null, 'salsa');


INSERT INTO taco_topping VALUES(null, 1, 1);
INSERT INTO taco_topping VALUES(null, 1, 2);
INSERT INTO taco_topping VALUES(null, 1, 3);
INSERT INTO taco_topping VALUES(null, 1, 4);
INSERT INTO taco_topping VALUES(null, 2, 5);
INSERT INTO taco_topping VALUES(null, 3, 1);


/* selects */
-- SELECT * FROM bad_taco;
-- SELECT * FROM taco;
-- SELECT * FROM shell;

/*
SELECT 
  taco.name AS 'taco',
  taco.shellID AS 'tacoShellID',
  shell.ID AS 'shellID',
  shell.name AS 'shell'
FROM
  taco,
  shell;

SELECT
  taco.name AS 'taco',
  shell.name AS 'shell'
FROM
  taco, shell
WHERE
  taco.shellID = shell.ID;
*/

-- SELECT * FROM taco_shell_view;

-- SELECT * FROM taco_topping_view;

SELECT taco, shell, price FROM taco_shell_view WHERE ID = 1;
SELECT topping FROM taco_topping_view WHERE ID = 1;




