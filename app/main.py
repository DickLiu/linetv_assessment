import json
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ItemJsonValidationSerivce(object):
    def __init__(self, item_data):
        self.item_data = item_data
        self.valid = False
        self.error_msg = None

    def validate_json_obj(self):
        try:
            # turn json to python dict
            item_dict = json.loads(self.item_data)
        except Exception as e:
            self.valid = False
            self.error_msg = e.args[0]
            return None
        self.valid = True
        return item_dict

    def validate_dict_value_type(self, item_dict):
        """
        {
         "ad_network": "FOO",
         "date": "2019-06-05",
         "app_name": "LINETV",
         "unit_id": "55665201314",
         "request": "100",
         "revenue": "0.00365325",
         "imp": "23"
        }
        :return:
        """
        validators = {
            "ad_network": lambda x: isinstance(x, str),
            "date": lambda x: isinstance(x, str) and type(datetime.strptime(x, "%Y-%m-%d")) == datetime,
            "app_name": lambda x: isinstance(x, str),
            "unit_id": lambda x: isinstance(x, str) and type(int(x)) == int,
            "request": lambda x: isinstance(x, str) and type(int(x)) == int,
            "revenue": lambda x: isinstance(x, str) and type(float(x)) == float,
            "imp": lambda x: isinstance(x, str) and type(int(x)) == int,
        }
        try:
            for k, v in item_dict.items():
                self.valid = validators.get(k, lambda x: False)(v)
        except Exception as e:
            self.valid = False
            self.error_msg = "{}, {}".format(k, e.args[0])

    def validate_item_json(self):
        # 先確認string是否符合json的格式
        item_dict = self.validate_json_obj()
        if self.valid:
            self.validate_dict_value_type(item_dict)
            if self.valid:
                # 將 item data寫入資料庫
                print("item_json is valid and will be stored in database.")
            else:
                print("item_json has invalid value: {}".format(self.error_msg))
        else:
            print("item_json is not a valid json format: {}".format(self.error_msg))
