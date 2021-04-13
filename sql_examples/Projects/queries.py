'''Write SQL queries'''


total_characters = '''
    SELECT COUNT(name)
    FROM charactercreator_character;
'''


total_subclass = '''
    SELCET COUNT(*)
    FROM charactercreator_necromancer;
'''


total_items = '''
    SELECT COUNT(DISTINCT(name))
    FROM armory_item;
'''


weapons = '''
    SELCT COUNT(*)
    FROM armory_weapon;
'''


non_weapons = '''
    SELECT COUNT(*)
    FROM armory_item
    LEFT JOIN armory_weapon
    ON armory_item.item_id =
    armory_weapon.item_ptr_id IS NULL;
'''


character_items = '''
    SELECT COUNT(item_id), character_id
    FROM charactercreator_character_inventory
    GROUP BY character_id;
'''


character_weapons = '''
    SELECT COUNT(item_id), character_id
    FROM armory_weapon
    LEFT JOIN charactercreator_character_inventory
    ON armory_weapon.item_ptr_id =
    charactercreator_character_inventory.item_id
    GROUP BY character_id;
'''


avg_character_items = '''

'''


avg_character_weapons = '''

'''
