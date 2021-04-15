'''Write SQL queries'''

# For rpg_db
TOTAL_CHARACTERS = '''
    SELECT COUNT(name)
    FROM charactercreator_character;
'''


TOTAL_SUBCLASS = '''
    SELCET COUNT(*)
    FROM charactercreator_necromancer;
'''


TOTAL_ITEMS = '''
    SELECT COUNT(DISTINCT(name))
    FROM armory_item;
'''


WEAPONS = '''
    SELCT COUNT(*)
    FROM armory_weapon;
'''


NON_WEAPONS = '''
    SELECT COUNT(*)
    FROM armory_item
    LEFT JOIN armory_weapon
    ON armory_item.item_id =
    armory_weapon.item_ptr_id IS NULL;
'''


CHARACTER_ITEMS = '''
    SELECT COUNT(item_id), character_id
    FROM charactercreator_character_inventory
    GROUP BY character_id
    LIMIT 20;
'''


CHARACTER_WEAPONS = '''
    SELECT COUNT(item_id), character_id
    FROM armory_weapon
    LEFT JOIN charactercreator_character_inventory
    ON armory_weapon.item_ptr_id =
    charactercreator_character_inventory.item_id
    GROUP BY character_id
    LIMIT 20;
'''


avg_character_items = '''

'''


avg_character_weapons = '''

'''

# For buddymove_holiday db
TOTAL_ROWS = '''
    SELECT COUNT(*)
    FROM buddymove_holidayiq
'''
