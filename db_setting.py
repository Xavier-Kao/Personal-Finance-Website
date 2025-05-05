import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="datafile"
)
cursor = conn.cursor()


cursor.execute(
    """create table if not exists cash (transaction_id int auto_increment primary key, taiwanese_dollars int, us_dollars double, note varchar(30), date_info date)""")

cursor.execute(
    """create table if not exists stock (transaction_id int auto_increment primary key, stock_id varchar(10), stock_num int, stock_price double, processing_fee int, tax int, date_info date)""")

conn.commit()
conn.close()
