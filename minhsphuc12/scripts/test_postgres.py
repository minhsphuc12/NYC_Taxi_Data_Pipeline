import psycopg2
from psycopg2 import sql

# Database connection parameters
db_params = {
    'dbname': 'testdb',
    'user': 'user',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

# Sample data to insert
data_to_insert = [
    ('Sample data 3',),
    ('Sample data 4',)
]

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Create table if not exists
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS test_table (
        id SERIAL PRIMARY KEY,
        data TEXT
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()

    # Insert data into table
    insert_query = '''
    INSERT INTO test_table (data) VALUES (%s);
    '''
    cursor.executemany(insert_query, data_to_insert)
    conn.commit()

    # Query the table
    cursor.execute('SELECT * FROM test_table;')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()

