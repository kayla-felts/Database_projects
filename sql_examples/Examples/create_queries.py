# For ./sqlite_to_postgreaql.py
CREATE_charactercreator_character = """
  CREATE TABLE IF NOT EXISTS charactercreator_character (
     id SERIAL PRIMARY KEY,
     name VARCHAR(30),
     level INT,
     exp INT,
     hp INT,
     strength INT,
     intelligence INT,
     dexterity INT,
     wisdom INT
  );
"""

INSERT_charactercreator_character = """
    INSERT INTO charactercreator_character (
      name,
      level,
      exp,
      hp,
      strength,
      intelligence,
      dexterity,
      wisdom
    ) VALUES (
      %s,
      %s,
      %s,
      %s,
      %s,
      %s,
      %s,
      %s
    );
"""

# For ./postgresql_examples.py
CREATE_TEST = '''
    CREATE TABLE test_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(40) NOT NULL,
        fav_num INT NOT NULL
    );
'''


INSERT_TEST = '''
    INSERT INTO test_table(name, fav_num) VALUES
    (
        'Nick',
        45
    ),
    (
        'Jack',
        42
    ),
    (
        'Stephen',
        56
    );
'''
