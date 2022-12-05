from config import config
import psycopg2
import pandas as pd
from datetime import datetime
 
# class libarary:

def connect():
    conn = None
    try:
        params=config()
        conn=psycopg2(**params)
        # cur=conn.cursor()
        print('connection is successful')
    except:
        print('connection error')
    return conn 
connect()

def create_tables():
    """ create tables in the PostgreSQL database"""
    tables = (
        """
        CREATE TABLE user_table (
            user_name CHAR NOT NULL,
            user_id VARCHAR
             )
        """,
        """ CREATE TABLE book (
                book_id varchar NOT NULL,
                title char NOT NULL,
                author char NOT NULL,
                genere char, 
                page int, 
                added_date date,
                quantity int
                
                )
        """,
        """
        CREATE TABLE borrowed_book (
                 book_id varchar ,
                 title char,
                 author char,
                 genere char, 
                 count int
                 FOREIGN KEY(book_id)
                 REFERENCES book (book_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE favorite_book (book_id varchar,
                                    title char,
                                    author char,
                                    genere char,
                                    count int
                                    foriegn key(book_id)
                                    references book(book_id)
                                   ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
   
    try:
        conn,cur=connect()
        for table in tables:
            cur.execute(table)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
  
    
def welcome():
    con,cur=create_tables()
    
    # user=user_table()
    print('well come to x libarary')
    print('sign in')
    user_name=str(input('inter your username here'))
    user_sql=f'select user_name from user_table where user_name={user_name} '
    user=cur.execute(user_sql)
    
    if user_name==user:
        print(f'well come {user_name} you are now logged in')

    else:
        try:
            print('the user name is not found please sign up')
            user_name=str(input('user_name: '))
            user_id=str(input('user_id: '))
            user_data_sql=f'insert into user_table values({user_name},{user_id})'
            sign_up=cur.execute(user_data_sql)
            print('you are successfully registered')
        except:
            print('registration failure')
# def sing_up():
#     con,cur=connect()
#     user_name=str(input('user_name: '))
#     user_id=str(input('user_id: '))
#     user_data_sql=f'insert into user_table values({user_name},{user_id})'
#     sign_up=cur.execute(user_data_sql)
def action():
    conn,cur=connect()
    print('add_book')
    print("please inter:")
    book_id=int(input('book id'))
    book_sql='''select book_id from book '''
    book_id=cur.execute(book_sql)
    all_book_id=book_id.fetchall
    for book_id in all_book_id:
        print(book_id)
    if book_id in all_book_id:
        print('the book id is taken try another')
    else:
        book_id=int(input('book_id'))
        title =str(input('book title'))
        author =str(input('auther name'))
        genere=str(input('book genere'))
        page =int(input('number of pages')) 
        added_date_date=str(input('added date in format dd/mm/yyyy'))
        quantity=int(input('quantity'))

        book_data_sql=f'insert into book values( {book_id} ,{title}, {author},{genere}, {page},{added_date_date},{quantity}'
        cur.execute(book_data_sql)
def borrow_book():
    count=0
    conn,cur=connect()
    print('check the availablithy of the book:')
    check=int(input(' enter the book_id '))
    # borrow_book_sql='''select book_id from book where book_id'''
    borrow=cur.execute('select book_id from book')
    borrowed_book=borrow.fetchall   
    if check in borrowed_book:
        print('the book is borrowed')
    else:
        print('you can access the book')
        borrow1=cur.execute('SELECT * FROM book where book_id=check')
        res=borrow1.fetchone()
        sql=f'INSERT INTO borrowed  values({res[0]},{res[1]},{res[2]},{res[3]}'
        cur.execute(sql)

        borrow_book=check
        
        reg_book=f'select book_id, book_name,genere from book'
        cur.execute('')
        count+=1
def search_book():
    conn,cur=connect()
    book_name=str(input('please insert the book name'))
    search_sql=f'select * from book where book_name= {book_name}'
    search_rlt=cur.execute(search_rlt)
    result=search_rlt.fetchall()
    print(result)

def search_by_auther():
    conn,cur=connect()
    author=str(input('enter the auther name: '))
    author_sql=f'select * from book where auther={author}'
    author_rslt=cur.execute(author_sql)
    result=author_rslt.fetchall()
    print(result)
def recently_added():
    conn,cur=connect()
    current_time=datetime.now()
    recent=f'select * from book where date_added <={current_time} sort by date_added dsc limit 5'
    recent_rslt=cur.execute(recent)
    print(recent_rslt)
def most_read_book():
    conn,cur=connect()
    genere=str(input('enter genere'))
    most_read_book_sql='''select * from book order by count dsc limit 10'''
    most_read=cur.execute(most_read_book)
    most_read_rslt=most_read.fetchall()
    print(most_read_rslt)
    most_read_genere_sql=f'select genere from book where genere = {genere} order by count asc limit 10'
    most_read_genere=cur.execure(most_read_genere_sql)
    most_read_genere_rslt= most_read_genere.fetchall()
    print(most_read_genere_rslt)
def favorite():
    book_n=str(input('enter your favorite books '))
    favorite_sql=f'update book set favorite_book=favorite where book_name={book_n}'
def most_fav():
    genere=str(input('enter the genere of the book'))
    most_fav_sql=f' select count("favorite") from book where genere={genere}'






                                 
 