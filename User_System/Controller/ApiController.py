import uuid
import datetime

from Controller import InputController
ic = InputController.InputControl()

from Controller import DatabaseController
db = DatabaseController.DatabaseControl()

from Model import StatusModel
sm = StatusModel

class ApiControl:
    def user_list(self) -> sm:
        return db.list_users()
    
    def user_show(self, req:dict) -> sm:
        verify_id = ic.verify_id(req)
        if verify_id and not verify_id.code == 200:
            return verify_id
        return db.get_user(req['id'])

    def user_create(self, req:dict) -> sm:
        req['id'] = uuid.uuid4().hex
        req['created_at'] = datetime.datetime.now()
        req['updated_at'] = datetime.datetime.now()
        verify_requirementes = ic.verify_user_requirements(req)
        if verify_requirementes and not verify_requirementes.code == 200:
            return verify_requirementes
        req['cpf'] = req['cpf'].replace(".", "").replace("-", "")
        return db.insert_user(req)

    def user_update(self) -> sm:
        pass

    def user_remove(self) -> sm:
        verify_id = ic.verify_id(req)
        if verify_id and not verify_id.code == 200:
            return verify_id