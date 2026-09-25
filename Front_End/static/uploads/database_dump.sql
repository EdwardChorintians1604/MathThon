BEGIN TRANSACTION;
CREATE TABLE testimonials (id INTEGER PRIMARY KEY AUTOINCREMENT, user_name TEXT NOT NULL, message TEXT NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP);
INSERT INTO "testimonials" VALUES(1,'Edward James','wah, website ini sangat berguna','2025-10-23 12:31:44');
INSERT INTO "testimonials" VALUES(2,'Thaufiq','Website ini harusnya diperbaiki lagi dan berikan kontrol AI-nya','2025-10-23 17:36:35');
INSERT INTO "testimonials" VALUES(4,'Mayang Janendra','Tolong untuk programmer-nya, segera perbaiki website ini karena ada bug yang harus diperbaiki lagi','2025-10-23 17:37:23');
CREATE TABLE user(  
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    katasandi VARCHAR(255) NOT NULL, 
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    jenis_kelamin VARCHAR(10),
    tempat_lahir VARCHAR(100),
    tanggal_lahir DATE,
    tingkat_kelas VARCHAR(20)
);
CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    born_place TEXT,
                    username TEXT NOT NULL UNIQUE,
                    born_date TEXT,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                , Photo [TEXT]);
INSERT INTO "users" VALUES(1,'Erantus Paripurna Samaloisa','padang','eddward','1990-12-12','nigga12@gmail.com','scrypt:32768:8:1$VbKTEvDfLNJF4i0A$c0feb17a179014b414310c4d616da4d966f0f11ddc5f429bb0162a65322079492256b6505a4fa6c38d42adb6a2150c70e3f1e1d4df83a7c4e79af7fd32b066fe',NULL);
INSERT INTO "users" VALUES(3,'Anisa Betsaida Pasaribu','Samosir','Anisa_Betsaida','2005-08-17','ramayana@gmail.com','scrypt:32768:8:1$DcuUMPG72rOpVoCL$819d56e4572e8b69c7e0debdf7c22490e11fa30076a4da7dd503d3a942c7eac5301f62c65587d201f1b1e1f12cb9a37cd0a97538d0bb2edc4fe88187b73d2c03',NULL);
INSERT INTO "users" VALUES(4,'Paska Agave Angelita Sakoikoi','Sikakap','Amoy_jelek','2006-04-17','paska_agave@gmail.com','scrypt:32768:8:1$McswBIfP06dTBBWZ$169e09e2b1b4da0323422f4e56e647dce20070ab16dcb67de50aed20e9f174d068b1f4280cf1ab4a70cf061563076b1cbd1bac9e743e6e726e0e8512139e25d3',NULL);
INSERT INTO "users" VALUES(5,'Hamonangan Pasaribu','Pandeglang','nigga09','2003-07-16','porsche12@yahoo.com','scrypt:32768:8:1$ch5nO7iCVTxLkbyP$8324b5d7a4d18c2b553d54072ead0e0202a0f7d4d35d9d8b30cee9ae15ccbba1794064c9ecbf050b9641b600f3b4a8fc74cb59621c29488843880ee68509b818','static/uploads/default.jpg');
INSERT INTO "users" VALUES(6,'Rey Rivaldo Hutagalung','Sikakap','Rey_23','2005-08-23','reyrivaldohutagalung@gmail.com','scrypt:32768:8:1$dRLWViALIPD7ryBs$50c84b0725657a30858494436db7c467e9f90e42f740b35a7e3c2cb292357663125b418a53ba1ebc001de248dfecdb9c01b10ff2a8ccddbbc2b2d152da00a745','static/uploads/default.jpg');
INSERT INTO "users" VALUES(7,'Mayang Janendra','Sikakap','MayangJanendraaaa','2006-01-23','janendramayang23@gmail.com','scrypt:32768:8:1$G6zDVNhjHd2LwNbc$2761d0af0d42eb0af9f5017cd56e30f4fd130114869c092df6ca62a776b48520bc519637828d79056c591bff3abf634fc2f68bf5fb942821c771d66373498834','static/uploads/default.jpg');
INSERT INTO "users" VALUES(8,'Christian Saogo','Tua Peijat','Saogo_Chris09','2001-09-23','saogochristian98@gmail.com','scrypt:32768:8:1$DMQ2HsQUlCyze0O9$8cbc88aa5e35edf44c637c8acd57201b8984f886d0093c530ea6b901f8dc58e8baa6bd26fca01ac3a28610dbc717226186693b6e2091c126c89b84c1c94ac337','static/uploads/default.jpg');
INSERT INTO "users" VALUES(9,'Hamdani Ryanto','Magelang','Ryanto_678','2005-09-09','ryanto_hamdani23@gmail.com','scrypt:32768:8:1$IFZdvaWuYz6GyQrl$f0275ab7005d1c85ed325c72a97ffef56f6f1a4fc2093c3b905bad61f39ea7e3fe06c4dfc50c365197cb320d5bf3234a74f9a8e0be0924d0692c1b26820e91fb','F:\MathThon\Back_End\uploads\Toko Masabuk Jaya.png');
INSERT INTO "users" VALUES(10,'Edward Kenway','Stockholm','edward_james','2004-03-16','edwardkenway@gmail.com','scrypt:32768:8:1$JtXqrW3bvHWJ8N5l$0f1028c3e7c4a70777d70c7d0516731b66b75bdd1abddca16277743f25f81b1f818de620673e38a80c64ec1e70988a375bd4c31d6c069d29e81e8616c5913212','F:\MathThon\Back_End\uploads\Darkfly Indonesian Automotive (2).png');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('testimonials',4);
INSERT INTO "sqlite_sequence" VALUES('users',10);
COMMIT;