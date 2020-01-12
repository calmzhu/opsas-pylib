from opsas.utils.BaseDataType import BaseDataType
from dataclasses import dataclass


@dataclass
class BaseDataTypeChild(BaseDataType):
    name: str = ''
    id: str = ''


class TestBaseDateType:
    @classmethod
    def setup_class(cls):
        cls.dict_data = {"name": "test_name", "id": "test_id"}
        cls.test_instance = BaseDataTypeChild(**cls.dict_data)

    def test_property_dict(self):
        assert self.test_instance.dict == self.dict_data

    def test_property_format_str(self):
        print(self.test_instance.format_str)

    def test_get_attr_list(self):
        attrs = BaseDataTypeChild.get_attr_list()
        assert attrs == tuple(self.dict_data.keys())

    def test_create_instance_from_dict(self):
        cls_instance = BaseDataTypeChild.create_instance_from_dict(self.dict_data)
        assert cls_instance == self.test_instance
