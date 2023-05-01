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
    command_1 = """
    CREATE DOMAIN valid_phone_number AS TEXT
    CHECK(
    VALUE ~ '^[+][0-9] [(][0-9]{3}[)] [0-9]{3}[-][0-9]{2}[-][0-9]{2}$'
    );
    """
    command_2 = """
    CREATE TABLE users_phones (
        user_id SERIAL PRIMARY KEY,
        user_name VARCHAR(255) NOT NULL,
        user_surname VARCHAR(255) NOT NULL,
        phone_number valid_phone_number NOT NULL
    )    
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command_1)
        cur.execute(command_2)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()


def is_user_exist(surname, name):
    sql = """
        SELECT * FROM users_phones WHERE user_surname = %s AND user_name = %s;
        """
    conn = None
    is_exist = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (name, surname))
        is_exist = cur.fetchone()[0]
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return is_exist


def insert_data_or_update(surnname, name, phone_number):
    sql_1 = """
        INSERT INTO users_phones(user_name, user_surname, phone_number)
        VALUES (%s, %s, %s) RETURNING user_id;
    """
    sql_2 = """
        UPDATE users_phones
        set phone_number = %s
        WHERE user_surname = %s AND user_name = %s;
        """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if is_user_exist(surnname, name):
            print("User phone updated!")
            cur.execute(sql_2, (phone_number, surnname, name))
        else:
            cur.execute(sql_1, (surnname, name, phone_number))
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print("Please check phone number format!")
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


def delete_by_phone(phone_number):
    conn = None
    sql = """
            DELETE FROM users_phones
            WHERE phone_number = (%s);
        """
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (phone_number))
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


def sort_using_pattern(pattern):
    conn = None
    sql_1 = """
    SELECT * FROM users_phones
    WHERE user_name ~ %s
    OR user_surname ~ %s
    OR phone_number ~ %s
    """
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql_1, (pattern, pattern, pattern))
        for table in cur.fetchall():
            print(table)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def query_data_with_limit_offset(limit, offset):
    sql = """
        SELECT * FROM users_phones
        ORDER BY user_id
        LIMIT {0}
        OFFSET {1};
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql.format(limit, offset))
        for line in cur.fetchall():
            print(line)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()


def insert_data_from_list(list):
    sql_1 = """
            INSERT INTO users_phones(user_name, user_surname, phone_number)
            VALUES (%s, %s, %s) RETURNING user_id;
        """
    sql_2 = """
            UPDATE users_phones
            set phone_number = %s
            WHERE user_surname = %s AND user_name = %s;
            """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for data in list:
            if is_user_exist(data[0], data[1]):
                print("User phone updated!")
                cur.execute(sql_2, (data[2], data[0], data[1]))
            else:
                cur.execute(sql_1, (data[0], data[1], data[2]))
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()


#create_tables()