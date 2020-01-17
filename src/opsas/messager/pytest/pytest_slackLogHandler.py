import pytest
from ..SlackLogHandler import SlackMessager
from ..SlackLogHandler import SlackLogHandler
import logging
import time


@pytest.fixture(autouse=True)
def pytest_skip_check(environment):
    global pytestmark
    # Todo
    # Add slack config in github to enable slack test in github actions ci
    if environment == "local":
        pytestmark = pytest.mark.skip("Slack Test oonly run in local")


@pytest.fixture(scope='class')
def bot(pytestConfiger, pytestLogger) -> SlackMessager:
    bot = SlackMessager(logger=pytestLogger, channel='opsas', token=pytestConfiger.get('slack_channel_token'))
    yield bot
    bot.session.close()


def pytest_namespace():
    return {"ts": None}


class TestSlackMessager:

    def test_send_message(self, bot: SlackMessager):
        res = bot.send_text_message("Hello Slack")
        pytest.ts = res['ts']
        return res['ts']

    def test_send_thread_message(self, bot: SlackMessager):
        res = bot.send_message(thread_ts=pytest.ts, message="Hello")
        assert res['ok'] is True


@pytest.fixture(scope="class")
def slackLogger(pytestConfiger, pytestLogger):
    pytestLogger.setLevel(pytestConfiger.get("pytest_loglevel"))
    slackLogHandler = SlackLogHandler(token=pytestConfiger.get("slack_channel_token"),
                                      channel=pytestConfiger.get("slack_channel"), title=__file__, logger=pytestLogger)
    slackLogger = logging.getLogger('TestSlackHandler')
    slackLogger.addHandler(slackLogHandler)
    slackLogger.setLevel('DEBUG')
    return slackLogger


class TestSlackHandler:
    def test_log_levels(self, slackLogger):
        for log_method_name in ["info", "debug", "warning", "error", "critical"]:
            log_method = getattr(slackLogger, log_method_name)
            time.sleep(1)
            log_method(log_method_name)
