import pytest
from opsas.utils.ConfigClient import ConfigClient
import os


@pytest.fixture(scope='class')
def configClient(pytestLogger):
    os.environ.setdefault("env", "test")
    base_dir = os.path.dirname(__file__)
    _ = ConfigClient(logger=pytestLogger, config_path=os.path.join(base_dir, 'config.yaml'))
    return _


class TestConfigClient:
    def test_get_config(self, configClient):
        assert configClient.get('port') == 8000

    def test_get_environment_config(self, configClient):
        assert configClient.get("env") == "test"
