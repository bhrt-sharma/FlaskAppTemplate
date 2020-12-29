from easydict import EasyDict as edict
from pathlib import Path

def get_config():
    conf = edict()
    conf.data_path = Path('data')
    conf.image_limit=3
    return conf


class ServiceConfig:
    SECRET_KEY = '6573ffa8b04f46ecae79769d86f581cf'
