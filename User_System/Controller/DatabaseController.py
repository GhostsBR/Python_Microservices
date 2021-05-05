import os
import mysql.connector
import pandas as pd

from dotenv import load_dotenv
load_dotenv()

from Model import StatusModel
sm = StatusModel



class DatabaseControl:
    def list_users(self) -> sm:
        try:
            mydb = mysql.connector.connect(
                db=os.getenv('DATABASE'),
                host=os.getenv('DATABASE_HOST'),
                user=os.getenv('DATABASE_USER')
            )
            cursor = mydb.cursor()
        except:
            return sm.StatusModel("Error: Connection with database failed", 503)
        try:
            cursor.execute(f"SELECT * FROM user")
            columns = [i[0] for i in cursor.description]
            result = pd.DataFrame(cursor.fetchall(), columns=columns).to_json(orient="records")
        except:
            return sm.StatusModel("Error: Cannot select user from database", 400)
        cursor.close()
        mydb.close()
        print(str(result))
        return sm.StatusModel(result, 200)

    def get_user(self, id:(str, int)) -> sm:
        try:
            mydb = mysql.connector.connect(
                db=os.getenv('DATABASE'),
                host=os.getenv('DATABASE_HOST'),
                user=os.getenv('DATABASE_USER')
            )
            cursor = mydb.cursor()
        except:
            return sm.StatusModel("Error: Connection with database failed", 503)
        try:
            cursor.execute(f"SELECT * FROM user WHERE id = {id}")
            columns = [i[0] for i in cursor.description]
            result = pd.DataFrame(cursor.fetchall(), columns=columns).to_json(orient="records")
        except:
            return sm.StatusModel("Error: Cannot select user from database", 400)
        cursor.close()
        mydb.close()
        return sm.StatusModel(result, 200)
    
    def insert_user(self, req:dict) -> sm:
        try:
            mydb = mysql.connector.connect(
                db=os.getenv('DATABASE'),
                host=os.getenv('DATABASE_HOST'),
                user=os.getenv('DATABASE_USER')
            )
            cursor = mydb.cursor()
        except:
            return sm.StatusModel("Error: Connection with database failed", 503)
        try:
            sql = "INSERT INTO user (id, name, cpf, phone_number, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (req['id'], req['name'], req['cpf'], req['phone_number'], req['created_at'], req['updated_at'])
            cursor.execute(sql, val)
            mydb.commit()
        except:
            return sm.StatusModel("Error: Cannot insert user in database", 400)
        row_change = cursor.rowcount
        cursor.close()
        mydb.close()
        if row_change > 0:
            return sm.StatusModel("Success: User created with success!", 200)
        else:
            return sm.StatusModel("Error: No record inserted!", 500)
    def update_user(self):
        pass
    
    def remove_user(self):
        pass