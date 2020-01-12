import pytest
import os
import logging
from opsas.configer.YmlConfiger import YmlConfiger

logging.basicConfig()
logger = logging.getLogger('pytest')
formatter_str = "%(asctime)s %(message)s"

test_base = os.path.dirname(__file__)
environment = os.environ.setdefault("environment", "local")

configer = YmlConfiger(ordered_file_paths=[os.path.join(test_base, f'config.{environment}.yaml')], logger=logger)

logger.setLevel(configer.get("pytest_loglevel"))
logging.basicConfig(format=formatter_str, datefmt='%F %H:%M %S', level="DEBUG")


@pytest.fixture(scope='session', autouse=True)
def pytestLogger():
    return logger


@pytest.fixture(scope='session', autouse=True)
def pytestConfiger(pytestLogger):
    return configer


@pytest.fixture(scope="session", autouse=True)
def environment():
    return environment
