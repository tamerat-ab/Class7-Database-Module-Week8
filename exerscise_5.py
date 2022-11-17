import psycopg2
from config1 import config1


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE student (
            student_id INTEGER NOT NULL,
            teacher_name VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE teacher(
                teacher_id INTEGER NOT NULL,
                teacher_name VARCHAR(25) NOT NULL
                
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config1()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
            print(cur.execute(command))
        data=[cur.execute("INSERT into students(student_id, name) VALUES (123, mike),(876,Ahamad),(908,shafi)"),
              cur.execute("INSERT into teachers(student_id, name) VALUES (123, mike),(876,Ahamad),(908,shafi)") 
            ]
        for data in data:
            print(cur.fetchall())

        cur.execute("SELECT * student")
        print(cur.fetchall())
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()