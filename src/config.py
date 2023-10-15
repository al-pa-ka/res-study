from pydantic import BaseModel
from pathlib import Path

import json

class Config(BaseModel):
    secret: str
    secret_for_passwords: str


with open(
    Path(Path(__file__).parent.parent.joinpath('config.json'))
    .resolve(), 'r'
) as config_file:
    config_data = config_file.read()
    config_dict = json.loads(config_data)


config = Config(**config_dict)
