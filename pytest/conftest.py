import logging.config
import os
import sys
import yaml

import pytest

test_base = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(os.path.dirname(test_base), 'src'))

from opsas.utils.ConfigClient import ConfigClient

with open(os.path.join(test_base, 'logging.yml'), 'r') as yaml_config:
    logging.config.dictConfig(yaml.safe_load(yaml_config))


@pytest.fixture(scope='session', autouse=True)
def environment():
    return os.environ.setdefault("environment", "local")


@pytest.fixture(scope='session', autouse=True)
def pytestLogger():
    _ = logging.getLogger('pytest')
    return _


@pytest.fixture(scope='session', autouse=True)
def pytestConfigClient(pytestLogger, environment):
    return ConfigClient(logger=pytestLogger, config_path=os.path.join(test_base, f"config.{environment}.yaml"))
