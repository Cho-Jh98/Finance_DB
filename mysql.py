import pymysql

# DB information
host = "host ip address or domain"
port = 3306
user = 'user'
password = "your_password"
db = 'finance'
charset = 'utf8'

# connect
conn = pymysql.connect(host='localhost', port=3306, user='user', password='New^york6', db='database1', charset='utf8')

# cursor
cursor = conn.cursor()

# SQL
sql = """CREATE TABLE user (
id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
email varchar(255),
department varchar(255)
)
"""
cursor.execute(sql)

rows = cursor.fetchall()
print(rows)

conn.close()
