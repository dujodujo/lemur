PRAGMA foreign_keys=OFF;

CREATE TABLE 'hero'(
    'rowid' INT NOT NULL,
    'name' TEXT NOT NULL,
    'x' INT NOT NULL,
    'y' INT NOT NULL
);

CREATE TABLE 'enemy'(
    'name' TEXT NOT NULL
);

CREATE TABLE 'inventory'(
    'rowid' INT NOT NULL,
	'item' INT NOT NULL,
	'amount' INT NOT NULL
);

CREATE TABLE 'items'(
    'item_name' TEXT NOT NULL,
    'item_image' TEXT NOT NULL
);

CREATE TABLE 'equipments'(
    'equipment_name' TEXT NOT NULL,
    'equipment_image' TEXT NOT NULL,
    'type' INT
);

CREATE TABLE 'swords'(
	'swordid' TEXT NOT NULL,
	'damage' REAL NOT NULL
);

INSERT INTO 'swords' VALUES('Claymore', 1);
INSERT INTO 'swords' VALUES('Oakshot ', 1);
INSERT INTO 'swords' VALUES('Xiphos', 1);
INSERT INTO 'swords' VALUES('Gladius', 1);
INSERT INTO 'swords' VALUES('Panzerstecher', 1);