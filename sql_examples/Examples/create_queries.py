# For ./sqlite_to_postgreaql.py


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
