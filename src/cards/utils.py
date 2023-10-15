from typing import Any

from pydantic import BaseModel, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema


class StaticUrl(str):
    @staticmethod
    def is_static_url(value: str):
        if not value.startswith('/static/'):
            raise ValueError('static url must be starts with /static/')
        
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(cls.is_static_url, handler(str))
