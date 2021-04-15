CREATE_passenger = '''
    CREATE TABLE IF NOT EXISTS titanic_passenger (
        survived INT,
        pclass INT,
        name VARCHAR(40),
        sex VARCHAR(5),
        age INT,
        siblings/spouses aboard INT,
        parents/children aboard INT,
        fare FLOAT
    );
'''

INSERT_passenger = '''
    INSERT INTO titanic_passenger (
      survived,
      pclass,
      name,
      sex,
      age,
      siblings/spouses aboard,
      parents/children aboard,
      far
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
'''
