import uuid
import datetime
import requests

from Controller import InputController
ic = InputController.InputControl()

from Controller import DatabaseController
db = DatabaseController.DatabaseControl()

from Model import StatusModel
sm = StatusModel

class ApiControl:
    def order_list(self) -> sm:
        return db.list_orders()

    def order_list_by_user(self, req:dict) -> sm:
        verify_id = ic.verify_id(req)
        if not verify_id: return sm.StatusModel("Error: id is invalid!", 400)
        return db.list_orders_by_user(req['id'])
    
    def order_show(self, req:dict) -> sm:
        verify_id = ic.verify_id(req)
        if not verify_id: return sm.StatusModel("Error: Invalid ID!", 400)
        return db.get_order(req['id'])

    def order_create(self, req: dict) -> sm:
        req['id'] = uuid.uuid4().hex
        req['created_at'] = datetime.datetime.now()
        req['updated_at'] = datetime.datetime.now()
        verify_order = ic.verify_order_requeriments(req)
        if verify_order and not verify_order.code == 200: return verify_order
        req['total_value'] = req['item_quantity'] * req['item_price']
        verify_generated = ic.verify_generated_requeriments(req)
        if verify_generated and not verify_generated.code == 200: return verify_generated
        req['total_value'] = int(req['item_quantity']) * int(req['item_price'])
        return db.insert_order(req)

        
    def order_update(self, req:dict) -> sm:
        req['updated_at'] = datetime.datetime.now()
        verify_order = ic.verify_order_requeriments(req)
        if verify_order and not verify_order.code == 200: return verify_order
        verify_id = ic.verify_id(req)
        if not verify_id: return sm.StatusModel("Error: id not found!", 400)
        req['total_value'] = int(req['item_quantity']) * int(req['item_price'])
        return db.update_order(req)

    def order_remove(self, req:dict) -> sm:
        verify_id = ic.verify_id(req)
        if not verify_id: return sm.StatusModel("Error: id not found!", 400)
        return db.remove_order(req)
