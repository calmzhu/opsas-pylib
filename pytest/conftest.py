import logging.config
import os
import sys
import yaml
import pytest

test_base = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(os.path.dirname(test_base), 'src'))
environment = os.environ.setdefault("environment", "local")

from opsas.configer.YmlConfiger import YmlConfiger
from opsas.messager.SlackLogHandler import SlackLogHandler

with open(os.path.join(test_base, 'logging.yml'), 'r') as yaml_config:
    logging.config.dictConfig(yaml.safe_load(yaml_config))
basic_logger = logging.getLogger('basic')
configer = YmlConfiger(ordered_file_paths=[os.path.join(test_base, f'config.{environment}.yaml')],
                       logger=basic_logger)

slackHandler = SlackLogHandler(token=configer.get('slack_channel_token'), channel=configer.get('slack_channel'),
                               logger=basic_logger)

slackLogger = logging.getLogger('pytest')


@pytest.fixture(scope='session', autouse=True)
def pytestLogger():
    return slackLogger


@pytest.fixture(scope='session', autouse=True)
def pytestConfiger():
    return configer


@pytest.fixture(scope="session", autouse=True)
def environment():
    return environment
