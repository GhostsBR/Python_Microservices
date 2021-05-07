from unittest import TestCase, mock
import os

from Controller import InputController
ic = InputController.InputControl()

from Model import StatusModel
sm = StatusModel

class InputTest(TestCase):
    @mock.patch("os.getenv")
    def test_verify_auth_works(self, mock_getenv):
        mock_getenv.return_value = "0FCMXohT0M6ZsLCAADkZiCsPu06y57"
        self.assertFalse(ic.verify_auth(dict()))
        self.assertTrue(ic.verify_auth(dict(auth="0FCMXohT0M6ZsLCAADkZiCsPu06y57")))

    @mock.patch("Controller.InputController.InputControl.verify_item_price")
    @mock.patch("Controller.InputController.InputControl.verify_item_quantity")
    def test_verify_order_requeriments_works(self, mock_item_quantity, verify_item_price):
        self.assertEqual(400, ic.verify_order_requeriments(dict()).code)
        self.assertEqual(400, ic.verify_order_requeriments(dict()).code)
        mock_item_quantity.return_value = False
        self.assertEqual(400, ic.verify_order_requeriments(dict(user_id="", item_description="", item_quantity="", item_price="")).code)
        mock_item_quantity.return_value = True
        verify_item_price.return_value = False
        self.assertEqual(400, ic.verify_order_requeriments(dict(user_id="", item_description="", item_quantity="", item_price="")).code)
        verify_item_price.return_value = True
        self.assertIsNone(ic.verify_order_requeriments(dict(user_id="", item_description="", item_quantity="", item_price="")))

    @mock.patch("Controller.InputController.InputControl.verify_total_value")
    def test_verify_generated_requeriments_works(self, mock_verify_total_value):
        self.assertEqual(500, ic.verify_generated_requeriments(dict()).code)
        mock_verify_total_value.return_value = False
        self.assertEqual(400, ic.verify_generated_requeriments(dict(id="", updated_at="", total_value="")).code)
    
    def test_verify_item_quantity_works(self):
        self.assertFalse(ic.verify_item_quantity("d"))
        self.assertTrue(ic.verify_item_quantity(1))
    
    def test_verify_item_price_works(self):
        self.assertFalse(ic.verify_item_price("d"))
        self.assertTrue(ic.verify_item_price(1))
    
    def test_verify_total_value_works(self):
        self.assertFalse(ic.verify_total_value("d"))
        self.assertTrue(ic.verify_total_value(1))

    def test_verify_id_works(self):
        self.assertFalse(ic.verify_id(dict()))
        self.assertTrue(ic.verify_id(dict(id="")))