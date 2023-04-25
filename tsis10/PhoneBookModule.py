import config
from configparser import ConfigParser
import psycopg2
from psycopg2.extensions import AsIs


def config(filename='phonebook.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db


def connect():
    conn = None
    try:
        params = config()
        print("Connecting to database...")
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print("PostgreSQL database version: ")
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed. ")


def create_tables():
    command = """
    CREATE TABLE users_phones (
        user_id SERIAL PRIMARY KEY,
        user_name VARCHAR(255) NOT NULL,
        user_surname VARCHAR(255) NOT NULL,
        phone_number VARCHAR(255) NOT NULL
    )    
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()


def insert_data(name, surname, phone_number):
    sql_1 = """
        INSERT INTO users_phones(user_name, user_surname, phone_number)
        VALUES (%s, %s, %s) RETURNING user_id;
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql_1, (name, surname, phone_number))
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()


def delete_by_name_surname(name, surname):
    conn = None
    sql = """
        DELETE FROM users_phones
        WHERE user_name = (%s) AND user_surname = (%s);
    """
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (name, surname))
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def import_from_csv(path):
    conn = None
    sql = """
    COPY users_phones
    FROM %s DELIMITER ',' CSV HEADER;
    """
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (path, ))
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not conn:
            conn.close()


def sort_by_attribute(attribute):
    sql = """
    SELECT * FROM users_phones
    ORDER BY %(attribute)s
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, {"attribute": AsIs(attribute)})
        for table in cur.fetchall():
            print(table)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()


def updated_using_surname(surname):
    option = int(input("Select data to change (1 - name, 2 - phone): "))
    conn = None
    sql_1 = """
    UPDATE users_phones
    set user_name = %s
    WHERE user_surname = %s;
    """
    sql_2 = """
    UPDATE users_phones
    set phone_number = %s
    WHERE user_surname = %s;
    """
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if option == 1:
            name = input("Enter new name: ")
            cur.execute(sql_1, (name, surname))
        elif option == 2:
            phone_number = input("Enter new phone number: ")
            cur.execute(sql_2, (phone_number, surname))
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()