import unittest

from app.main import ItemJsonValidationSerivce


class ItemJsonValidationTestCase(unittest.TestCase):
    def setUp(self):
        self.item_json_string = """{ "ad_network": "FOO",
                          "date": "2019-06-05",
                          "app_name": "LINETV",
                          "unit_id": "55665201314",
                          "request": "100",
                          "revenue": "0.00365325",
                          "imp": "23" }
                          """


    def test_validate_json_obj(self):
        item_json_dict = {"ad_network": "FOO",
                          "date": "2019-06-05",
                          "app_name": "LINETV",
                          "unit_id": "55665201314",
                          "request": "100",
                          "revenue": "0.00365325",
                          "imp": "23"}
        item_json_validation_service = ItemJsonValidationSerivce(item_data=self.item_json_string)
        self.assertEqual(item_json_dict,
                         item_json_validation_service.validate_json_obj())

    def test_validate_dict_value_type(self):
        valid_item_json_dict = {"ad_network": "FOO",
                                "date": "2019-06-05",
                                "app_name": "LINETV",
                                "unit_id": "55665201314",
                                "request": "100",
                                "revenue": "0.00365325",
                                "imp": "23"}
        invalid_item_json_dict = {"ad_network": "FOO",
                                  "date": "2a19-06-05",
                                  "app_name": "LINETV",
                                  "unit_id": "55665201314",
                                  "request": "100",
                                  "revenue": "0.00365325",
                                  "imp": "23"}
        item_json_validation_service = ItemJsonValidationSerivce(item_data=self.item_json_string)
        item_json_validation_service.validate_dict_value_type(valid_item_json_dict)
        self.assertTrue(item_json_validation_service.valid)
        item_json_validation_service.validate_dict_value_type(invalid_item_json_dict)
        self.assertFalse(item_json_validation_service.valid)

    def test_validate_item_json(self):
        item_json_validation_service = ItemJsonValidationSerivce(item_data=self.item_json_string)
        item_json_validation_service.validate_item_json()
        self.assertTrue(item_json_validation_service.valid)


if __name__ == '__main__':
    tests = unittest.TestLoader().loadTestsFromTestCase(ItemJsonValidationTestCase)
    unittest.TextTestRunner(verbosity=2).run(tests)
