import logging.config
import os
import sys
import yaml
import pytest

test_base = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(os.path.dirname(test_base), 'src'))
environment = os.environ.setdefault("environment", "local")

from opsas.configer.YmlConfiger import YmlConfiger

with open(os.path.join(test_base, 'logging.yml'), 'r') as yaml_config:
    logging.config.dictConfig(yaml.safe_load(yaml_config))
logger = logging.getLogger()
configer = YmlConfiger(ordered_file_paths=[os.path.join(test_base, f'config.{environment}.yaml')],
                       logger=logging.getLogger())


@pytest.fixture(scope='session', autouse=True)
def pytestLogger():
    return logger


@pytest.fixture(scope='session', autouse=True)
def pytestConfiger():
    return configer


@pytest.fixture(scope="session", autouse=True)
def environment():
    return environment
