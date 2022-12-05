y=int(input('interger'))
count=0
while True:
    if y==1
        print('goo')
        count+=1
        print(count)
    else:
        print('non')

# if __name__ == '__main__':
    # create_tables()
# def connect():
#     try:
#         params=config()
#         conn=psycopg2(**params)
#         cur=conn.cursor()
#         print('connection is successful')
#     except:
#         print('connection error')
#     return conn,cur
# def user_table():
#     conn,cur=connect()
#     user=''' CREATE TABEL user(user_name CHAR,user_id VARCHAR)
#              values('name','id')'''
#     user_table=cur.excute(user)
#     print(user_table)
# def book():
#     con,cur=connect()
#     book=''' CREATE TABELE book (book_id varchar,title char,author char,genere char, page int, added_date date,quantity int)
#                             values('id','title', 'author','genere', 'page', 'added_date'''
#     book_table=cur.excute(book)
#     print(book_table)
# def borrowed_book():
#     con,cur=connect()
#     borrowed_book=''' CREATE TABLE borrowed_book (book_id varchar,title char,author char,genere char, count int)
#                                    values('id', 'title','auther','genere', 'count')'''
# def favorite_book():
#     con,cur=connect()
#     favorite_book=''' CREATE TABLE favorite_book( book_id varchar,title char,author char,genere char, count int)
#                                    values('id', 'title','auther','genere', 'count')'''
#     favorite_bk=cur.execute(favorite_book)
# def returned_book():
#     con,cur=connect()
#     returned_book= ''' CREATE TABLE returned_book( book_id varchar,title char,author char,genere char, count int)
#                                    values('id', 'title','auther','genere', 'count')'''
#     returned_bk=cur.execute(returned_book)
#     print(returned_bk)
