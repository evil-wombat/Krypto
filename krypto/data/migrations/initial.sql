CREATE TABLE "movements" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"date"	TEXT NOT NULL,
	"time"	TEXT NOT NULL,
	"from_currency"	TEXT NOT NULL,
	"from_quantity"	REAL NOT NULL,
	"to_currency"	TEXT NOT NULL,
	"to_quantity"	REAL NOT NULL
);