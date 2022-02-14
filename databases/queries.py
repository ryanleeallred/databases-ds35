# SQL - Structured Query Language
# The result of my query was: 302 characters
GET_CHARACTERS = '''SELECT * FROM charactercreator_character;''' 

GET_ONE_CHAR_NAME = '''SELECT "name", "hp" 
                       FROM charactercreator_character 
                       WHERE name = 'Minus c';'''

NUM_DISTINCT_NAMES = '''SELECT COUNT(DISTINCT name) 
                        FROM charactercreator_character;'''

NUM_CLERIC_ITEMS = '''SELECT cc_char.name, COUNT(ai.name) as num_items
                      FROM charactercreator_character AS cc_char
                      INNER JOIN charactercreator_cleric AS cc_cleric
                      ON cc_char.character_id = cc_cleric.character_ptr_id
                      JOIN charactercreator_character_inventory as cc_inv
                      ON cc_char.character_id = cc_inv.character_id
                      JOIN armory_item as ai
                      ON cc_inv.item_id = ai.item_id
                      GROUP BY cc_char.name;'''