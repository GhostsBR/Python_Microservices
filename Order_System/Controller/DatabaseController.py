import os
import mysql.connector
import pandas as pd
import requests
import json
from ast import literal_eval

from dotenv import load_dotenv
load_dotenv()

from Model import StatusModel
sm = StatusModel



class DatabaseControl:
    def list_orders(self) -> sm:
        try:
            mydb = mysql.connector.connect(
                db=os.getenv('DATABASE'),
                host=os.getenv('DATABASE_HOST'),
                user=os.getenv('DATABASE_USER')
            )
            cursor = mydb.cursor()
        except:
            return sm.StatusModel("Error: Connection with database failed", 503)
        cursor.execute("SELECT * FROM `order`")
        columns = [i[0] for i in cursor.description]
        result = pd.DataFrame(cursor.fetchall(), columns=columns).to_json(orient="records")
        cursor.close()
        mydb.close()
        return sm.StatusModel(result, 200)

    def list_orders_by_user(self, id) -> sm:
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
            cursor.execute(f"SELECT * FROM `order` WHERE `user_id` = '{id}'")
        except:
            return sm.StatusModel("Error: Cannot get all orders from database", 400)
        columns = [i[0] for i in cursor.description]
        result = pd.DataFrame(cursor.fetchall(), columns=columns).to_json(orient="records")
        cursor.close()
        mydb.close()
        literal_result = literal_eval(result)
        res = requests.get(os.getenv('USER_SYSTEM_URL_GET_USERS'), json={"auth":os.getenv('USER_SYSTEM_AUTH')})
        users = json.loads(res.content)
        print(len(users))
        for i in range(len(literal_result)):
            for x in range(len(users)):
                if literal_result[i]['user_id'] == users[x]['id']:
                    print("funfou")
        return sm.StatusModel(result, 200)

    def get_order(self, id:(str, int)) -> sm:
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
            cursor.execute(f"SELECT * FROM `order` WHERE `id` = '{id}'")
        except:
            return sm.StatusModel("Error: Cannot get all orders from database", 400)
        columns = [i[0] for i in cursor.description]
        result = pd.DataFrame(cursor.fetchall(), columns=columns).to_json(orient="records")
        cursor.close()
        mydb.close()
        return sm.StatusModel(result, 200)
    
    def insert_order(self, req:dict) -> sm:
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
            sql = "INSERT INTO `order` (id, user_id, item_description, item_quantity, item_price, total_value, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (req['id'], req['user_id'], req['item_description'], req['item_quantity'], req['item_price'], req['total_value'], req['created_at'], req['updated_at'])
            cursor.execute(sql, val)
            mydb.commit()
        except:
            return sm.StatusModel("Error: Cannot insert order in database", 400)
        row_change = cursor.rowcount
        cursor.close()
        mydb.close()
        if row_change > 0:
            return sm.StatusModel("Success: Order created with success!", 200)
        else:
            return sm.StatusModel("Error: No record inserted!", 500)
    def update_order(self, req:dict) -> sm:
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
            sql = "UPDATE `order` SET `user_id` = %s, `item_description` = %s, `item_quantity` = %s, `item_price` = %s, `total_value` = %s, `updated_at` = %s WHERE `id` = %s"
            val = (req['user_id'], req['item_description'], req['item_quantity'], req['item_price'], req['total_value'], req['updated_at'], req['id'])
            cursor.execute(sql, val)
            mydb.commit()
        except:
            return sm.StatusModel("Error: Cannot update order in database", 400)
        row_change = cursor.rowcount
        cursor.close()
        mydb.close()
        if row_change > 0:
            return sm.StatusModel("Success: Order updated with success!", 200)
        else:
            return sm.StatusModel("Error: No record updated!", 500)

    def remove_order(self, req:dict) -> sm:
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
            sql = "DELETE FROM `order` WHERE `id` = %s"
            val = (req['id'],)
            cursor.execute(sql, val)
            mydb.commit()
        except:
            return sm.StatusModel("Error: Cannot delete order from database", 400)
        row_change = cursor.rowcount
        cursor.close()
        mydb.close()
        if row_change > 0:
            return sm.StatusModel("Success: Order deleted with success!", 200)
        else:
            return sm.StatusModel("Error: No record updated!", 400)
        