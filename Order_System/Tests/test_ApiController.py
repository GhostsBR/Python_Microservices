from unittest import TestCase, mock
from Controller import DatabaseController

from Controller import ApiController
ac = ApiController.ApiControl()

from Controller import InputController
ic = InputController.InputControl()

from Model import StatusModel
sm = StatusModel

class TestDatabase(TestCase):
    @mock.patch("Controller.DatabaseController.DatabaseControl.list_orders")
    def test_order_list_works(self, mock_database_list):
        mock_database_list.return_value = sm.StatusModel("Sucess!", 200)
        result_value = ac.order_list()
        self.assertEqual("Sucess!", result_value.content)
        self.assertEqual(200, ac.order_list().code)

    @mock.patch("Controller.DatabaseController.DatabaseControl.list_orders_by_user")
    @mock.patch("Controller.InputController.InputControl.verify_id")
    def test_order_list_by_user_works(self, mock_verify_id, mock_database_orders_by_user):
        mock_verify_id.return_value = True
        mock_database_orders_by_user.return_value = sm.StatusModel([], 200)
        req = {"id": "lTDf51NKbOeCpvRQ08KeHpDBzaZfah"}
        test_result_value = ac.order_list_by_user(req)
        self.assertEqual([], test_result_value.content)
        self.assertEqual(200, test_result_value.code)
        mock_verify_id.return_value = False
        self.assertEqual(400, ac.order_list_by_user(req).code)

    @mock.patch("Controller.DatabaseController.DatabaseControl.get_order")
    @mock.patch("Controller.InputController.InputControl.verify_id")
    def test_order_show_works(self, mock_verify_id, mock_database_get_order):
        mock_verify_id.return_value = True
        mock_database_get_order.return_value = sm.StatusModel([], 200)
        req = {"id": "lTDf51NKbOeCpvRQ08KeHpDBzaZfah"}
        test_result_value = ac.order_show(req)
        self.assertEqual([], test_result_value.content)
        self.assertEqual(200, test_result_value.code)
        mock_verify_id.return_value = False
        self.assertEqual(400, ac.order_show(req).code)
    
    @mock.patch("Controller.DatabaseController.DatabaseControl.insert_order")
    @mock.patch("Controller.InputController.InputControl")
    @mock.patch("Controller.ApiController.datetime")
    def test_order_create_works(self, mock_datetime, mock_inputcontrol, mock_database_insert_order):
        mock_datetime.now.return_value = "2009-01-06 15:08:24.789150"
        mock_inputcontrol.verify_order_requeriments.return_value = sm.StatusModel("sucess", 200)
        mock_inputcontrol.verify_generated_requeriments.return_value = sm.StatusModel("sucess", 200)
        mock_database_insert_order.return_value = sm.StatusModel("sucess", 200)
        self.assertEqual(200, ac.order_create(dict(user_id="rTG6gWrfjyudKO6oVJeM7Gak34qYBt", item_description="product", item_quantity=2, item_price=10.0)).code)
        self.assertEqual(400, ac.order_create(dict()).code)

    @mock.patch("Controller.DatabaseController.DatabaseControl.update_order")
    @mock.patch("Controller.InputController.InputControl.verify_id")
    @mock.patch("Controller.InputController.InputControl.verify_order_requeriments")
    @mock.patch("Controller.ApiController.datetime")
    def test_order_update(self, mock_datetime, mock_verify_order_requeriments, mock_verify_id, mock_database_update_order):
        mock_datetime.now.return_value = "2009-01-06 15:08:24.789150"
        mock_verify_order_requeriments.return_value = sm.StatusModel("sucess", 200)
        mock_verify_id.return_value = True
        mock_database_update_order.return_value = sm.StatusModel("sucess", 200)
        test_return_value = ac.order_update(dict(item_quantity=1, item_price=2))
        self.assertEqual(200, test_return_value.code)

    @mock.patch("Controller.DatabaseController.DatabaseControl.remove_order")
    @mock.patch("Controller.InputController.InputControl.verify_id")
    def test_order_remove(self, mock_verify_id, mock_database_remove_order):
        mock_verify_id.return_value = True
        mock_database_remove_order.return_value = sm.StatusModel("sucess", 200)
        self.assertEqual(200, ac.order_remove({}).code)



