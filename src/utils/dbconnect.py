import mysql.connector
from config import *

def db_connect(table_is_existed):
    conn = mysql.connector.connect(
        host=host,  
        user=username,
        password=password,
        database=database
        )
    if  table_is_existed == False:
        mycursor = conn.cursor()
        mycursor.execute(f"""
        CREATE TABLE {table_name} (
            ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            ImgPath VARCHAR(500) NOT NULL,
            Xmin INT NULL,
            Ymin INT NULL,
            Xmax INT NULL,
            Ymax INT NULL,
            Confidence FLOAT NULL,
            Country VARCHAR(255),
            PaddleOCR VARCHAR(350) NULL,
            EasyOCR VARCHAR(350) NULL
        );
        """)
        conn.commit()
    return conn