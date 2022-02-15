DROP_TEST_TABLE = '''DROP TABLE IF EXISTS test_table;'''

CREATE_TEST_TABLE = '''CREATE TABLE IF NOT EXISTS test_table 
                        ("id" SERIAL NOT NULL PRIMARY KEY, 
                        "name" VARCHAR(50) NOT NULL, 
                        "age" INT NOT NULL);'''

INSERT_TEST_TABLE = '''INSERT INTO test_table ("name", "age")
                       VALUES ('Ryan Allred', 30);'''

READ_TEST_TABLE = '''SELECT * FROM test_table;'''

GET_CHARACTERS = '''SELECT * FROM charactercreator_character;'''

DROP_CHARACTER_TABLE = '''DROP TABLE IF EXISTS charactercreator_character;'''

CREATE_CHARACTER_TABLE = '''CREATE TABLE IF NOT EXISTS charactercreator_character (
                            "character_id" SERIAL NOT NULL PRIMARY KEY,
                            "name" VARCHAR(30) NOT NULL,
                            "level" INT NOT NULL,
                            "exp" INT NOT NULL,
                            "hp" INT NOT NULL,
                            "strength" INT NOT NULL,
                            "intelligence" INT NOT NULL,
                            "dexterity" INT NOT NULL,
                            "wisdom" INT NOT NULL
                            ); 
                            '''
INSERT_RYAN = '''INSERT INTO charactercreator_character ("name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom")
                 VALUES ('Ryan Allred', 75, 100, 1000, 9000, 1000000, 3, -10)'''
